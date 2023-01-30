from django.urls import path
from . import views

urlpatterns = [
    path('', views.hometr, name="hometr"),
    path('en/',views.homeen,name="homeenglish"),
    path('vsco-profil-buyutucu/',views.redd,name='redirect'),]