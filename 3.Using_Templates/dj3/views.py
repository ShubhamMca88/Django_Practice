from django.shortcuts import render

# Create your views here.

def index (reqest):
    return render(reqest, 'index.html')