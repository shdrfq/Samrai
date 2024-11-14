from django.http import HttpResponse #to show only text message on page
from django.shortcuts import render # to render new page

# def home(request):
#     return HttpResponse("It is home function")
def index(request):
    return render(request,"index.html")
# def aboutus(request):
#     return HttpResponse("It is aboutus function")
def about(request):
     return render(request,"about.html")

# def category(request):
#     return HttpResponse("It is category function")
def category(request):
     return render(request,"category.html")


# def testimonial(request):
#     return HttpResponse("It is testimonial function")
def testimonial(request):
     return render(request,"testimonial.html")
# def blog(request):
#     return HttpResponse("It is blog function")
def blog(request):
     return render(request,"blog.html")
# def contact(request):
#     return HttpResponse("It is contact function")
def contact(request):
     return render(request,"contact.html")

# def categorydetail(request,catid):
#      return HttpResponse(catid)
def categorydetail(request):
     return render(request,"categorydetail.html")