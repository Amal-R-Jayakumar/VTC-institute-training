from django.contrib import admin
from django.urls import path, include
from adminapp import views
from adminapp.views import Enrollment_details
from django.contrib.auth import views as auth_views

# app_name="vtc_app"

urlpatterns = [
   
   # path('addvtc/', views.add_new_vtc, name='add_vtcs'),
   path('vtc-list/', views.view_vtcs, name='view_vtcs'),
   path('delete/<int:id>', views.destroy,name="deactivate_account"),  
   path('add-student/', Enrollment_details, name='add_student'),
   path('add-student-demo/', views.add_student_demo),
   path('ajax/load-cities/', views.load_municipalities, name='ajax_load_cities'), # AJAX
   path('vtc-student-list/', views.view_student_vtc, name='vtc_student_list'),
   path('vtc-student-list/<str:code>/', views.view_student_admin, name='vtc_student_list_admin'),
   path('vtc-list-upload/', views.upload, name='vtc_list_upload'),
]