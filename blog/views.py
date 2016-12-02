from django.shortcuts import render
from blog.models import Post

# Create your views here.
def post_list(request):
	post = Post.objects.all()
	contexto = {'posts':post}
	return render (request, 'blog/post_list.html',contexto)

def post_detail(request, id_post):
	post = Post.objects.get(id=id_post)
	contexto = {'post':post}
	return render(request, 'blog/post_detail.html', contexto)

