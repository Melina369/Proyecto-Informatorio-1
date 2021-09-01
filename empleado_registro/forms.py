from django import forms
from django.db.models import fields
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model= Employee
        fields= ('fullname', 'emp_code', 'mobile', 'position')
        labels= {
            'fullname': 'Nombre Completo',
            'emp_code':'Código EMP.',
            'mobile':'Teléfono',
            'position':'Profesión'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False