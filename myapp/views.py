from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hellobase(request):
    return render(request,'base.html')

def portfolio(request):
    return render(request,template_name='index.html')

def home(request):
    return render(request,'home.html')

def features(request):
    return render(request,'features.html')

def pricing(request):
    return render(request,'pricing.html')

def template_table(request):

    items=[{"name":"abc","storelocation":"KTM", "price":300},
           {"name":"def","storelocation":"PKR", "price":500},
           {"name":"ghi","storelocation":"BRT", "price":700}]
    
    data={"name":"Kashyap", "age":22, "address":"KTM", "items":items}

    #for context passing, the data should be in a dictionary format 
    return render(request,'temp_inherit_table.html',context=data)

