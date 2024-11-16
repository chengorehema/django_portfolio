from django.shortcuts import render, redirect
from .models import Project
from .forms import ContactForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def home(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
        else:
            form = ContactForm()
        return render(request, 'contact.html', {'form': form})


def projects(request):
    project_list = Project.objects.all()  # Example: Query all projects
    return render(request, 'projects.html', {'projects': project_list})
