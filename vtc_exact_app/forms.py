from django import forms
from vtc_exact_app.models import VtcModel, Batch

class VTCProfileForm(forms.ModelForm):
    class Meta:
        model = VtcModel
        fields = ['district','corporation','municipality','panchayath','code','psc','ssc','upsc','bank_exam','vtc_name']
    def __init__(self, *args, **kwargs):
        super(VTCProfileForm, self).__init__(*args, **kwargs)
        self.fields['psc'].required = False
        self.fields['ssc'].required = False
        self.fields['upsc'].required = False
        self.fields['bank_exam'].required = False
class BatchForm(forms.ModelForm):
    batch_no = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "type": "text", "placeholder": "Batch Number"}))
    max_no_of_students = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "type": "text", "placeholder": "Maximum Number of Students"}))
    class Meta:
        model = Batch
        fields = ['batch_no','max_no_of_students']
