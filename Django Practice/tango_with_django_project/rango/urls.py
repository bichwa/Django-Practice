# The contents of this file will allow you to map URLs for your application
#(www.tangowithdjango.com/rango/) to specific views


 

from django.conf.urls import patterns, url
from rango import views

# The urlpatterns  tuple contains a series of calls to 
# the django.conf.urls.url() function 
urlpatterns = patterns('',
	url(r'^$', views.index, name = 'index'),
	url(r'^about/', views.about, name = 'about'),
	url(r'^category/(?P<category_name_url>\w+)/$', views.category, name = 'category'),)
