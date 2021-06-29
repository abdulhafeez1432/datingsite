from django.shortcuts import render
from user.models import *
from app.models import *
from django.contrib.auth import login as mylogin
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from ..forms import *
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import  auth, messages
from django.contrib.auth import logout as django_logout
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from ..decorators import male_required






@login_required
@male_required
def Dashboard(request):
    
    user = User.objects.filter(is_female=True).filter(profile__available=True)
    last_login = request.user.last_login
    proposal_list = InterestData.objects.filter(interestin=request.user).filter(created_at__gt=last_login).filter(read=False)
    
    if proposal_list:
        messages.success(request, " Notification: You have new Proposal since your last login")
    
    malequestion = Question.objects.filter(user=request.user).first()
    content = {'user': user, 'malequestion': malequestion, 'proposal_list': proposal_list}
    return render(request, 'male/dashboard.html', content)







#@login_required
@method_decorator([login_required, male_required], name='dispatch')
class MaleProfile(CreateView):
    template_name = "male/profile.html"
    model = Profile
    form_class = ProfileForm
    #success_url = reverse_lazy('male:dashboard')

    def form_valid(self, form): 
              
        
        p = form.save(commit=False)
        p.user = self.request.user
        p.save()
        messages.success(self.request, 'The Profile has been Added Successully!')
        return redirect('male:dashboard')



@method_decorator([login_required, male_required], name='dispatch')
class EditMaleProfile(UpdateView):
    template_name = "male/profile.html"
    model = Profile
    form_class = ProfileForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        super(EditMaleProfile, self).save(form)

    def get_success_url(self):
        messages.success(self.request, 'The Profile has been Updated Successully!')
        return reverse_lazy('male:dashboard')






@method_decorator([login_required, male_required], name='dispatch')
class MaleAboutMe(CreateView):
    template_name = "male/general.html"
    model = AboutMe
    form_class = AboutMeForm
    #success_url = reverse_lazy('male:dashboard')

    def form_valid(self, form): 
              
        
        p = form.save(commit=False)
        p.user = self.request.user
        p.save()
        messages.success(self.request, 'The Details has been Added Successully!')
        return redirect('male:dashboard')



@method_decorator([login_required, male_required], name='dispatch')
class EditMaleAboutMe(UpdateView):
    template_name = "male/general.html"
    model = AboutMe
    form_class = AboutMeForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        super(EditMaleAboutMe, self).save(form)

    def get_success_url(self):
        messages.success(self.request, 'The Profile has been Updated Successully!')
        return reverse_lazy('male:dashboard')






@method_decorator([login_required, male_required], name='dispatch')
class MaleReligion(CreateView):
    template_name = "male/general.html"
    model = Religion
    form_class = ReligionForm
    #success_url = reverse_lazy('male:dashboard')

    def form_valid(self, form): 
              
        
        p = form.save(commit=False)
        p.user = self.request.user
        p.save()
        messages.success(self.request, 'The Details has been Added Successully!')
        return redirect('male:dashboard')

@method_decorator([login_required, male_required], name='dispatch')
class EditMaleReligion(UpdateView):
    template_name = "male/general.html"
    model = Religion
    form_class = ReligionForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        super(EditMaleReligion, self).save(form)

    def get_success_url(self):
        messages.success(self.request, 'The Details has been Updated Successully!')
        return reverse_lazy('male:dashboard')




@method_decorator([login_required, male_required], name='dispatch')
class MaleCharacter(CreateView):
    template_name = "male/general.html"
    model = Character
    form_class = CharacterForm
    #success_url = reverse_lazy('male:dashboard')

    def form_valid(self, form): 
              
        
        p = form.save(commit=False)
        p.user = self.request.user
        p.save()
        messages.success(self.request, 'The Details has been Added Successully!')
        return redirect('male:dashboard')


@method_decorator([login_required, male_required], name='dispatch')
class EditMaleCharacter(UpdateView):
    template_name = "male/general.html"
    model = Character
    form_class = CharacterForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        super(EditMaleCharacter, self).save(form)

    def get_success_url(self):
        messages.success(self.request, 'The Details has been Updated Successully!')
        return reverse_lazy('male:dashboard')





@method_decorator([login_required, male_required], name='dispatch')
class MaleFamily(CreateView):
    template_name = "male/general.html"
    model = Family
    form_class = FamilyForm
    #success_url = reverse_lazy('male:dashboard')

    def form_valid(self, form): 
              
        
        p = form.save(commit=False)
        p.user = self.request.user
        p.save()
        messages.success(self.request, 'The Family Profile has been Added Successully!')
        return redirect('male:dashboard')



@method_decorator([login_required, male_required], name='dispatch')
class EditMaleFamily(UpdateView):
    template_name = "male/general.html"
    model = Family
    form_class = FamilyForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        super(EditMaleFamily, self).save(form)

    def get_success_url(self):
        messages.success(self.request, 'The Details has been Updated Successully!')
        return reverse_lazy('male:dashboard')





@method_decorator([login_required, male_required], name='dispatch')
class MaleEducation(CreateView):
    template_name = "male/general.html"
    model = Education
    form_class = EducationForm
    #success_url = reverse_lazy('male:dashboard')

    def form_valid(self, form): 
              
        
        p = form.save(commit=False)
        p.user = self.request.user
        p.save()
        messages.success(self.request, 'The Education has been Added Successully!')
        return redirect('male:dashboard')



@method_decorator([login_required, male_required], name='dispatch')
class EditMaleEducation(UpdateView):
    template_name = "male/general.html"
    model = Family
    form_class = FamilyForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        super(EditMaleEducation, self).save(form)

    def get_success_url(self):
        messages.success(self.request, 'The Details has been Updated Successully!')
        return reverse_lazy('male:dashboard')





@method_decorator([login_required, male_required], name='dispatch')
class MaleContact(CreateView):
    template_name = "male/general.html"
    model = Contact
    form_class = ContactForm
    #success_url = reverse_lazy('male:dashboard')

    def form_valid(self, form): 
              
        
        p = form.save(commit=False)
        p.user = self.request.user
        p.save()
        messages.success(self.request, 'The Contact Details has been Added Successully!')
        return redirect('male:dashboard')




@method_decorator([login_required, male_required], name='dispatch')
class EditMaleContact(UpdateView):
    template_name = "male/general.html"
    model = Contact
    form_class = ContactForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        super(EditMaleContact, self).save(form)

    def get_success_url(self):
        messages.success(self.request, 'The Details has been Updated Successully!')
        return reverse_lazy('male:dashboard')









@male_required
@login_required
def FemaleDetails(request, pk):
    #details = get_object_or_404(Profile, pk=pk)
    female = get_object_or_404(User, pk=pk)
    taker = TakenQuestion.objects.filter(question__user=female).filter(taker=request.user).first()
    interest = InterestData.objects.filter(interester=request.user).filter(interestin=female).first()
    subscription = Subscription.objects.filter(user=request.user).filter(payment=True).filter(disable=False)
    print(subscription)
    
    
    content = {'female': female, 'taker': taker, 'interest': interest, 'subscription': subscription}
    return render(request, 'male/details.html', content)



def ShowQuestion(request, pk):
    female = get_object_or_404(User, pk=pk)
    print(female)
    question = Question.objects.filter(user=female)
    print(question)
    return render(request, 'male/interest.html', {'question': question})


def QuestionAnswer(request, pk):

    if TakenQuestion.objects.filter(question__user=pk).filter(taker=request.user):
        messages.success(request, 'You Have Shown the Interest before Now. Just Wait for her response!')
        return redirect('male:dashboard')

    user = get_object_or_404(User, pk=pk)
    
    to_email = user.email
    sender_username =  request.user.username
   
    
    question = Question.objects.filter(user=user).order_by('?')
    form = ShowInterestForm()


    if request.method == 'POST':

        question_pk = request.POST.getlist('question_pk', False)
        answer =  request.POST.getlist('choice_pk', False)

        form = ShowInterestForm(request.POST)

        if form.is_valid():
            note = form.cleaned_data.get('note')
            show = form.save(commit=False)                
            show.interester = request.user
            show.interestin = user
            show.status = 'I'
            show.save()

            

            subject = f'You have a Proposal form { sender_username }'
            send_mail(subject, note, settings.SERVER_EMAIL, [to_email])
            print(send_mail)

           


        with transaction.atomic():

            for x, y in zip(question_pk, answer):

                k = Question.objects.get(id=x)    #print(x,y)

                z = TakenQuestion(taker=request.user, question=k, answer=y)
                z.save()
              
                
            messages.success(request, 'You Interest has been Sent to her Successully!')
            return redirect('male:dashboard')

    return render(request, 'male/interest.html', {'question': question, 'user': user, 'form': form})








def MyInterest(request, pk):

    if InterestData.objects.filter(interestin=pk).filter(interester=request.user):
        messages.success(request, 'You Have Shown the Interest before Now. Just Wait for her response!')
        return redirect('male:dashboard')

    female = get_object_or_404(User, pk=pk)
    form = ShowInterestForm()

    if request.method == 'POST':  
        form = ShowInterestForm(request.POST)
        if form.is_valid():
            show = form.save(commit=False)                
            show.interester = request.user
            show.interestin = female
            show.status = 'I'
            show.save()
            messages.success(request, 'You Interest has been Sent to her Successully!')
            return redirect('male:dashboard')

    return render(request, 'male/general.html', {'form': form})






def AddTypedQuestion(request):

      
    context = {'user': user, 'question': question}
    return render(request, 'male/interest.html', context)


def ExamCompleted(request):
    return render(request, 'male/completed.html')
    
   
    
