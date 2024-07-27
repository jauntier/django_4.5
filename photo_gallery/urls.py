# photo_gallery/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
]


