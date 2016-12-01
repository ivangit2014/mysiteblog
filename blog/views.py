from django.shortcuts import render
from blog.models import Post

# Create your views here.
def post_list(request):
	post = Post.objects.all()
	contexto = {'posts':post}
	return render (request, 'blog/post_list.html',contexto)