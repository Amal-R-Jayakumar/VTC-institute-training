from django.contrib.auth import authenticate, get_user_model
from django import forms
from django.conf import settings
from account.models import User, Profile
from courses.models import Category, Course,TestQuestion
from courses.models import Enrollment
from django.db import models
from vtc_exact_app.models import Batch

class add_student_form_user(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
                           "class": "form-control form-control-custom style_2", "type": "text", "placeholder": "Full Name"}))
    contact_number = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control form-control-custom style_2", "type": "text", "placeholder": "Contact Number"}))
    email = forms.CharField(widget=forms.TextInput(attrs={
                            "class": "form-control form-control-custom style_2", "type": "text", "placeholder": "Email Address"}))
    gender = forms.CharField(widget=forms.TextInput(attrs={
                             "class": "form-control form-control-custom style_2", "type": "text", "placeholder": "Gender"}))

    class Meta:
        fields = ['name', 'contact_number', 'email', 'gender']
        model = User


class add_student_form_profile(forms.ModelForm):
    # vtc_code = '123'
    qualification = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control form-control-custom style_2", "type": "text", "placeholder": "Qualification"}))
    # code = forms.CharField(widget=forms.TextInput(attrs={
    #                        "class": "form-control form-control-custom style_2", "type": "text", "placeholder": "Code"}), initial=vtc_code)

    class Meta:
        fields = ['qualification']
        model = Profile


class add_student_form_enroll(forms.ModelForm):
    # mode_of_training =forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control","type":"text","placeholder":"Mode of training"}))

    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Category:',
                                      widget=forms.Select(attrs={'class': 'form-control form-control-custom style_2'}))
    course = forms.ModelChoiceField(queryset=Course.objects.all(), label='Course:',
                                    widget=forms.Select(attrs={'class': 'form-control form-control-custom style_2'}))
    batch = forms.ModelChoiceField(queryset=Batch.objects.all(), label='Batch:', widget=forms.Select(attrs={'class': 'form-control form-control-custom style_2'}))
    class Meta:
        fields = ['category', 'course','batch']
        model = Enrollment


class TestQuestionForm(forms.ModelForm):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), label='Course:', widget=forms.Select(attrs={'class': 'form-control m-2', 'placeholder': 'Question'}))
    question = forms.CharField(label="Question", widget=forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Question'}))
    opt1 = forms.CharField(label="Option1", widget=forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Option1'}))
    opt2 = forms.CharField(label="Option2", widget=forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Option2'}))
    opt3 = forms.CharField(label="Option3", widget=forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Option3'}))
    opt4 = forms.CharField(label="Option4", widget=forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Option4'}))
    correct_ans = forms.CharField(label="Correct answer", widget=forms.TextInput(attrs={'class': 'form-control m-2', 'placeholder': 'Correct Answer'}))
    class Meta:
        fields = ['course', 'question', 'opt1', 'opt2', 'opt3', 'opt4', 'correct_ans']
        model = TestQuestion

