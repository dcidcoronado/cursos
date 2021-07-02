from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Course

def index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    if request.method == 'GET': 
        return render(request, 'index.html', context)
    if request.method == 'POST':
        errors = Course.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            Course.objects.create(
            name = request.POST['name'],
            description = request.POST['description']
            )
            messages.success(request, 'Course succesfully created')   
            return redirect('/')


def destroy_page(request, course_id):
    course = Course.objects.get(id=course_id)
    context = {
        'course': course
    }
    return render(request, 'destroy.html', context)


def destroy(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect ('/')