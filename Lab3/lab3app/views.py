
# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def comparison(request):
    return render(request, 'comparison.html')

def activate_engines(request):
    return render(request, 'activate-engines.html')

def dtl_filters(request):
    return render(request, 'dtl-filters.html')

