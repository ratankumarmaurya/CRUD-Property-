from django import forms
from myapp.models import Employee
from myapp.models import WangUser
# class StudentForm(forms.Form):
#     firstname = forms.CharField(label="Enter first name",max_length=50)
#     lastname  = forms.CharField(label="Enter last name", max_length = 100)

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class UserReg(forms.ModelForm):
    class meta:
        model = WangUser
        fields = "__all__"