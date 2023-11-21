from django.shortcuts import render

# Create your views here.


def forloop(request):
    d={'Name':'Ramesh'}
    return render(request,'forloop.html',d)