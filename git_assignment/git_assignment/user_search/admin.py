

# from django.http import HttpResponse
from django.contrib import admin
from .models import UserProfile
from git_assignment import settings

class UserProfileAdmin(admin.ModelAdmin):
    class Meta:
    	model = UserProfile
    """data_record_created_at - time of data record creation"""
    list_display = ("login_name", "login_id", "url", "email", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at", "email", "data_record_created_at")

admin.site.register(UserProfile, UserProfileAdmin)
