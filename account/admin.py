from django.contrib import admin
from account.models import Enquiryform, User, Profile, LoggedInUser

admin.site.register(Enquiryform)
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(LoggedInUser)
