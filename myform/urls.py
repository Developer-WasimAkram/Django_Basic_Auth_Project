from django.contrib import admin
from django.urls import path
from .views import form_view, card
urlpatterns = [
    path("register/", form_view,name="register"),
    path("card/", card,name="card"),
    
    ]