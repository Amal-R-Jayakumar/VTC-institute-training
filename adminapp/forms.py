from django.db.models.fields.files import FileField
from account.models import Profile, User
from phonenumber_field.formfields import PhoneNumberField
from account.choices import *
from django import forms
from adminapp.models import Municipality, District, Corporation,Panchayath, VTCListExcel


class AddVTCAdminForm(forms.ModelForm):
    name = forms.CharField(label="Name of VTC Director", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    email = forms.CharField(label="Email", widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))
    contact_number = forms.CharField(label='Phone Number', widget=forms.TextInput(
        attrs={'class': 'form-control rounded-0', 'placeholder': 'Phone Number*'}))

    class Meta:
        fields = ['name', 'email', 'contact_number']
        model = User

# class VTCProfileForm(forms.ModelForm):
    #address = forms.CharField(label='Address*:', widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'floatingDob', 'placeholder': 'Enter Your Home Address*', 'rows': 4}))
    #district= forms.ChoiceField(choices=DISTRICTS, label='Select District:',widget=forms.Select(attrs={'class': 'form-select'}))
    #district= forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-select'}))
    #Municipality= forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-select'}))
    
    #code = forms.CharField(label="VTC Code: ", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Institute Code'}))
    #psc = forms.BooleanField(label="PSC", widget=forms.CheckboxInput(attrs={'class': 'form-check-label'}))
    #ssc = forms.BooleanField(label="SSC", widget=forms.CheckboxInput(attrs={'class': 'form-check-label'}))
    #upsc = forms.BooleanField(label="UPSC", widget=forms.CheckboxInput(attrs={'class': 'form-check-label'}))
    #bank_exam = forms.BooleanField(label="Bank Exam", widget=forms.CheckboxInput(attrs={'class': 'form-check-label'}))
    
    # class Meta:
    #     model = Profile
    #     fields = ['address','district','corporation','municipality','panchayath','code','psc','ssc','upsc','bank_exam','vtc_name']
    # def __init__(self, *args, **kwargs):
    #     super(VTCProfileForm, self).__init__(*args, **kwargs)
    #     self.fields['psc'].required = False
    #     self.fields['ssc'].required = False
    #     self.fields['upsc'].required = False
    #     self.fields['bank_exam'].required = False
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['municipality'].queryset = Municipality.objects.none()

    #     if 'district' in self.data:
    #         try:
    #             district_id = int(self.data.get('district'))
    #             self.fields['municipality'].queryset = Municipality.objects.filter(district_id=district_id).order_by('name')
    #         except (ValueError, TypeError):
    #             #pass  # invalid input from the client; ignore and fallback to empty City queryset
    #             print("no data get")
    #     #elif self.instance.pk:
    #         #self.fields['city'].queryset = self.instance.country.city_set.order_by('name')


class UploadFileForm(forms.Form):
    excel_file = forms.FileField(label="Profile Picture", required=True, widget=forms.FileInput(
        attrs={'class': 'form-control', 'placeholder': 'Upload Your Profile Picture*'}))
    class Meta:
        model = VTCListExcel
        fields = ["excel_file"]
