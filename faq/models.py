from django.db import models
from django.core.urlresolvers import reverse

class Faq(models.Model):
    pergunta = models.CharField(max_length = 200)
    resposta = models.CharField(max_length = 200)
    data = models.DateField()

    def __unicode__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse ('faq:editar_faq', kwargs={'pk':self.pk})
