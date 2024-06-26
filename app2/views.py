from django.shortcuts import render

# Create your views here.
def heart(request):
    return render(request,"heart.html")

def smile(request):
    return render(request,"smile.html")