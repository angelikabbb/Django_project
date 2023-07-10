from django.urls import path
from .views import *

app_name = 'myapp'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contacts/<int:id>', contacts, name='contacts'),

    path('cars/<int:pk>/', car_card, name='car_card'),
    path('cars/', cars, name='cars'),
    path('add_car/', add_car, name='add_car'),

    path('driver_card/<int:pk>/', driver_card, name='driver_card'),
    path('drivers/', drivers, name='drivers'),
    path('add_driver/', add_driver, name='add_driver'),

    path('clients/<int:pk>/', client_card, name='client_card'),
    path('clients/', clients, name='clients'),
    path('add_client/', add_client, name='add_client'),

    path('employees/<int:pk>/', EmployeeUpdate.as_view(), name='employee-update'),
    path('employees/<int:pk>/', EmployeeDelete.as_view(), name='employee-delete'),
    path('employees/', EmployeeList.as_view(), name='employee_list'),
    path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),
    path('employee_form/', EmployeeCreate.as_view(), name='employee-form'),
]

