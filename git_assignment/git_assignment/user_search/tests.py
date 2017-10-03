# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from .views import profile
from .models import UserProfile

class TestUserSearch(TestCase):

	def test_update_user(self):
		self.user1 = UserProfile.objects.create(
	            			user_name= "Test",
	                        login_name="test1",
	                        login_id=123,
	                        email="None",
	                        bio="None",
	                        url="https://github.com/test",
	                        public_repos=2,
	                        created_at=timezone.now().date(),
	                        updated_at=timezone.now().date() + datetime.timedelta(days=20)
	        )
		print profile("test")


