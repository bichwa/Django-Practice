from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
	url(r'^$', views.post_list),
	# post/ means that after the beginning, the URL should contain the word post and /.
	# (?P<pk>[0-9]+) means django will take everything that you 
	# place here and transfer it to a view as a variable pk.[0-9] and that it should 
	# be only a number.
	# Then we need / 
	# $ is the end of the url
	  
	url(r'post/(?P<pk>[0-9]+)/$', views.post_detail),
	url(r'post/new/$', views.post_new, name = 'post_new')
	)