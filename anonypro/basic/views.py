from django.shortcuts import render
from django.http import HttpResponse
from basic.models import userInfo

def hello(request):
    return render(request,'index.html')

def enterdetails(request):
    if request.method == "POST":
        name= request.POST.get('name')
        uname= request.POST.get('uname')
        email= request.POST.get('email')
        age= int(request.POST.get('age'))

        info = userInfo(name= name, uname = uname, email= email, age= age)

        info.save()

    return render(request, 'index.html')

# Create your views here.