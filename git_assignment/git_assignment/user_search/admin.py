

# from django.http import HttpResponse
from django.contrib import admin
from .models import UserProfile
from git_assignment import settings

class UserProfileAdmin(admin.ModelAdmin):
    class Meta:
    	model = UserProfile

admin.site.register(UserProfile, UserProfileAdmin)
