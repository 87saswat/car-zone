from django.shortcuts import render
from .models import Team

# Create your views here.

def home (request):
    teams = Team.objects.all()
    context = {'teams': teams}
   
   
    return render (request, "about.html", context) 
    




def about(request):
    teams = Team.objects.all()
    context = {'teams': teams,}
    
    return render (request, "about.html", context) 

def services(request):
    context={}
    return render (request, "services.html", context) 

def contact(request):
    context={}
    return render (request, "contact.html", context) 