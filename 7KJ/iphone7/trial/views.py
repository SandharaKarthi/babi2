from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def greens(request):
    return HttpResponse('Hi .... karthika how are you')

def blue(request):
    a=105
    b=[6,7,8,9,3,2,1,]
    return render(request, 'first.html',{"ki":a , "kl":b})

