from django.http import HttpResponse #to show only text message on page
from django.shortcuts import render # to render new page

def index(request):
    return render(request,"index.html")