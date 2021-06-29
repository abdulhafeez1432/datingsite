from django.shortcuts import render
from user.models import *
from django.contrib.auth import login as mylogin
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import *
from ..forms import *
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import  auth, messages
from django.contrib.auth import logout as django_logout
from app.models import *
from datetime import date 
from django.forms import inlineformset_factory
from ..decorators import *

@login_required
@female_required
def Dashboard(request):
    user = User.objects.filter(is_male=True).filter(profile__available=True)
    femalequestion = Question.objects.filter(user=request.user).first()
    
    last_login = request.user.last_login
    
    proposal_list = InterestData.objects.filter(interestin=request.user).filter(created_at__gt=last_login).filter(read=False)
    
    
    if proposal_list:
        messages.error(request, " Notification: You have Proposal that is unread")

    context = {'user': user, 'femalequestion': femalequestion, 'proposal_list': proposal_list }
    
    return render(request, 'female/dashboard.html', context)






@method_decorator([login_required, female_required], name='dispatch')
class FemaleProfile(CreateView):
    template_name = "female/profile.html"
    model = Profile
    form_class = ProfileForm
    #success_url = reverse_lazy('male:dashboard')

    def form_valid(self, form): 
              
        
        p = form.save(commit=False)
        p.user = self.request.user
        p.save()
        messages.success(self.request, 'The Profile has been Added Successully!')
        return redirect('female:dashboard')



@method_decorator(login_required, name='dispatch')
#path("edit_female_profile/<int:pk>/", female.EditFemaleProfile.as_view(), name='edit_female_profile'),
class EditFemaleProfile(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "female/profile.html"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        super(EditFemaleProfile, self).save(form)

    def get_success_url(self):
        messages.success(self.request, 'The Profile has been Updated Successully!')
        return reverse_lazy('female:dashboard')


    """  
    def get_queryset(self):
        #user = get_object_or_404(User, pk=self.kwargs['pk'])
        return User.objects.filter(pk=self.request.user) 
        
    """








@method_decorator(login_required, name='dispatch')
class FemaleFamily(CreateView):
    template_name = "female/general.html"
    model = Family
    form_class = FamilyForm
    #success_url = reverse_lazy('male:dashboard')

    def form_valid(self, form): 
              
        
        p = form.save(commit=False)
        p.user = self.request.user
        p.save()
        messages.success(self.request, 'The Family Profile has been Added Successully!')
        return redirect('female:dashboard')


@method_decorator(login_required, name='dispatch')
class EditFemaleFamily(UpdateView):
    model = Family
    form_class = FamilyForm
    template_name = "female/general.html"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        super(EditFemaleFamily, self).save(form)

    def get_success_url(self):
        messages.success(self.request, 'The Profile has been Updated Successully!')
        return reverse_lazy('female:dashboard')




@method_decorator(login_required, name='dispatch')
class FemaleEducation(CreateView):
    template_name = "female/general.html"
    model = Education
    form_class = EducationForm
    #success_url = reverse_lazy('male:dashboard')

    def form_valid(self, form): 
              
        
        p = form.save(commit=False)
        p.user = self.request.user
        p.save()
        messages.success(self.request, 'The Education has been Added Successully!')
        return redirect('female:dashboard')



@method_decorator(login_required, name='dispatch')
class EditFemaleEducation(UpdateView):
    model = Education
    form_class = EducationForm
    template_name = "female/general.html"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        super(EditFemaleEducation, self).save(form)

    def get_success_url(self):
        messages.success(self.request, 'The Profile has been Updated Successully!')
        return reverse_lazy('female:dashboard')



@method_decorator(login_required, name='dispatch')
class FemaleContact(CreateView):
    template_name = "female/general.html"
    model = Contact
    form_class = ContactForm
    #success_url = reverse_lazy('male:dashboard')

    def form_valid(self, form): 
              
        
        p = form.save(commit=False)
        p.user = self.request.user
        p.save()
        messages.success(self.request, 'The Contact Details has been Added Successully!')
        return redirect('female:dashboard')



@method_decorator(login_required, name='dispatch')
class EditFemaleContact(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = "female/general.html"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        super(EditFemaleContact, self).save(form)

    def get_success_url(self):
        messages.success(self.request, 'The Profile has been Updated Successully!')
        return reverse_lazy('female:dashboard')


@method_decorator(login_required, name='dispatch')
class FemaleAboutMe(CreateView):
    template_name = "female/general.html"
    model = AboutMe
    form_class = AboutMeForm
    

    def form_valid(self, form): 
        p = form.save(commit=False)
        p.user = self.request.user
        p.save()
        messages.success(self.request, 'The Details has been Added Successully!')
        return redirect('female:dashboard')


@method_decorator(login_required, name='dispatch')
class EditFemaleAboutMe(UpdateView):
    model = AboutMe
    form_class = AboutMeForm
    template_name = "female/general.html"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        super(EditFemaleAboutMe, self).save(form)

    def get_success_url(self):
        messages.success(self.request, 'The Profile has been Updated Successully!')
        return reverse_lazy('female:dashboard')


@method_decorator(login_required, name='dispatch')
class FemaleReligion(CreateView):
    template_name = "female/general.html"
    model = Religion
    form_class = ReligionForm
    #success_url = reverse_lazy('male:dashboard')

    def form_valid(self, form): 
              
        
        p = form.save(commit=False)
        p.user = self.request.user
        p.save()
        print("Hello World")
        messages.success(self.request, 'The Details has been Added Successully!')
        return redirect('female:dashboard')



@method_decorator(login_required, name='dispatch')
#path("edit_female_profile/<int:pk>/", female.EditFemaleProfile.as_view(), name='edit_female_profile'),
class EditFemaleReligion(UpdateView):
    model = Religion
    form_class = ReligionForm
    template_name = "female/general.html"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        super(EditFemaleReligion, self).save(form)

    def get_success_url(self):
        messages.success(self.request, 'The Profile has been Updated Successully!')
        return reverse_lazy('female:dashboard')
    





@method_decorator(login_required, name='dispatch')
class FemaleCharacter(CreateView):
    template_name = "female/general.html"
    model = Character
    form_class = CharacterForm
    #success_url = reverse_lazy('male:dashboard')

    def form_valid(self, form): 
              
        
        p = form.save(commit=False)
        p.user = self.request.user
        p.save()
        messages.success(self.request, 'The Details has been Added Successully!')
        return redirect('female:dashboard')



@method_decorator(login_required, name='dispatch')
class EditFemaleCharacter(UpdateView):
    model = Character
    form_class = Character
    template_name = "female/general.html"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        super(EditFemaleCharacter, self).save(form)

    def get_success_url(self):
        messages.success(self.request, 'The Profile has been Updated Successully!')
        return reverse_lazy('female:dashboard')
    


@login_required
@female_required
def AddQuestion(request):  
    
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            messages.success(request, 'You may now add answers/options to the question.')
            return redirect('question_change', question.pk)
    else:
        form = QuestionForm()

    return render(request, 'addquestion.html', {'form': form})






def QuestionList(request):
    pass



def DeleteQuestion(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk )
    question.delete()

    messages.success(request, 'Question Has Been Succesfully Deleted!')
    return redirect('all_question')





@login_required
def EditQuestion(request, question_pk):    
    
    question = get_object_or_404(Question, pk=question_pk)
    


    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
       
        if form.is_valid():
            form.save()
                
            messages.success(request, 'Question Has Been Succesfully Updated!')
            return redirect('all_question')
    else:
        form = QuestionForm(instance=question)
       

    return render(request, 'updatequestion.html', {'form': form})








def AllQuestion(request):
    questions = Question.objects.filter(user=request.user).annotate(answers_count=Count('answers'))
    print(questions)
    context = {'questions': questions}
    return render(request, 'allquestions.html', context)

def MyOffer(request):
    offer = TakenQuestion.objects.values('taker__username', 'taker').distinct()
    context = {'offer': offer}
    return render(request, 'female/offers.html', context)

def Result(request, pk):
    taker = get_object_or_404(User, pk=pk)
    result = TakenQuestion.objects.filter(question__user=request.user).filter(taker=taker)
    note = InterestData.objects.filter(interester=taker).filter(interestin=request.user).first()
    print(note.status)
    InterestData.objects.update(interester=taker, interestin=request.user, read=True)
    
    context = {'result': result, 'taker': taker, 'note': note}

    return render(request, 'female/result.html', context)

    


def MyAllProposal(request):
    proposal = InterestData.objects.filter(interestin=request.user).order_by('-created_at')
    context = {'proposal': proposal}
    return render(request, 'female/allproposal.html', context)


def MaleDetails(request, pk):
    #details = get_object_or_404(Profile, pk=pk)
    user = get_object_or_404(User, pk=pk)
    taker = TakenQuestion.objects.filter(question__user=user).filter(taker=request.user).first()
    interest = InterestData.objects.filter(interester=request.user).filter(interestin=user).first()
    content = {'user': user, 'taker': taker, 'interest': interest}
    return render(request, 'female/details.html', content)


def AcceptMaleProposal(request, pk):

    taker = get_object_or_404(User, pk=pk)

    

    if request.method == 'POST': 

        acceptance = request.POST.get('acceptance')

        InterestData.objects.filter(interester=taker).filter(interestin=request.user).update(status='L', acceptance=acceptance)
        messages.success(request, 'You Interest has been Sent to her Successully!')
        return redirect('female:dashboard')

    return render(request, 'female/accept.html')


def EjectMaleProposal(request, pk):
    
    taker = get_object_or_404(User, pk=pk)   

    InterestData.objects.filter(interester=taker).filter(interestin=request.user).update(status='R', acceptance='')
    messages.success(request, 'You Interest has been Sent to her Successully!')
    return redirect('female:dashboard')

    return render(request, 'female/accept.html')

    








