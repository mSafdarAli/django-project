from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
def restaurant_listview(request):
	template_name = "restaurants/restaurants_list.html"
	context = {
		"object_list": [12, 14, 445, 45]
	}
	return render(request, template_name, context)