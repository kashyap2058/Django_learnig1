from django.contrib import admin
from .models import Student,ClassRoom,StudentProfile,Publication,Article
# Register your models here.

admin.site.register(Student)
admin.site.register(ClassRoom)
admin.site.register(StudentProfile)
admin.site.register(Publication)
admin.site.register(Article)