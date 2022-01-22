from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from vtc_exact_app.views import add_batch
from vtc_exact_app.views import show_test_questions, show_questions_by_course

urlpatterns = [
    path('add-batch/', add_batch, name='add_batch'),
    path('view-test-questions/', show_test_questions, name='show_test_questions'),
    path('view-test-questions-course/<int:id>', show_questions_by_course),

]