from django.db import models


class SearchedUser(models.Model):
    userId = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30)
    searched = models.IntegerField(default=1)
