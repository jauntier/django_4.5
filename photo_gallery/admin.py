from django.contrib import admin
from .models import Instructor, Student, Course

admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(Course)
