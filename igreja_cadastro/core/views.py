# Create your views here.
# coding: utf-8

from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')