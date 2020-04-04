import re
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse


print("Test URL is http://127.0.0.1:5000/hello/pks")
print("This is for signning commit")


def home(request):
    return render(request, "hello/home.html")


def about(request):
    return render(request, "hello/about.html")


def contact(request):
    return render(request, "hello/contact.html")


def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )


# Create your views here.
