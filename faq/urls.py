from django.conf.urls import patterns, include, url

from faq import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.ListarFaq.as_view(), name='listar_faq'),
    url(r'^novo$', views.CriarFaq.as_view(), name='criar_faq'),
    url(r'^editar/(?P<pk>\d+)$', views.AlterarFaq.as_view(), name='editar_faq'),
    url(r'^deletar/(?P<pk>\d+)$', views.DeletarFaq.as_view(), name='deletar_faq'),
)
