from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^create$', views.register),
	url(r'^login$', views.login),
	url(r'^logout$', views.logout),
	url(r'^pokes$', views.pokes),
	url(r'^pokes/add/(?P<number>\d+)$', views.add)
]