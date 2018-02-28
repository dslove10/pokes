# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.db.models import F
from .models import *
import bcrypt

# Create your views here.
def index(request):
	return render(request, 'users/index.html')

def register(request):
	errors = User.objects.register_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/')
	else:
		hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
		new_user = User.objects.create(name = request.POST['name'], alias = request.POST['alias'], email = request.POST['email'], password = hashed_pw, dob = request.POST['dob'])
		user = User.objects.get(email = request.POST['email'])
		request.session['alias'] = user.alias
		request.session['id'] = user.id
		return redirect('/pokes')

def login(request):
	errors = User.objects.login_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/')
	else:
		user = User.objects.get(email = request.POST['email'])
		request.session['alias'] = user.alias
		request.session['id'] = user.id
		return redirect('/pokes')

def logout(request):
	del request.session['alias']
	del request.session['id']
	return redirect('/')

def pokes(request):
	pokes = {
		'poked': Poke.objects.exclude(poked_by_id = request.session['id']),
		'all_users': User.objects.exclude(id = request.session['id'])
	}

	print Poke.objects.filter(poked_by_id = 1)
	return render(request, 'users/pokes.html', pokes)

def add(request, number):
	poked = Poke.objects.create(poked_by = User.objects.get(id = request.session['id']))
	poker = User.objects.filter(id = number)
	poker.update(pokes = F('pokes') + 1)
	return redirect('/pokes')