
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
import requests
import json

# Create your views here.


def profile(request):
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
            	userData['updated_at'] = data['updated_at']
            	userData['created_at'] = data['created_at']
            requiredData.append(userData)
        else:
            return render(request, 'errors/generic_error.html')
    return render(request, 'user_profile/profile.html', {'requiredData': requiredData})