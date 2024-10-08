from django.shortcuts import render
# books/views.py

from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to the Books section!")
