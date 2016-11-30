from django.shortcuts import render
from blog.models import Post

# Create your views here.
def post_list(request):
	post = Post.objects.all()
	contexto = {'post':post}
	return render (request, 'blog/post_list.html',contexto)