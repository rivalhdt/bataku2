from django.urls import path
from . views import *
app_name = 'menu'

urlpatterns = [
    path('', splash, name='splash'),
    path('menu/', menu, name='menu'),
]
