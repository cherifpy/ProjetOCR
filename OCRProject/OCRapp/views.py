from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.template import loader
from .testclass import Tesssst


def index(request):
    
    reponse = {
        "message": "Hello OCR!"
    }
    return render(request,'OCRapp/index.html',reponse)



