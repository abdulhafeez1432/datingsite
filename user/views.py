from django.conf.urls import url
from django.http.response import Http404
from django.shortcuts import render
from user.models import *
from django.contrib.auth import login as mylogin
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from .forms import *
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import  auth, messages
from django.contrib.auth import logout as django_logout
from app.models import *
from datetime import datetime, timedelta
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from nikkah.settings import EMAIL_HOST_USER, DEFAULT_FROM_EMAIL

from user import  helpers

# Create your views here.


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    
    return render(request, 'home.html')


class FemaleSignUpView(CreateView):
    model = User
    form_class = FemaleSignUpForm
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Female'
        return super().get_context_data(**kwargs)


    def form_valid(self, form):
        user = form.save()
        mylogin(self.request, user)
        return redirect('female:dashboard')


class MaleSignUpView(CreateView):
    model = User
    form_class = MaleSignUpForm
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Male'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        
        user = form.save()
        mylogin(self.request, user)
        return redirect('male:dashboard')



def login(request):
    

        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            if form.is_valid():
                user = auth.authenticate(username=username, password=password)

                if user is not None:
                    auth.login(request, user)

                    if request.user.is_female:
                        last_login = request.user.last_login                        
                        proposal_list = InterestData.objects.filter(interestin=request.user).filter(updated_at__gt=last_login)              
                        
                        try:
                            if proposal_list:
                                messages.success(request, "Notification: You have new Proposal since your last login")
                        except:
                            pass
                        
                        return redirect('female:dashboard')

                    elif request.user.is_male:
                        last_login = request.user.last_login
                        proposal_list = InterestData.objects.filter(interestin=request.user).filter(created_at__gt=last_login)
                        if proposal_list:
                            messages.success(request, " Notification: You have new Proposal since your last login")
                        
                        return redirect('male:dashboard')
                                                
            
            else:
                args = {'form': form}
                return render(request, 'registration/login.html', args)

        else:
            form = AuthenticationForm

        args = {'form': form}
        return render(request, 'registration/login.html', args)


def logout_user(request):
    django_logout(request)
    return redirect('login')





@method_decorator([login_required], name='dispatch')
class CreateSubscription2(CreateView):
    template_name = "general.html"
    model = Subscription
    form_class = SubscriptionForm

    #success_url = reverse_lazy('male:dashboard')
    
    def form_valid(self, form):            
        
        p = form.save(commit=False)
        p.user = self.request.user
        p.start_time = datetime.now()
        p.api_key  = helpers.generate_activation_key(),
        p.end_time = datetime.now() + timedelta(days=p.plan.duration_days)
        p.save()
        messages.success(self.request, 'The Details has been Added Successully!')
        return redirect('make_payment', p.user)




def CreateSubscription(request, pk):
    user = get_object_or_404(User, pk=pk)
    subscription = Subscription.objects.filter(user=user).filter(payment=False).first()
    template_name = "subscrible.html"
    
    if subscription:
         return redirect('make_payment', user.pk)


    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.user = request.user
            p.start_time = datetime.now()
            p.api_key  = helpers.generate_activation_key(),
            p.end_time = datetime.now() + timedelta(days=p.plan.duration_days)
            p.save()
            messages.success(request, 'The Details has been Added Successully!')
            return redirect('make_payment', p.user.id)
    else:
        form = SubscriptionForm()


    

    return render(request, template_name, {'form': form})





def EditSubscription(request, pk):
    user = get_object_or_404(User, pk=pk)
    subscription = Subscription.objects.filter(user=user).filter(payment=False).first()
    template_name = "subscrible.html"
    
    


    if request.method == 'POST':
        form = SubscriptionForm(request.POST, instance=subscription)        
        if form.is_valid():
            p = form.save(commit=False)
            p.user = request.user
            p.start_time = datetime.now()
            p.api_key  = helpers.generate_activation_key(),
            p.end_time = datetime.now() + timedelta(days=p.plan.duration_days)
            p.save()
            messages.success(request, 'The Details has been Added Successully!')
            return redirect('make_payment', p.user.id)
    else:
        form = SubscriptionForm(instance=subscription)


    

    return render(request, template_name, {'form': form})


@login_required
def Payment(request, pk):
    templates_name = 'payment/payment.html'
    user = get_object_or_404(User, pk=pk) 
    d = Subscription.objects.filter(user=user).filter(payment=False).first()
    
    if d.user != request.user:
        return redirect('logout')

    return render(request, templates_name, {'d': d})



def SuccessPayment(request):
    templates_name = 'payment/successpayment.html'
    txref = request.Get['reference'].strip()
    try:
        subscription = get_object_or_404(Subscription, api_key=txref)
    except Exception as e:
        raise Http404("Invalid Invoice PIN")
    url = 'https://api.flutterwave.com/v3/transactions/123456/verify'
    SEC_KEY = 'FLWSECK_TEST-25a0ef49ef0e26d8cb885d3983119f5b-X'
    response = request.get(url, 
        headers={'Authorization: Bearer {{SEC_KEY}}'}) 
    json_response = response.json()
    print(json_response)
    if json_response['status'] == True:
        if json_response['status'] == 'success' and \
            json_response['data']['amount'] == ((subscription.plan.price)) and \
                json_response['data']['tx_ref'] == txref:

            subject = 'Payment Confirmation'
            message = "Your Payment has been successfully done. This is a confirmation Message with Your Recipte"
            to_email = subscription.user.email
            print(to_email)
            #email = send_mail(subject, message, settings.SERVER_EMAIL, [to_email], fail_silently = False)

            return render(request, templates_name)

    return render(request, templates_name, {'subscription': subscription})








def SuccessPayment(request, pk):
    templates_name = 'payment/successpayment.html'

    d = get_object_or_404(Subscription, pk=pk)

    subject = 'Payment Confirmation'
    message = "Your Payment has been successfully done. This is a confirmation Message with Your Recipte"
    to_email = d.user.email
    #email = send_mail(subject, message, settings.SERVER_EMAIL, [to_email], fail_silently = False)
    Subscription.objects.filter(pk=d.id).update(payment=True)
    

    return render(request, templates_name, {'d': d})





def ViewSubscription(request, pk):
    templates_name = 'payment/viewsubscription.html'
    subscription = get_object_or_404(Subscription, pk=pk, payment=True)
    return render(request, templates_name, {'subscription': subscription})




def error_404_view(request, exception):
    return render(request,'error_404.html')