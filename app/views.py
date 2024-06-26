from django.shortcuts import render

# Create your views here.

def fire(request):
    return render(request,"fire.html")

def sky(request):
    return render(request,"sky.html")