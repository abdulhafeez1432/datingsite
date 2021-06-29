from  django import  forms
from  django.forms import ModelForm
from  django.contrib.auth.forms import  UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField, PasswordResetForm
from .models import *
from django.db import transaction
from django.forms.utils import ValidationError
import re
from django.core.files.images import get_image_dimensions
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from django.forms.widgets import CheckboxSelectMultiple 
from django.forms import ModelMultipleChoiceField
from django.forms import modelformset_factory, formset_factory




INTEGER_CHOICES= [tuple([x,x]) for x in range(0,20)]

#rating = forms.IntegerField(label="Rate The Job", widget=forms.Select(choices=INTEGER_CHOICES))



class ProfileForm(forms.ModelForm):

    def clean_passport(self):
        image = self.cleaned_data.get("image")
        if not image:
            raise forms.ValidationError("No image!")
        else:
            w, h = get_image_dimensions(image)
            if w > 200:
                raise forms.ValidationError("The image is %i pixel wide. It's supposed to be 300px" % w)
            if h > 200:
                raise forms.ValidationError("The image is %i pixel high. It's supposed to be 300px" % h)
        return image


    class Meta:
        model = Profile
        exclude = ('user', 'available')

        widgets = {'dob': forms.DateInput(format=('%d-%m-%Y'), attrs={'firstDay': 1, 'pattern=': '\d{4}-\d{2}-\d{2}', 'lang': 'pl', 'format': 'yyyy-mm-dd', 'type': 'date'}), }



class FamilyForm(forms.ModelForm):

    sister = forms.IntegerField(label="Number of Sisters", widget=forms.Select(choices=INTEGER_CHOICES))
    brother = forms.IntegerField(label="Number of Brothers", widget=forms.Select(choices=INTEGER_CHOICES))

    class Meta:
        model = Family
        exclude = ('user',)

        #widgets = {'dob': forms.DateInput(format=('%d-%m-%Y'), attrs={'firstDay': 1, 'pattern=': '\d{4}-\d{2}-\d{2}', 'lang': 'pl', 'format': 'yyyy-mm-dd', 'type': 'date'}), }


class EducationForm(forms.ModelForm):

    

    class Meta:
        model = Education
        exclude = ('user',)



class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        exclude = ('user',)

class CharacterForm(forms.ModelForm):

    class Meta:
        model = Character
        exclude = ('user',)




class AboutMeForm(forms.ModelForm):

    class Meta:
        model = AboutMe
        exclude = ('user',)


class ReligionForm(forms.ModelForm):

    class Meta:
        model = Religion
        exclude = ('user',)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('text',  )


class ExamForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('text',)


class BaseAnswerInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()

        has_one_correct_answer = False
        for form in self.forms:
            if not form.cleaned_data.get('DELETE', False):
                if form.cleaned_data.get('is_correct', False):
                    has_one_correct_answer = True
                    break
        if not has_one_correct_answer:
            raise ValidationError('Mark at least one answer as correct.', code='no_correct_answer')

'''
class TakeQuizForm(forms.ModelForm):
    answer = forms.ModelChoiceField(
        queryset=Answer.objects.none(),
        widget=forms.RadioSelect(),
        required=True,
        empty_label=None)

    class Meta:
        model = StudentAnswer
        fields = ('answer', )

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        super().__init__(*args, **kwargs)
        self.fields['answer'].queryset = question.answers.order_by('text')

'''


class ShowInterestForm(forms.ModelForm):
    class Meta:
        model = InterestData
        exclude = ('interestin', 'interester', 'status', 'read', 'acceptance' )