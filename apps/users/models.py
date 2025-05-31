from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    # username and password
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Student(Person):
    # student specific fields
    registration = models.CharField(max_length=6, primary_key=True)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['name']

    def __str__(self):
        return self.name


class Employee(Person):
    employee_id = models.CharField(max_length=6, primary_key=True)

    class Meta:
        abstract = True


class Teacher(Employee):
    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
        ordering = ['name']

    def __str__(self):
        return self.name


class Coordinator(Person):
    class Meta:
        verbose_name = 'Coordinator'
        verbose_name_plural = 'Coordinators'
        ordering = ['name']

    def __str__(self):
        return self.name
