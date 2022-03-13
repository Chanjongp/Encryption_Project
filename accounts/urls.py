from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('input-sensitive', views.CreateSensitiveInfoAPIView.as_view(), name="input-sensitive"),
]