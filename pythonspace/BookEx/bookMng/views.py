from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    #return HttpResponse(" { \"info\" : { \" author \" : \" xcode \"} }")
    # return render(request, "base.html")
    return render(request, "bookMng/displaybooks.html")
