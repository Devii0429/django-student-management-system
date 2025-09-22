from django.db import models
from django.contrib.auth.models import User
from courses.models import Course

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    enrolled_courses = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"