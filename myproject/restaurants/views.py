import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# funtion based view
def home(request):
	num = random.randint(0,50)
	return render(request, "home.html", {"bool_item": True, "num": num})
def contact(request):
	return render(request, "contact.html")
def about(request):
	return render(request, "about.html")		