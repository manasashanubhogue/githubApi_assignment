# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase, RequestFactory
import datetime
from django.utils import timezone
from .views import profile
from .models import UserProfile



class TestUserSearch(TestCase):

	def setUp(self):
        # Every test needs access to the request factory.
    	self.factory = RequestFactory()
        # self.user = UserProfile.objects.create(
	       #      			user_name= "None",
	       #                  login_name="test",
	       #                  login_id=383316,
	       #                  email="None",
	       #                  bio="None",
	       #                  url="https://github.com/test",
	       #                  public_repos=2,
	       #                  created_at=timezone.now().date(),
	       #                  updated_at=timezone.now().date() + datetime.timedelta(days=20)
	       #  )

	def test_search_user(self):
		self.factory = RequestFactory()
		request = self.factory.post('/profile/')
		print profile(request)
		# response = profile(request)
		# print response
		
		# self.assertEqual()


