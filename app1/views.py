from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def welcome(request):
    # return HttpResponse("欢迎来到首页")
    return render(request, 'app1/home_page.html')


def index(request):
    return HttpResponse("hello django")
