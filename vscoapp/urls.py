from django.urls import path
from . import views


# path("", views.index, name="index"),
urlpatterns = [
    path('vsco-profil-resmi-buyutme', views.vscomain, name="vscomain"),
    path('vsco-profile-picture-zoom', views.vscomainen, name="vscomainen"),
    path('getpic/',views.send_pic,name="getpic"),
]