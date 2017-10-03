
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
import requests
import json
from rest_framework import serializers, viewsets
from .models import UserProfile
from rest_framework.decorators import api_view
# Create your views here.

class UserSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = UserProfile



def profile(request):
    """ get user profile data for the user name entered in the form using https://api.github.com/users/ API 
    returns user data if serach successfull else a error page"""

    dataList = []
    requiredData = []
    userData = {}
    if request.method == 'POST':
        name = request.POST.get('user')
        req = requests.get('https://api.github.com/users/'+ name)
        if req.status_code ==200:
            dataList.append(json.loads(req.content))
            
            for data in dataList:
            	userData['login_id'] = data['id']
            	userData['user_name'] = data['name']
            	userData['login_name'] = data['login']
            	userData['email'] = data['email']
            	userData['bio'] = data['bio']
                #userData['avatar'] = data['avatar']
                userData['url'] = data['html_url']
                userData['public_repos'] = data['public_repos']
            	userData['updated_at'] = data['updated_at']
            	userData['created_at'] = data['created_at']
                UserProfile.objects.get_or_create(user_name= userData['user_name'],
                        login_name=userData['login_name'],
                        login_id=userData['login_id'],
                        email=userData['email'],
                        bio=userData['bio'],
                        url=userData['url'],
                        public_repos=userData['public_repos'],
                        created_at=userData['updated_at'],
                        updated_at=userData['updated_at'])
            requiredData.append(userData)
        else:
            return render(request, 'errors/generic_error.html')
        
    return render(request, 'user_profile/profile.html', {'requiredData': requiredData})

