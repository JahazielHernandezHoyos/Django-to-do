import http
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def task(request):
    metodo = request.method
    if metodo == "GET":
        dictionary = {
            "id": 0,
            "estado": "por hacer",
            "checklist": ["Coding", "Art", "Gaming", "Cricket", "Piano"]
        }
        return JsonResponse(dictionary)
    if metodo == "POST":
        body = json.loads(request.body.decode("utf-8"))
        print(type(body))
        resultado = int(body["numero1"]) + int(body["numero2"])
        return JsonResponse({"resutlado":resultado})