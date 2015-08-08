from django.db import models
from django.core.urlresolvers import reverse

class Faq(models.Model):
	pergunta = models.CharField('Pergunta', max_length=200)
    resposta = models.CharField('Resposta', max_length=200)
    data = DateField('Data') 

    def __unicode__(self):
    	return self.nome

    def get_absolute_url(self):
    	return reverse ('faq:editar_faq', kwargs('pk':self.pk))
