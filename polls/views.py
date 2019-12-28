from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def first(request):
    context = "Test Data"
    return render(request, 'polls/first.html', {'context': context})
