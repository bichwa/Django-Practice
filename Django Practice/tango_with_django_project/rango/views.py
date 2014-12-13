from rango.models import Category
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse # We import HttpResponse Object from django.http module
from rango.models import Page
from django.template import Context, loader
#Each view exists  within views.py as a series of individual functions hence index view.# Each view takes in atleast one arguement. Convention dictates that this is named request

def index(request):
	context = RequestContext(request)

	# Query the database for a  list of ALL categories
	#Order by category number likes in descending order.
	# Retreive the top 5 only - or all if less than 5
	# Place the list in our context_dic dictionary  which will be passed.
	#RequestClass is used to gain access to settings related to the user's request
	# The context contains information such as the client's machine detail


	category_list = Category.objects.order_by('-likes')[:5]
	context_dict = {'categories': category_list}

	#We can then create a dictionary to store any data we want  to sen through to the template
	#dictionary to pass to the template engine as its context
	#context_dict = {'boldmessage': "I am bold font from the context"}
    #render_to_response is a helper function. We pass as parameters the template we wish to use, the dictionary with
    # our template variables and the context we obtained from the user's request

	for category in category_list:
		category.url = category.name.replace('', '_')
		return render_to_response('rango/index.html', context_dict, context)

# Each view must return a HttpResponse object
	#return HttpResponse("Rango says: hello world! <a href='/rango/about'>About</a>")


def about(request):

	context = RequestContext(request)


	context_dict = {'itallicmessage': "I am itallic font from the context"}

	return render_to_response('rango/about.html', context_dict, context)


def category(request, category_name_url):
	context = RequestContext(request)


	category_name = category_name_url.replace('_', ' ')


	context_dict = {'category_name': category_name}

	try:

		category = Category.objects.get(name = category_name)


		pages = Page.objects.filter(category= category)


		context_dict['pages'] = pages

		context_dict['category'] = category
	except Category.DoesNotExist:

		pass

	return render_to_response('rango/category.html', context_dict, context)

def contact(request):
	pages_present = Page.objects.all()
	t = loader.get_template('rango/page.html')
	c = Context({'pages_present': pages_present})
	return HttpResponse(t.render(c))

	