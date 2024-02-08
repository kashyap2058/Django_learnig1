from django.urls import path
from .views import *
urlpatterns = [
    path("add-classroom/",add_classroom,name='add_classroom'),
    path("add-student/",add_student,name='add_student'),
    path("delete-student/<int:id>/",delete_student,name='delete_student'), #delete garna lai id chainxa so id lai ni url saga pass garne
    path("details-student/<int:id>",details_student,name='details_student'),
    path("update-student/<int:id>",student_update,name='update_student'),
]
