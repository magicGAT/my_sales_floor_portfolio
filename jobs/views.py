from django.shortcuts import render

# Job model import statement to pull data from the project database
from .models import Job

def home(request):
	jobs = Job.objects
	return render(request, 'jobs/home.html', {'jobs':jobs})
