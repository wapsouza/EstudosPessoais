from django.shortcuts import render
from django.http import request
from django.http import HttpResponse
from .forms import *

def index(request):
    return render(request,'index.html')

def contato (request):
    if request.POST:
        form = ContatoForm(request.POST)
        if form.is_valid():
	            form.envia_email()
    else:
        form = ContatoForm()
    context = {
		"contato.html":form
    }
    return render(request,"contato.html", context)


