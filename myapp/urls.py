from django.urls import path
from .views import *

urlpatterns=[
    path('hello/',hellobase),
    path('portfolio/',portfolio,name='portfolio_page'),
    path('',home,name='homepage'),
    path('features/',features,name='featurespage'),
    path('pricing/',pricing,name='pricepage'),
    path('table/',template_table,name='table'),
    path('student/',studentdetails,name='studentpage'),
    
]
