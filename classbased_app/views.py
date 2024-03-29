from typing import Any
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,CreateView,UpdateView
from myapp.models import ClassRoom,Student,StudentProfile
from .forms import ClassRoomModelForms,StudentProfileForms

#to redirect after a form has been submitted
from django.urls import reverse_lazy


# Create your views here. 
class HomeView(TemplateView):
    template_name="classbased/home.html"



class ClassRoomView(CreateView):
    form_class=ClassRoomModelForms
    template_name='classbased/classroom_add.html'

    #aagadi normally functional approach ma hamile tala return garda request,template name(html file),context load garya them
    #yo context vitra query set pathako them tei garne yesma ni for which
    queryset=ClassRoom.objects.all() #context ko value ko kaam garxa automatically
    # context_object_name="classrooms" #context ko key ko naam dine kaam garxa automatically
    success_url=reverse_lazy('classbased_classroom')#to redirect to this page after form has been submitted and data has been written in the database


    #hamile mathi ko matra garem vane context ma gayera classroom jadaina so to overwritr the data we do
    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['classrooms']=ClassRoom.objects.all()
        return context


class AddStudentView(CreateView):
    form_class=StudentProfileForms
    template_name='classbased/add_student.html'
    success_url=reverse_lazy('classbased_std')
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['classrooms']=ClassRoom.objects.all()
        return context

class StudentView(ListView):
    template_name='classbased/student.html'
    queryset=StudentProfile.objects.all()
    context_object_name="students"


def delete_class(request,id):
    if request.method=='POST':
        ClassRoom.objects.get(id=id).delete()
        return redirect('classbased_classroom')
    return render(request,'classbased/delete.html',context={'classroom':ClassRoom.objects.get(id=id)})

class ClassRoomUpdateView(UpdateView):
    template_name="classbased/classroom_update.html"
    form_class=ClassRoomModelForms
    queryset=ClassRoom.objects.all()
    success_url=reverse_lazy("classbased_classroom") #yesle sumbit vaye yo url ma lanxa
    
