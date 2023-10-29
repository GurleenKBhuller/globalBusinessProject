from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def pestle_view(request):
    return render(request, 'pestle.html')

def hofsted_view(request):
    return render(request, 'hofsted.html')

def competitive_view(request):
    return render(request, 'competitiveness.html')

def entry_view(request):
    return render(request, 'entry.html')

def citations_view(request):
    return render(request, 'citations.html')

def goingglobal(request):
    return render(request, 'goingglobal.html')