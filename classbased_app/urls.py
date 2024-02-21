from django.urls import path
from .views import *
urlpatterns = [
    path('',HomeView.as_view(),name='classbased_home'),
    path('classroom/',ClassRoomView.as_view(),name='classbased_classroom'),
    path('student/',StudentView.as_view(),name='classbased_std'),
    path('add-student/',AddStudentView.as_view(),name='classbased_addstd'),
    path('delete-class/<int:id>',delete_class,name='classbased_deleteclass'),
    path('update-class/<int:pk>',ClassRoomUpdateView.as_view(),name='classbased_updateclass'), #yesma pk huna parxa coz updateview ma default ma pk linxa
]
