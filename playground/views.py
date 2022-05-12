from django.shortcuts import render
from django.http import HttpResponse

# request handler: request -> response
# Create your views here.

def calculate():
    x = 1
    y = 2
    return x+y


def say_hello(request):
    # x = 1
    x = calculate()
    return render(request, 'hello.html', {'name':'Jenny'})

    # return HttpResponse("Hello World")