# from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import request,HttpResponse
from .models import *
# Create your views here.

def index(request):
    #return HttpResponse('Heyy there')
    student_List = Student.objects.all()
    # print(student_List)
    context = {
        'student_list':student_List
    }
    return render(request,'index.html',context)

def index1(request):
    # return HttpResponse('<h1 style="color:red">Heyy there1</h1>')
    print(request.GET.get('usn'))
    if request.method == 'POST':
        usn2 = request.POST.get('usn')
        name2 = request.POST.get('name')
        age2 = request.POST.get('age')
        branch2 = request.POST.get('branch')

        student_obj = Student(usn = usn2, name = name2, age = int(age2), branch = branch2)
        student_obj.save()
        print(request.POST.get('usn'))
        print(request.POST.get('name'))
        print(request.POST.get('age'))
        print(request.POST.get('branch'))
        return render(request,'success.html')
    else:
        return render(request,'index1.html')
    

def update_delete(request):
    if request.method == 'POST':
        usn = request.POST.get('usn')
        action = request.POST.get('action')

        if action == 'Update':
            return redirect('update_student', usn=usn)
        elif action == 'Delete':
            return redirect('delete_student', usn=usn)

    return render(request, 'update_delete.html')


def updateStudent(request, usn):
    student = get_object_or_404(Student, usn=usn)
    
    if request.method == 'POST':
        # Update student object based on POST data
        student.usn = request.POST.get('usn')
        student.name = request.POST.get('name')
        student.age = int(request.POST.get('age'))
        student.branch = request.POST.get('branch')
        student.save()
        return render(request, 'success.html')
    
    # Render form with existing student data
    context = {
        'student': student,
    }
    return render(request, 'update_student.html', context)


def deleteStudent(request, usn):
    student = get_object_or_404(Student, usn=usn)
    
    if request.method == 'POST':
        # Delete student object
        student.delete()
        return render(request, 'success_delete.html')
    
    # Render confirmation page for delete action
    context = {
        'student': student,
    }
    return render(request, 'delete_student.html', context)

        