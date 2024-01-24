from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello</h1>")

def portfolio(request):
    return render(request,template_name='index.html')