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
def blue(request):
    '''render the blue ninja, Leonardo'''
    return render(request, 'ninjas/blue.html')
def orange(request):
    '''render the orange ninja, Machelangelo'''
    return render(request, 'ninjas/orange.html')
def red(request):
    '''render the red ninja, Raphael'''
    return render(request, 'ninjas/red.html')
def purple(request):
    '''render the purple ninja, Donatello'''
    return render(request, 'ninjas/purple.html')
def invalid(request):
    ''' render the invalid page with April Oneil on it'''
    return render(request, 'ninjas/invalid.html')
