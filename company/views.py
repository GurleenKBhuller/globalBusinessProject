from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def pestle_view(request):
    return render(request, 'pestle.html')

def hofsted_view(request):
    return render(request, 'hofsted.html')
