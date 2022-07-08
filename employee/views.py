from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from employee.forms import EmployeeForm  
from employee.models import Employee  
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST or None , request.FILES or None) 
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    employees = Employee.objects.all()
    return render(request,"show.html",{'employees':employees})  
def update(request, id):   
    employee = get_object_or_404(Employee, id = id)
    form = EmployeeForm(request.POST or None, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/show") 
    return render(request, "edit.html", {'form':form})
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")