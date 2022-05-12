from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    print(request.user)
    return render(request, "home.html", {})

def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact Page</h1>")

def about_view(request):
    my_context = {
        "my_text": "This is me",
        "my_number": 61400000000,
        "my_list": ["AUS", "TWD", 123],
        "my_html": "<h3>Hey World</h3>"
    }
    return render(request, "about.html", my_context)