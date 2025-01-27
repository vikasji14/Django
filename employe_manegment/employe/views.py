from django.shortcuts import render
from django.http import HttpResponse
from .form import EmployeeForm
from django.shortcuts import redirect
from .models import Employee
# Create your views here.

def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')  # Replace 'list' with the correct name of the URL pattern for the employee list view
    else:
        form = EmployeeForm()
    return render(request, 'create.html', {'form': form})


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'list.html', {'employees': employees})

def employee_update(request, employee_id):
    employee = Employee.objects.get(employee_id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'update.html', {'form': form})


def employee_delete(request, employee_id):
    employee = Employee.objects.get(employee_id=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('list')