from django.urls import path
from .views import *
urlpatterns = [
    path('',HomeView.as_view(),name='classbased_home'),
    path('classroom/',ClassRoomView.as_view(),name='classbased_classroom'),
]
