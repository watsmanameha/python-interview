from django.urls import path
from productapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add')
]