from django.db import models

# Create your models here.

class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    technologies=models.CharField(max_length=200)
    github_link = models.URLField(max_length=300)
    live_link = models.URLField(max_length=300, blank=True)

    def __str__(self):
        return self.title
    

class ContactSubmission(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField()
    message=models.CharField()
    phone_number=models.CharField(max_length=20)

    def __str__(self):
        return f"Message from {self.name}"


    