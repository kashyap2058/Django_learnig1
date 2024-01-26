from django.db import models

# Create your models here.
# for one to many relationship
class ClassRoom(models.Model):
    class_name =models.CharField(max_length=20)

    def __str__(self):
        return self.class_name
    

#student class ma classroom class ko foreign key hunxa
class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    #tala on_delete vaneko classroom ma data delete vayo vane tyo same classroom vako student ni delete hunxa
    #related_name vaneko chai reverse relation lai ho.
    #null=True ra blank=True chai student table suruma banera data already xa tei vayera tyo narakhi migrations run hunna
    #if classroom surum banera tesma data vayera student ma haleko vaye chai null ra blank lai chalauna parthena

    classroom=models.ForeignKey(ClassRoom,on_delete=models.CASCADE,related_name="classroom_students",null=True,blank=True)

    def __str__(self):
        return self.name
    


#For one to one field ie studentProfile ma every unique student ko profile hunxa testo garda
    
class StudentProfile(models.Model):
    student=models.OneToOneField(Student,on_delete=models.CASCADE)
    phone=models.CharField(max_length=14)
    roll_no=models.IntegerField()
    bio=models.TextField(max_length=500)
    profile_pic=models.FileField(null=True, blank=True,upload_to="profile_pics")


    