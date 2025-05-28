from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    # username and password
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['name']

    def __str__(self):
        return self.name
