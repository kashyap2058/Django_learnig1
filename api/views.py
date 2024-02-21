# from django.shortcuts import render api ma render chaidaina so hataideko but api ma data json ma janxa so jason chainxa
from django.http import JsonResponse

# Create your views here.
def hello_world(request):
    return JsonResponse({
        "message":"hello world!!"
    })