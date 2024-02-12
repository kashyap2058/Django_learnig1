from django import forms
from  myapp.models import ClassRoom,StudentProfile


class ClassRoomModelForms(forms.ModelForm):
    class Meta:
        model=ClassRoom
        fields=["class_name",]


class StudentProfileForms(forms.ModelForm):
    class Meta:
        model=StudentProfile
        fields=["student_id","phone","roll_no","bio","profile_pic",]