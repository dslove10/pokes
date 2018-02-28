# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z_ ]*$')

# Create your models here.
class UserManager(models.Manager):
	def register_validator(self, postData):
		errors = {}
		if len(postData['name']) < 3:
			errors["name"] = 'Name must be at least 2 characters'
		if not NAME_REGEX.match(postData['name']):
			errors["name"] = 'Only letters, underscore, or spaces allowed for name'
		if len(postData['alias']) < 3:
			errors["alias"] = 'Alias must be at least 2 characters'
		if User.objects.filter(alias = postData['alias']).exists():
			errors["alias"] = 'Alias already exists'
		if len(postData['email']) < 1:
			errors["email"] = 'Email cannot be empty'
		if not EMAIL_REGEX.match(postData['email']):
			errors["email"] = 'Must be a valid email'
		if User.objects.filter(email = postData['email']).exists():
			errors["email"] = 'Email already exists'
		if len(postData['password']) < 8:
			errors["password"] = 'Password must be at least 8 characters'
		if postData['password'] != postData['confirm']:
			errors["password"] = 'Passwords do not match'
		return errors

	def login_validator(self, postData):
		user = User.objects.get(email = postData['email'])
		errors = {}
		if len(user.email) != 0:
			if bcrypt.checkpw(postData['password'].encode(), user.password.encode()) == False:
				errors["pass_check"] = 'Invalid Email/Password Combination'
		else:
			errors["alias"] = 'Invalid Email/Password Combination'
		return errors

class User(models.Model):
	name = models.CharField(max_length = 255)
	alias = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	password = models.TextField()
	dob = models.DateField()
	pokes = models.IntegerField(default = 0)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = UserManager()

class Poke(models.Model):
	poked_by = models.ForeignKey(User, related_name = 'poked_me')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)