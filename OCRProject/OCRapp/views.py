from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.template import loader
from .testclass import Tesssst


def index(request):
    class_ = Tesssst()
    reponse = {
        "cherif" :[1,2,3,4,5,6],
        "yanis" : "Agdlksdbnmfbndfobnkdf",
        "cls" : class_
    }
    return render(request,'OCRapp/index.html',reponse)



