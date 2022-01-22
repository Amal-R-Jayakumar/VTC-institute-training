from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from courses import views


urlpatterns = [
    path('course_view/', views.view_all_courses, name='view_courses'),
    path('enrollment_view/', views.Enrollment_details, name='enrollment_details'),
    path('test-question/', views.test_question, name='test_question'),
    ]