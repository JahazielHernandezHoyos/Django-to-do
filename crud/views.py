import http
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse

def task(request):
    dictionary = {
        "id": 0,
        "estado": "por hacer",
        "checklist": ["Coding", "Art", "Gaming", "Cricket", "Piano"]
    }
    return JsonResponse(dictionary)