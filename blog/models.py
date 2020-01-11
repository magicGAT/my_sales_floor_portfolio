from django.db import models

#Blog post class for project database 
class Post(models.Model):
	image = models.ImageField(upload_to="images/")
	title = models.CharField(max_length=100)
	date = models.DateField(null=True)
	content = models.TextField()
	sources = models.CharField(max_length=500)
