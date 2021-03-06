from django.shortcuts import render

# Job model import statement to pull data from the project database
from .models import Job

def home(request):
	jobs = Job.objects
	return render(request, 'jobs/home.html', {'jobs':jobs})

def about(request):
	return render(request, 'jobs/aboutme.html')

def social_media(request):
	return render(request, 'jobs/social_media.html')
