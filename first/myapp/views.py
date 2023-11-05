from django.shortcuts import render, redirect
from .form import EmployeeForm
from .models import Employee
from myapp.models import WangUser
from myapp.form import UserReg
from myapp import models


# def index(request):
#     student = StudentForm()
#     return render(request,"index.html",{'form':student})

def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


def service(request):
    return render(request, 'service.html')


def index(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form = form.save()
                return redirect('about')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form': form})


def about(request):
    emp = Employee.objects.all()
    return render(request, 'about.html', {'form2': emp})


def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/about")


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/about")
    return render(request, "edit.html", {'employee': employee})


def register(request):
    if request.method == 'POST':

        username = request.POST.get('username')

        email = request.POST.get('email')

        password = request.POST.get('password')

        user_list = models.WangUser.objects.filter(username=username)

        error_name = []
        if user_list:
            error_name = 'The user name already exists'

            return render(request, 'request.html', {'error_name': error_name})
        else:
            username = models.WangUser.objects.create(username=username, password=password)

            username.save()

        return redirect('/login')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        obj_user = models.WangUser.objects.filter(username=username, password=password)
        if obj_user:
            return redirect('/index')

        error = 'Wrong username and password'

    return render(request, 'login.html', locals())
