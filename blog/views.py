from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here

def allblogs(request):
	blogs = Post.objects
	return render(request, 'blog/allblogs.html', {'blogs': blogs})

def detail(request, blog_id):
	detail_post = get_object_or_404(Post, pk=blog_id)
	return render(request, 'blog/detail.html', {'post': detail_post})
