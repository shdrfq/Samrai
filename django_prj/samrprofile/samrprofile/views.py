import pandas as pd
from django.http import HttpResponse #to show only text message on page
from django.shortcuts import render # to render new page


# def home(request):
#     return HttpResponse("It is home function")
def index(request):
     data={
           'title':"Samria",
           'clist':['PHP','JAVA','DJANGO'],
            'sdetail': [{"name":"shahid","age":25,"salary": 50000},
                        {"name":"ali","age":25,"salary": 60000}  ,
                         {"name":"imran","age":45,"salary": 160000}  ] 

        

             }

     return render(request,"index.html",data)
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
"""
def load_excel_data(request):
    # Load your Excel file
    file_path = '/static/data/beltdata.xlsx'  # Specify the path to your Excel file
    data = pd.read_excel(file_path)

    # Process data (if needed)
    # For example, let's filter or summarize the data
    data_summary = data.describe()  # This gives a statistical summary of numerical columns

    # Convert the Pandas DataFrame to HTML to display it in a Django template
    html_data = data.to_html()  # Or use data_summary.to_html() for summarized data

    return HttpResponse(html_data)

"""


def load_excel_data(request):
    file_path = '/static/data/beltdata.xlsx'
    data = pd.read_excel(file_path)
    data_summary = data.describe()  # Optional data processing

    # Convert DataFrame to HTML for use in template
    html_data = data.to_html(classes='table table-striped')  # Add classes for styling (optional)

    return render(request, 'data_template.html', {'data': html_data})