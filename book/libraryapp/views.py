from django.shortcuts import render
# HttpResponse is used to
# pass the information 
# back to view
from django.http import HttpResponse

from .forms import InputForm
 
# Defining a function which
# will receive request and
# perform task depending 
# upon function definition
def hello_geeks (request) :
 
    # This will return Hello Geeks
    # string as HttpResponse
    return HttpResponse("Hello Geeks")

 
# Create your views here.
def home_view(request):
    context ={}
    context['form']= InputForm()
    return render(request, "home.html", context)