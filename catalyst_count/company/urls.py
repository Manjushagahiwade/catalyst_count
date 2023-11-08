
from django.contrib import admin
from django.urls import path

from company.views import upload_excel, success,search

urlpatterns = [
    path('upload_excel/', upload_excel, name='upload_excel'),
    path('success/', success, name='success'),
    path('search/', search, name='search'),
]