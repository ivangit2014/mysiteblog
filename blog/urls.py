from django.conf.urls import url

from blog.views import post_list, post_detail, post_new, post_edit

urlpatterns=[
	url(r'^listar',post_list, name='post_listar'),
	url(r'^(?P<id_post>[0-9]+)/$',post_detail, name='post_detalle'),
	url(r'^new',post_new, name='post_crear'),
	url(r'^edit/(?P<id_post>[0-9]+)/$',post_edit, name='post_editar'),
]