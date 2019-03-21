from django.urls import path
from . import views

urlpatterns = [
    path('sheep', views.sheep_report, name='sheepReport'),
]
