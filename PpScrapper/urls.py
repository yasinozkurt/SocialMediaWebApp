from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('instagram-profil-fotografi-buyutme', views.index, name="index"),
    path('instagram-profile-picture-zoom',views.indexen,name="index-english"),
    path('getpic/',views.resmi_Gonder,name='resim'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


