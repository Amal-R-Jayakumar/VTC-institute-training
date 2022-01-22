from django.contrib import admin
from django.urls import path, include, reverse_lazy
from account import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.home_view, name='home'),
   path('signup/', views.signup, name='signup'),
   path('login/', views.login_view, name='login'),
   path('view_profile/', views.view_profile, name='view_profile'),
   path('vtc/', views.vtc, name='vtc'),
  
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   path('about_rutronix/', views.about_rutronix, name='about_rutronix'),
   path('about_vijayaveedhi/', views.about_vijayaveedhi, name='about_vijayaveedhi'),
   path('contact/', views.contact, name='contact'),
   #password reset views starts here
   # path('profile/change-password/done/',auth_views.PasswordChangeDoneView.as_view(template_name='accounts/change_password_done.html'), name='password_change_done'),
   # path('profile/change-password/', auth_views.PasswordChangeView.as_view(template_name='accounts/change_password.html',success_url=reverse_lazy('accounts:password_change_done')), name='change_password'),
    # Password reset views
   path('edit-profile/', views.edit_profile, name='edit_profile'),
   path('reset-password/', auth_views.PasswordResetView.as_view(template_name="password-reset.html",success_url = reverse_lazy('password_reset_done'),email_template_name = 'password_reset_email.html'), name ="reset_password"),
   path('reset-password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name ="password_reset_done"),
   path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html",success_url = reverse_lazy('veedhiapp:password_reset_complete')), name="password_reset_confirm"),
   path('reset-password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name ="password_reset_complete"),
   



]
