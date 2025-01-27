from django.urls import path
from django.urls import include, path
from .views import create_employee, employee_list, employee_update, employee_delete


urlpatterns = [
    path('', employee_list, name='list'),
    path('create/', create_employee, name='create'), 
    path('update/<int:employee_id>/', employee_update, name='update'),
    path('delete/<int:employee_id>/', employee_delete, name='delete'),  
]