
from django.shortcuts import render, HttpResponse
import requests
import json

# Create your views here.


def profile(request):
    dataList = []
    requiredData = []
    userData = {}
    req = requests.get('https://api.github.com/users/mansa-maravanthe')
    dataList.append(json.loads(req.content))
   
    for data in dataList:
    	userData['login_id'] = data['id']
    	userData['user_name'] = data['name']
    	userData['login_name'] = data['login']
    	userData['email'] = data['email']
    	userData['bio'] = data['bio']
    	userData['updated_at'] = data['updated_at']
    	userData['created_at'] = data['created_at']
    requiredData.append(userData)
    return render(request, 'user_profile/profile.html', {'requiredData': requiredData})