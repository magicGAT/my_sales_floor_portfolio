from django.contrib import admin

#imports Job app model to the admin interface for the entire project
from .models import Job

admin.site.register(Job)
