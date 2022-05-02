from django.shortcuts import render
from django.http import HttpResponse
def f1(request):
    return HttpResponse('Hai,this is project3')

def f2(request):
    return render(request,'index.html')

def f10(request):
    return render(request,'genstat.html')

def f12(request):
    return render(request,'urlnavg1.html')

def f13(request):
    return render(request,'urlnavg2.html')