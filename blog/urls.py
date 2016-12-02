from django.conf.urls import url

from blog.views import post_list, post_detail

urlpatterns=[
	url(r'^listar',post_list, name='post_listar'),
	url(r'^(?P<id_post>[0-9]+)/$',post_detail, name='post_detalle'),
]