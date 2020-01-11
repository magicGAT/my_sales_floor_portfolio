from django.contrib import admin

#import Post model for use within the project admin interface
from .models import Post 

admin.site.register(Post)
