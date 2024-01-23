"""
URL configuration for Django_learning_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from myapp.views import hello
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hello/',hello), #pattern is path(<url>,<function>) 
    # mathi ko url lai if multiple apps xa vane savlai lekhera import garna jhyau hunxa tesko lagi yesto garne 
    path("myapp/",include('myapp.urls')),
]
