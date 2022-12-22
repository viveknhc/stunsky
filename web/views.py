from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'web/index.html')

def package(request):
    return render(request,'web/package.html')

def uiux(request):
    return render(request,'web/uiux.html')