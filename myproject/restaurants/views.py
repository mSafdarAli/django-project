import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
# funtion based view		
class HomeView(TemplateView): #inherits from template_view class imported
	template_name = "home.html"