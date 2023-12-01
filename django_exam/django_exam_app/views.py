from django.shortcuts import render
from .models import Task
# Create your views here.
def main_page(request):
    tasks = Task.objects.all()


    return render(request,'index.html',context={'tasks':tasks})  

def index_page(request):
    tasks = Task.objects.all()

    return render(request,'index_2.html',context={'tasks':tasks}) 