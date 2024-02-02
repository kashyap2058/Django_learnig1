from django.urls import path
from .views import *
urlpatterns = [
    path("add-classroom/",add_classroom,name='add_classroom'),
]
