from django.db import models
import pytz
from django.core.validators import URLValidator

class UserProfile(models.Model):
    user_name = models.CharField(max_length=30, null=True, blank=True, default="None")
    login_name = models.CharField(max_length=30, primary_key=True)
    login_id = models.IntegerField(default=0)
    email = models.EmailField(max_length=254, null=True, blank=True, default="None") 
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    bio = models.CharField(max_length=30, null=True, blank=True, default="None")
    url = models.TextField(validators=[URLValidator()], default='')
    public_repos = models.IntegerField(default=0)
    #avatar = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')

            	
            	
            	
            	
               
            	
