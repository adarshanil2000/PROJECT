from django.shortcuts import render
from .models import student
# Create your views here.
def index(request):
    obj=student.objects.name()
    return render(request,'index.html',{"student": obj})



