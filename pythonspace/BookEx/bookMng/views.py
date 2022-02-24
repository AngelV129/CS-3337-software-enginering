from django.shortcuts import render

from .forms import BookForm
from .models import MainMenu

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    # return HttpResponse(" { \"info\" : { \" author \" : \" xcode \"} }")
    # return render(request, "base.html")
    return render(request,
                  "bookMng/displaybooks.html",
                  {
                      'item_list': MainMenu.objects.all()
                  }
                  )


def postbook(request):
    submitted = False
    form = BookForm
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/postbook?submitted=True')
    else:
        form = BookForm
        if 'submitted' in request.GET:
            submitted = True

        return render(request, "bookMng/postbook.html",
                      {
                          'form': form,
                          'item_list': MainMenu.objects.all(),
                          'submitted': submitted
                      }
                      )
