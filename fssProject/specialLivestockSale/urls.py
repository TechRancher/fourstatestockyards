from django.urls import path
from . import views

urlpatterns = [
    path('specialLivestockSale/', views.special_livestock_sale, name='specialSales'),
]
