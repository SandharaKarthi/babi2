from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def grey(request):
    return HttpResponse('Hi .... who is favorite color')