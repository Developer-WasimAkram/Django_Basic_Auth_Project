from django.contrib import admin
from django.urls import path
from .views import form_view
urlpatterns = [
    path("register/", form_view,name="register"),]