from django.shortcuts import render

# Create your views here.


def menu(request):

    return render(request, 'menu.html')

def splash(request):

    return render(request, 'menu2.html')
