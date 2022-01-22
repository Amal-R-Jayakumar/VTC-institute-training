from django.db import models
from django.contrib.auth.models import AbstractUser
from account.choices import *
# from adminapp.models import District, Municipality, Corporation, Panchayath
from django.conf import settings
# from courses.models import Course, Category


class Enquiryform(models.Model):
    fname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone_code = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=17)
    course_interested = models.CharField(max_length=100)
    place_of_study = models.CharField(max_length=100)

    def register(self):
        self.save()


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Student'), (2, 'VTC'), (3, 'Rutronix'), (4, 'Groware')
    )
    name = models.CharField(max_length=255)
    # phone_regex = RegexValidator(regex=r'^(\+91[\-\s]?)?[0]?(91)?[6789]\d{9}$', message="Phone number entered incorrectly.")
    contact_number = models.CharField(max_length=17, blank=True)  # validators=[phone_regex]
    gender = models.CharField(max_length=30)
    user_type = models.PositiveIntegerField(choices=USER_TYPE_CHOICES, default=1)

    def __str__(self):
        return f'{self.id}  -  {self.username}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=400)
    qualification = models.CharField(max_length=300)
    dob = models.DateField(null=True)
    profile_pic = models.ImageField(default='images/default.png', upload_to='images/profile_pics')

    # code = models.CharField(max_length=50)
    #
    #
    # district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    # corporation = models.ForeignKey(Corporation, on_delete=models.SET_NULL, blank=True, null=True)
    # municipality = models.ForeignKey(Municipality, on_delete=models.SET_NULL, blank=True, null=True)
    # panchayath = models.ForeignKey(Panchayath, on_delete=models.SET_NULL, blank=True, null=True)
    # vtc_name =  models.CharField(max_length=200,null=True)
    #
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True )
    # course = models.ForeignKey(
    #     Course, on_delete=models.CASCADE, blank=True, null=True)
    # #district = models.OneToOneField(District, on_delete=models.CASCADE, blank=True, null=True)
    # #municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, blank=True, null=True)
    #
    # psc = models.BooleanField(default=False)
    # ssc = models.BooleanField(default=False)
    # upsc = models.BooleanField(default=False)
    # bank_exam = models.BooleanField(default=False)
    #
    def __str__(self):
        return f'{self.user.username}\'s Profile'


class LoggedInUser(models.Model):
    user = models.OneToOneField(User, related_name='logged_in_user', on_delete=models.CASCADE)
    session_key = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.user.username
