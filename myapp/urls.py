from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('contacts/<int:id>', contacts, name='contacts'),
    path('cars/', cars, name='cars'),
    path('add_car/', add_car, name='add_car'),
    path('drivers/', drivers, name='drivers'),
    path('add_driver/', add_driver, name='add_driver'),
    path('clients/', clients, name='clients'),
    path('add_client', add_client, name='add_client')
]

