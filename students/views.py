from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Student

def home(request):
    return render(request, 'home.html')

@login_required
def student_dashboard(request):
    try:
        student = Student.objects.get(user=request.user)
        context = {
            'student': student,
            'enrolled_courses': student.enrolled_courses.all(),
        }
        return render(request, 'students/dashboard.html', context)
    except Student.DoesNotExist:
        return render(request, 'students/not_student.html')