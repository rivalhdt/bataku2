from django.urls import path
from . views import *
app_name = 'hitung'

urlpatterns = [
    path('batamerah', batamerah, name='batamerah'),
    path('bataringan', bataringan, name='bataringan'),
    path('batako', batako, name='batako'),
    path('panduan', panduan, name='panduan'),
    path('harga', harga, name='harga'),
    path('panduan2', panduan2, name='panduan2'),
]
