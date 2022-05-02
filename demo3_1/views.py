from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse


class sample():
    def __init__(self,name,roll,phone):
        self.name=name
        self.roll=roll
        self.phone=phone

# Create your views here.
def f3(request):
    obj=sample('sai',123456,9854154)
    return render(request,'home.html',{'a':'25','b':'Hello','c':(10,20),'d':[10,20,30],'e':{'A':10},'f':obj})

def f4(request):
    return render(request,'optag.html',{'var':'hello'})

def f5(request):
    return render(request,'optag.html',{'res':[10,20,30,40]})

def f6(request,data):
    return render(request,'index.html',{'abc':data})

def f7(request):
    return render(request,'home.html',{'m':'hello','n':'hello python'})

def f8(request):
    return render(request,'child.html')

def f9(request):
    return render(request,'partials.html')

def f11(request):
    return render(request,'appstat.html')

def f14(request):
    return render(request,'urlnava1.html')

def f15(request):
    return render(request,'urlnava2.html')