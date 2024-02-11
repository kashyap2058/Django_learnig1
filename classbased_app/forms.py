from django import forms
from  myapp.models import ClassRoom


class ClassRoomModelForms(forms.ModelForm):
    class Meta:
        model=ClassRoom
        fields=["class_name",]