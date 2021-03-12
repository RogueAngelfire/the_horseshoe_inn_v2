from django.shortcuts import render, HttpResponse


def index(request):
    """ A view to return the index page """
    context = {
        
    }
    template = "home/index.html"

    return render(request, template, context)
