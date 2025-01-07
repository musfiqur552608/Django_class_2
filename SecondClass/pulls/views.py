from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def contact(request):
    return HttpResponse("Thanks for contacting us. We will get back to you soon.")

