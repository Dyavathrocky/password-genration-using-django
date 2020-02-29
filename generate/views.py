from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    return render(request,'generate\home.html')

def about(request):
    return render(request,'generate\\about.html')

def password(request):

    thepassword = 'testing'
    
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    
    if request.GET.get('specialcase'):
        characters.extend(list('!@#$%^&*()_+'))

    length  = int(request.GET.get('length',12))

    thepassword = ''
    for x in range((length)):
        thepassword += random.choice(characters)


    return render(request , 'generate\password.html',{'password':thepassword})