from django.http import HttpResponse
from django.shortcuts import render




def home(request):
    # return HttpResponse("Hello, world. You're at the home page.")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("Hello, world. You're at the about page.")

def contact(request):
    return HttpResponse("Hello, world. You're at the contact page.")

def index(request):
    return HttpResponse("Hello, world. You're at the index page.")

def login(request):
    return HttpResponse("Hello, world. You're at the login page.")

def error(request):
    return HttpResponse("Hello, world. You're at the error page.")