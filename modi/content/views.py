from django.shortcuts import render
from math import ceil
from django.http import HttpResponse
from .models import mobile, baby_mo, footwear_mo, shoes_mo
# Create your views here.
def first(request):
    data=mobile.objects.all()
    print(data)

    return render(request, 'mobile/mobile1.html', context={'data':data})

def shoo(request):
    data = footwear_mo.objects.all()
    return render(request, 'footwear/footwear1.html', {'data':data})



def baby(request):
    data = baby_mo.objects.all()
    return render(request, 'baby/baby1.html', {'data':data})


