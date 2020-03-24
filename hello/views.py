import re
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse


print("Test URL is http://127.0.0.1:5000/hello/pks")


def home(request):
    return HttpResponse("Hello, Django!!!!")


def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )


'''
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"
    
    content = "Hellop there, " + clean_name + "! It's " + formatted_now

    return HttpResponse(content)

'''


# Create your views here.
