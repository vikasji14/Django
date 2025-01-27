from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__' # This will include all the fields of the Employee model in the form. If you want to include only specific fields, you can specify them in the fields attribute as a list.