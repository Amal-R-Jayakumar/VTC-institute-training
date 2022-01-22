from django.contrib import admin
from courses.models import Course, Category,TestQuestion,Enrollment

# Register your models here.
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(TestQuestion)
