from django import forms
from django.forms import TextInput, EmailInput, NumberInput, ChoiceField
from django.forms.widgets import Select
from affiliation.models import Affiliation_request, Affiliation_inspection
from adminapp.models import District

class affiliation_request_form(forms.ModelForm):
    owner_name = forms.CharField(label="Name",  widget=forms.TextInput(
        attrs={'class': 'form-control form-control-custom style_2', 'placeholder': 'Full Name'}))
    email = forms.CharField(label="Email", widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-custom style_2', 'placeholder': 'Email'}))
    contact_number = forms.CharField(label='Phone Number', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-custom style_2', 'placeholder': 'Phone Number*'}))
    location = forms.CharField(label="Location",  widget=forms.TextInput(
        attrs={'class': 'form-control form-control-custom style_2', 'placeholder': 'Center Location'}))
    localbodytype = forms.CharField(label="Localbody Type",  widget=forms.TextInput(
        attrs={'class': 'form-control form-control-custom style_2', 'placeholder': 'Localbody Type'}))
    localbodyname = forms.CharField(label="Localbody Name",  widget=forms.TextInput(
        attrs={'class': 'form-control form-control-custom style_2', 'placeholder': 'Localbody Name'}))
    district = forms.CharField(label="District",  widget=forms.TextInput(
        attrs={'class': 'form-control form-control-custom style_2', 'placeholder': 'District'}))
    pincode = forms.CharField(label="Pincode",  widget=forms.TextInput(
        attrs={'class': 'form-control form-control-custom style_2', 'placeholder': 'Pincode'}))
    class Meta:
        model = Affiliation_request
        fields = ['owner_name','email','contact_number','location','localbodytype','localbodyname']

    widgets = {
        'owner_name': TextInput(attrs={"class":"form-control form-control-custom style_2","type":"text","placeholder":"Applicant Name"}),
        'email': EmailInput(attrs={"class":"form-control form-control-custom style_2","type":"email","placeholder":"Email Address"}),
        'contact_number': NumberInput(attrs={"class":"form-control form-control-custom style_2","type":"tel","placeholder":"Phone Number"}),
        'location': TextInput(attrs={"class":"form-control form-control-custom style_2","type":"text","placeholder":"Center Location"}),
        'localbodytype': TextInput(attrs={"class":"form-control form-control-custom style_2","type":"text","placeholder":"Localbody Type"}),
        'district': TextInput(attrs={"class":"form-control form-control-custom style_2","type":"text","placeholder":"District"}),
        'pincode': TextInput(attrs={"class":"form-control form-control-custom style_2","type":"text","placeholder":"Pincode"}),
            # 'place': TextInput(attrs={"class":"form-control form-control-custom style_2","type":"text","placeholder":"Center Location"}),
            # 'district': Select(attrs={"class":"form-control form-control-custom style_2","type":"text","placeholder":"District"}),
            # 'localbodytype': TextInput(attrs={"class":"form-control form-control-custom style_2","type":"text","placeholder":"Localbody Type"}),
            # 'localbodyname': TextInput(attrs={"class":"form-control form-control-custom style_2","type":"text","placeholder":"Localbody Name"}),
            # 'pincode': TextInput(attrs={"class":"form-control form-control-custom style_2","type":"text","placeholder":"Pincode"}),
            }


class affiliation_inspection_form(forms.ModelForm):
    name = forms.CharField(label="Name",  widget=forms.TextInput(
        attrs={'class': 'form-control form-control-custom style_2', 'placeholder': 'Full Name'}))
    institution_name = forms.CharField(label="Name of institutions",  widget=forms.TextInput(
        attrs={'class': 'form-control form-control-custom style_2', 'placeholder': 'Name of institutions'}))  
    institution_address = forms.CharField(label="Name of institutions",  widget=forms.TextInput(
        attrs={'class': 'form-control form-control-custom style_2', 'placeholder': 'Name of institutions'}))  

    class Meta:
        model = Affiliation_inspection
        fields = ['name','institution_name','institution_address']    