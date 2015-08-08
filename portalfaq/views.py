from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

def home(request):
	html = """
	<h1>Faq Portal de Ideias</h1>
	<a href="/faq/">Faq</a><br>
	"""

	return HttpResponse(html)