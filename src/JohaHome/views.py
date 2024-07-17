# src/JohaHome/views.py
from django.http import HttpResponse

def home_page(request, *args, **kwargs):
    return HttpResponse("<h1>Hello, world!</h1>")
