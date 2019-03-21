from django.urls import path
from . import views

urlpatterns = [
    path('livestock/', views.livestock_report, name='livestockReport')
]
