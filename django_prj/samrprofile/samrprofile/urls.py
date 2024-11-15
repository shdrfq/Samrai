"""
URL configuration for samrprofile project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from samrprofile import views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about/', views.about),
    path('category/', views.category),
    #path('category/<slug:catid>', views.categorydetail),  # it using for dynamic parameter
    path('testimonial/', views.testimonial),
    path('blog/', views.blog),
    path('contact/', views.contact),
    path('load-excel/', views.load_excel_data, name='load_excel'),
   


]
