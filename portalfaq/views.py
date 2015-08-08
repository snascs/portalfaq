from django.shortcuts import render, redirect, get_objetc_or_404
from django.http import HttpResponse

def home(request):
	html = """
	<h1>Faq Portal de Idéias</h1>
	<a href="/faq/">Faq</a><br>
	"""

	return HttpResponse(html)