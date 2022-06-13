from django.shortcuts import render
from . import views

# Create your views here.
def index(request):
    return render(request,'appserv/index.html')