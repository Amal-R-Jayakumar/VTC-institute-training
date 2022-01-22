from django.urls import path
from . import views
from account.views import home_view

urlpatterns = [
    path('affiliation/', views.Affiliation_first_form,name='affiliation'),
    path('affiliation-request-list/', views.view_new_affiliation, name='affiliation_request_list'),
    path('affiliation-request-response/<int:id>', views.accepting_vtc_first),
    path('secondform/', views.affiliation_second),
    #path('affiliation-request-list/<int:id>', views.output, name='script'),
    #path('requestform/', views.Affiliation_first_form, name='requestform'),
    path('affiliation_secondform/', views.affiliation_second, name='affiliation_secondform'),
    

]
