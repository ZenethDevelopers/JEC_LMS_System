from django.shortcuts import render, get_object_or_404, redirect
from base.models import Department, Student
from .Forms.teacher_forms import DepartmentForm
from .Tool.Tools import student_detials, staff_detials


def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department/department_list.html', staff_detials(request,'Department Details',{'departments': departments}))

def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'department/department_detail.html', staff_detials(request,'Department Detail',{'department': department}))

def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = form.save()
            return redirect('department_detail', pk=department.pk)
    else:
        form = DepartmentForm()
    return render(request, 'department/department_form.html', staff_detials(request,'Create department',{'form': form}))


def department_edit(request, pk):
    department = get_object_or_404(Department, pk=pk)
    old_department_name = department.name  # Get the department name before editing
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            department = form.save()
            new_department_name = form.cleaned_data['name']  # Accessing cleaned_data to retrieve the name field value
            print("Department: ", old_department_name, "->", new_department_name)
            std = Student.objects.filter(department=old_department_name)
            for student in std:
                student.department = new_department_name  # Assigning the new department name to each student's department
                student.save()
            return redirect('department_detail', pk=department.pk)
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'department/department_form.html', staff_detials(request,'Create Edit',{'form': form}))

def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    return render(request, 'department/department_confirm_delete.html', {'department': department})
