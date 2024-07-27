from django.shortcuts import render, get_object_or_404
from .models import Course, Student

def index(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})

def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'courses/student_detail.html', {'student': student})
