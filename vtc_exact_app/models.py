from django.db import models
from account.models import User
# from courses.models import Course, Category
from adminapp.models import Corporation, District, Municipality, Panchayath
# Create your models here.
class VtcModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=50)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    corporation = models.ForeignKey(Corporation, on_delete=models.SET_NULL, blank=True, null=True)
    municipality = models.ForeignKey(Municipality, on_delete=models.SET_NULL, blank=True, null=True)
    panchayath = models.ForeignKey(Panchayath, on_delete=models.SET_NULL, blank=True, null=True)
    vtc_name = models.CharField(max_length=200, null=True)
    psc = models.BooleanField(default=False)
    ssc = models.BooleanField(default=False)
    upsc = models.BooleanField(default=False)
    bank_exam = models.BooleanField(default=False)

    # category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    # course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    # district = models.OneToOneField(District, on_delete=models.CASCADE, blank=True, null=True)
    # municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.vtc_name}'
class Batch(models.Model):
    batch_no = models.CharField(max_length=200, null=True)
    max_no_of_students = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(VtcModel,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f'{self.batch_no}-{self.user}'