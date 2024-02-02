from django.shortcuts import render,HttpResponse,redirect
from myapp.models import ClassRoom
# Create your views here.



#Create operation:
def add_classroom(request):

    classrooms=ClassRoom.objects.all()
    context={'classrooms':classrooms}
    if request.method == 'POST':
        name=request.POST.get("classname") #form ma name=classname haleko xa so classname
        # or yesari ni lekhna milxa yeslai but tala jasari lekhda if classname vanne ma data xaina vane error fyalxa while mathi ko jasari garda null fyalxa
        # name=request.POST['classname']
        ClassRoom.objects.create(class_name=name)
        return redirect("add_classroom")
    return render(request,'forms/form.html',context=context)