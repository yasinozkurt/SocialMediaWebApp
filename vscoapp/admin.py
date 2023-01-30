from django.contrib import admin
from .models import SearchedUser
from django.http import HttpRequest
from django.db.models.query import QuerySet


class UserProfile(admin.ModelAdmin):
    list_display=['userId', 'username', 'searched']

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        return super(UserProfile, self).get_queryset(request).order_by('-searched')


admin.site.register(SearchedUser, UserProfile)
