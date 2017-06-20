# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):
    '''Render the index home page with no ninjas'''
    return render(request, 'ninjas/index.html')
def ninjas(request):
    '''Render the nindas page, with buttons to select a ninja'''
    return render(request, 'ninjas/ninjas.html')
def show(request, color):
    '''Render the ninjas page'''
    if color == "blue":
        context = {"tmnt": "Leonardo.jpg"}
        return render(request, 'ninjas/show.html', context)
    elif color == "orange":
        context = {"tmnt": "Michelangelo.jpg"}
        return render(request, 'ninjas/show.html', context)
    elif color == "purple":
        context = {"tmnt": "Donatello.jpg"}
        return render(request, 'ninjas/show.html', context)
    elif color == "red":
        context = {"tmnt": "Raphael.jpg"}
        return render(request, 'ninjas/show.html', context)
    else:
        return render(request, 'ninjas/invalid.html')
def invalid(request):
    return render(request, 'ninjas/invalid.html')
    