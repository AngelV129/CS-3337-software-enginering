from django.shortcuts import render
from .models import MainMenu

# Create your views here.

from django.http import HttpResponse


def index(request):
    #return HttpResponse(" { \"info\" : { \" author \" : \" xcode \"} }")
    # return render(request, "base.html")
    return render(request,
                  "bookMng/displaybooks.html",
                    {
                        'item_list': MainMenu.objects.all()
                     }
                  )
