from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from .models import *


class FemaleSignUpForm(UserCreationForm):
    
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=("Username"), error_messages={ 'invalid': ("This value must contain only letters, numbers and underscores.") })
    first_name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=("Surname"))
    last_name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=("First Name"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=("Password (again)"))
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_lenght=50)), label=("Email Address"))

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in [ 'username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(("The username already exists. Please try another one."))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # check and raise error if other user already exists with given email
        is_exists = User.objects.filter(email=email).exists()
        if is_exists:
            raise forms.ValidationError("User already exists with this email")
        return email
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(("The two password fields did not match."))
        return self.cleaned_data


    term = forms.ModelMultipleChoiceField(widget = forms.CheckboxSelectMultiple, queryset = Term.objects.all())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'who', 'term')

        # widgets = {
        #     #'body': forms.Textarea(),
        #     'term': forms.CheckboxSelectMultiple(),
        #     #'who': forms.ChoiceField()
        #     #year = forms.ChoiceField(choices=[(x,x) for x in range (2016,2021)], initial=date.today().year)

        # }

   


    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_female = True
        if commit:
            user.save()
        return user


class MaleSignUpForm(UserCreationForm):

    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=("Username"), error_messages={ 'invalid': ("This value must contain only letters, numbers and underscores.") })
    first_name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=("Surname"))
    last_name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=("First Name"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=("Password (again)"))
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_lenght=50)), label=("Email Address"))

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in [ 'username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(("The username already exists. Please try another one."))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # check and raise error if other user already exists with given email
        is_exists = User.objects.filter(email=email).exists()
        if is_exists:
            raise forms.ValidationError("User already exists with this email")
        return email
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(("The two password fields did not match."))
        return self.cleaned_data


    term = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Term.objects.all(), required=True)
   

    """ term = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={
            'btn_class': 'btn btn-link dccn-link dccn-text-small',
            'label_class': 'dccn-text-0',
        }), required=True) """

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'who', 'term')

        # widgets = {
        #     #'body': forms.Textarea(),
        #     'term': forms.CheckboxSelectMultiple(),
        #     #'who': forms.ChoiceField()
        #     #year = forms.ChoiceField(choices=[(x,x) for x in range (2016,2021)], initial=date.today().year)

        # }

   
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_male = True
        if commit:
            user.save()
        return user




""" class MaleSignUpForm(UserCreationForm):
    interests = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.interests.add(*self.cleaned_data.get('interests'))
        return user """

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ('plan',)

