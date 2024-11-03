from django.shortcuts import render
from django.http import HttpResponse
#If you just want to return plain text
def home(request):
    return HttpResponse("Welcome to Sankyana!")

# Create your views here.
##If you want to render an HTML template
def home (request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def skills(request):
    return render(request, 'skills.html')

def project(request):
    return render(request, 'project.html')

def contact(request):
    return render(request, 'contact.html')