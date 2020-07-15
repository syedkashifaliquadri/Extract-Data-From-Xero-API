from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import *
# Create your views here.


def employee_list(request):
    context = {'employee_list':Invoices.objects.all()}
    return render(request,"employee_register/employee_list.html",context)


def employee_form(request,id=0):
    if request.method == "GET":                     # Ye info lekr ayga
        if id==0:                                   # Yaha ye new bande ko form dakhayega 0 means new user
            form = EmployeeForm()
        else:                                       # yaha jo app link mai id dogy user us ki info dakhyga
            employee = Invoices.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request,"employee_register/employee_form.html", {'form':form})
    else:
        if id==0:                                   # Yaha ye new bande ko form dakhayega 0 means new user
            form = EmployeeForm(request.POST)
        else:                                       # yaha jo app link mai id dogy user us ki info dakhyga or changes karre k bad DB mai b POST karega
            employee = Invoices.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():                         # Form agar sahi fill kara hoga phr DB mai save kar dega
            form.save()
        return redirect('/list')

def employee_delete(request,id):
    employee = Invoices.objects.get(pk=id)
    employee.delete()
    return redirect('/list')