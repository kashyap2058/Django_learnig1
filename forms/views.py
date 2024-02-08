from django.shortcuts import render,HttpResponse,redirect
from myapp.models import ClassRoom, Student, StudentProfile
import myapp.urls
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


def add_student(request):
    
    
    if request.method == "POST":
        sname=request.POST.get('stdname')
        sage=request.POST.get('stdage')
        saddress=request.POST.get('stdaddress')
        semail=request.POST.get('stdemail')
        sclassroom=request.POST.get('classselect')
        # Student.objects.create(name=sname,age=sage,address=saddress,email=semail,classroom_id=sclassroom) yesto chai hamile student profile ma student saga relationship rakheko vaye garna milthyo but yo case ma tala jasari garna parxa coz student ko data hamilai chainxa studentprofile ma halna
        student=Student.objects.create(name=sname,age=sage,address=saddress,email=semail,classroom_id=sclassroom)


        
        sphone=request.POST.get('sphone')
        sbio=request.POST.get('sbio')
        sroll=request.POST.get('sroll')
        spic=request.FILES.get('spic') #pic is a file so get garda files bata garne
        
        profile=StudentProfile.objects.create(phone=sphone,roll_no=sroll,bio=sbio,student=student)
        if spic:
            profile.profile_pic=spic
            profile.save()
        return redirect('studentpage')
    classrooms=ClassRoom.objects.all()
    context={#'students':students, # students nahalda ni kei hunna coz form ma student ko object nikalnai pardaina
             'classrooms':classrooms}
    return render(request,'forms/student_form.html',context=context)


def delete_student(request,id): #url bata pathako id lai views ma catch garna milxa tei gareko 
    student=StudentProfile.objects.get(id=id)
    if request.method=="POST":
        studentdelete=student.student.id
        Student.objects.get(id=studentdelete).delete()
        return redirect('studentpage')
    return render(request,'forms/delete_student.html',context={'student':student})

def details_student(request,id):
    student=StudentProfile.objects.get(id=id)
    return render(request,'forms/details_student.html',context={'student':student})


def student_update(request,id):
    classrooms=ClassRoom.objects.all()
    student=StudentProfile.objects.get(id=id)
    context={'student':student,
             'classrooms':classrooms}
    if request.method=='POST':
        sname=request.POST.get('stdname')
        sage=request.POST.get('stdage')
        saddress=request.POST.get('stdaddress')
        semail=request.POST.get('stdemail')
        sclassroom=request.POST.get('classselect')
        studenttabledata=Student.objects.filter(id=student.student_id).update(name=sname,age=sage,address=saddress,email=semail,classroom_id=sclassroom) #yesto chai hamile student profile ma student saga relationship rakheko vaye garna milthyo but yo case ma tala jasari garna parxa coz student ko data hamilai chainxa studentprofile ma halna

        sphone=request.POST.get('sphone')
        sbio=request.POST.get('sbio')
        sroll=request.POST.get('sroll')
        spic=request.FILES.get('spic') #pic is a file so get garda files bata garne
        
        StudentProfile.objects.filter(id=id).update(roll_no=sroll,phone=sphone,bio=sbio)
        
        if spic:
            student.profile_pic=spic
            student.save()

        
        return redirect('studentpage')
    
    return render(request,'forms/update_details.html',context=context)