import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# funtion based view
def home(request):
	num = random.randint(0,50)
	return render(request, "base.html", {"bool_item": False, "num": num})