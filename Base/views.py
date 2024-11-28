from django.shortcuts import render, redirect
from .models import Project
from .forms import ContactForm
import logging

logger = logging.getLogger(__name__)

# Index view
def index(request):
    return render(request, 'base.html')

# Projects view
def projects(request):
    project_list = Project.objects.all()  # Query all projects from the database
    return render(request, 'projects.html', {'projects': project_list})

# Resume view
def resume(request):
    return render(request, 'resume.html')

# Services view
def services(request):
    return render(request, 'services.html')

# Contact view
def contact(request):
    logger.info("Contact view accessed")  # Logging for debugging
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data
            return redirect('contact')  # Redirect to the same contact page (or another page if desired)
    else:
        form = ContactForm()  # Initialize an empty form
    return render(request, 'contact.html', {'form': form})

# Home view (if needed)
def home(request):
    return render(request, 'base.html')


