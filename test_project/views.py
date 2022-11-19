import json

from django.shortcuts import render
from django.contrib.auth import login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from django.db import IntegrityError

 

 
 
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "aboutus.html")

def jobs(request):
    return render(request, "jobs.html")     
    
def magazine(request):
    return render(request, "magazine.html")

def contact(request):
    return render(request, "contactus.html")
