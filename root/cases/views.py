from django.shortcuts import render

def index(request):
    return render(request, 'cases.html')
# Create your views here.
