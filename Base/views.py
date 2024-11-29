
from django.http import JsonResponse
from django.shortcuts import render
from .models import Project
from .forms import ContactForm


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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            # Return a JSON response if it's an AJAX request
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Your message has been sent successfully!'})
        else:
            # Return error response for invalid form if it's AJAX
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'message': 'Form is invalid. Please try again.'})

    # Handle GET request by rendering the contact form
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def home(request):
    return render(request, 'base.html')


