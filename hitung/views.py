from django.shortcuts import render

# Create your views here.


def batamerah(request):

    return render(request, 'batamerah.html')


def bataringan(request):

    return render(request, 'bataringan.html')


def batako(request):

    return render(request, 'batako.html')


def panduan(request):

    return render(request, 'panduan.html')

def harga(request):

    return render(request, 'harga.html')
