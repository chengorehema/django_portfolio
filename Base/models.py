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
    email=models.EmailField(max_length=30)
    subject = models.CharField(max_length=200)
    message=models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text="Enter a value between 1 (beginner) and 100 (expert)")

    def __str__(self):
        return f"{self.name} - {self.proficiency}%"

    