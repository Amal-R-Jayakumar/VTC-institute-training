from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.conf import settings
from account.models import User, Profile
from django.db import models


class UserSignUpForm(UserCreationForm):
    name =forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","type":"text","placeholder":"Name"}))
    contact_number =forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","type":"text","placeholder":"Contact Number"}))
    email =forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","type":"email","placeholder":"Email"}))
    gender =forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","type":"text","placeholder":"Gender"}))
    password1 =forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","type":"password","placeholder":"Password"}))
    password2 =forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","type":"password","placeholder":"Confirm Password"}))
    class Meta:
        fields = ('name', 'contact_number', 'email','gender',
                  'password1', 'password2')
        model = User

class SignupProfileForm(forms.ModelForm):
    dob = forms.DateField(label='Date of Birth*', widget=forms.DateInput(format='%d/%m/%Y',attrs={'class': 'form-control','type':'date', 'placeholder': 'Date of Birth', 'id': 'inputDate'}), input_formats=settings.DATE_INPUT_FORMATS)
    address = forms.CharField(label='Address*:', widget=forms.Textarea(
        attrs={'class': 'form-control', 'id': 'floatingDob', 'placeholder': 'Enter Your Home Address*', 'rows': 4}))
    qualification = forms.CharField(label='Course Currently Pursued*:', widget=forms.TextInput(
        attrs={'class': 'form-control', 'id':"floatingQualification", 'placeholder': 'Enter your Qualification*'}))
    class Meta:
        fields = ['dob', 'address', 'qualification']
        model = Profile

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","type":"text","placeholder":"Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","type":"password","placeholder":"Password"}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError('Incorrect Email or Password')

            if not user.check_password(password):
                raise forms.ValidationError('Incorrect Email or Password')

        return super(UserLoginForm, self).clean(*args, **kwargs)

class ProfileUpdateForm(forms.ModelForm):
    dob = forms.DateField(label='Date of Birth*', widget=forms.DateInput(format='%d/%m/%Y',
        attrs={'class': 'form-control', 'placeholder': 'DD-MM-YYYY','id':'inputDate'}),input_formats=settings.DATE_INPUT_FORMATS)
    address = forms.CharField(label='Address*:', widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Home Address*', 'rows': 3}))
    qualification = forms.CharField(label='Course Currently Pursued*:', widget=forms.TextInput(
        attrs={'class': 'form-control', 'id':"floatingQualification", 'placeholder': 'Enter your Qualification*'}))
    #profile_pic = forms.ImageField(label="Profile Picture", required=True, widget=forms.FileInput(
        #attrs={'class': 'form-control', 'placeholder': 'Upload Your Profile Picture*'}))
    class Meta:
        model = Profile
        fields = ['dob', 'address', 'qualification']
    
class UserUpdateForm(forms.ModelForm):
    name =forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","type":"text","placeholder":"Name",'readonly':'readonly'}))
    contact_number =forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","type":"text","placeholder":"Contact Number",'readonly':'readonly'}))
    email =forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","type":"email","placeholder":"Email",'readonly':'readonly'}))
    gender =forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","type":"text","placeholder":"Gender"}))
    class Meta:
        fields = ('name', 'contact_number', 'email','gender',)
        model = User