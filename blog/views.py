from django.shortcuts import render, redirect
from django.utils import timezone
from blog.models import Post
from blog.forms import PostForm


# Create your views here.
def post_list(request):
	post = Post.objects.all()
	contexto = {'posts':post}
	return render (request, 'blog/post_list.html',contexto)

def post_detail(request, id_post):
	post = Post.objects.get(id=id_post)
	contexto = {'post':post}
	return render(request, 'blog/post_detail.html', contexto)

def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
		return redirect('blog:post_detalle', id_post=post.id)
	else:
		form = PostForm()
		return render(request,'blog/post_form.html',{'form':form})

def post_edit(request,id_post):
	post = Post.objects.get(id=id_post)
	if request.method == 'GET':
		form = PostForm(instance = post)
	else:
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			form.save()
		return redirect('blog:post_detalle', id_post=post.id)
	return render(request, 'blog/post_form.html',{'form':form})