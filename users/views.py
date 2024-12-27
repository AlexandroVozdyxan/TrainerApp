from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def user_page(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def specific_user(request, user_id):
    return HttpResponse("Hello, world. You're at the polls index.")

def login_page(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def logout_page(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def register_page(request):
    return HttpResponse("Hello, world. You're at the polls index.")
