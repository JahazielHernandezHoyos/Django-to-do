import http
from django.http import HttpResponse
from django.shortcuts import render

def task(request):
    return HttpResponse("hola jojos")