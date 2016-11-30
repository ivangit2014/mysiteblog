from django.conf.urls import url

from blog.views import post_list

urlpatterns=[
	url(r'^listar',post_list, name='post_listar'),
]