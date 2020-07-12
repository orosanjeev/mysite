from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

   # return HttpResponse('hello')

def about(request):
    return HttpResponse("<h1> about mysite </h1> ")

def service(request):
    return HttpResponse('service of mysite')

def test(request):
    return render(request, 'test.html')