from django.db import models
from teachers.models import Teacher

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    credits = models.IntegerField(default=3)

    def __str__(self):
        return self.name