from django.db import models


class UserProfile(models.Model):
    user_name = models.CharField(max_length=30)
    login_name = models.CharField(max_length=30, unique=True)
    login_id = models.IntegerField()
    email = models.EmailField(max_length=254, null=True) 