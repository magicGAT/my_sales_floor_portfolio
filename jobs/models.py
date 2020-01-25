from django.db import models

# database class for project database 
class Job(models.Model):
	image = models.ImageField(upload_to='images/')
	summary = models.CharField(max_length=300)

	def __str__(self):
		return self.summary