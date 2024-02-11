from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from myapp.models import ClassRoom,Student,StudentProfile
# Create your views here.
class HomeView(TemplateView):
    template_name="classbased/home.html"



class ClassRoomView(ListView):
    template_name='classbased/classroom_add.html'

    #aagadi normally functional approach ma hamile tala return garda request,template name(html file),context load garya them
    #yo context vitra query set pathako them tei garne yesma ni for which
    queryset=ClassRoom.objects.all() #context ko value ko kaam garxa automatically
    context_object_name="classrooms" #context ko key ko naam dine kaam garxa automatically
