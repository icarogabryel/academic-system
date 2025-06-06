from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    # username and password
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True  # Don't create a table for this model


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
    options = (
        ('teacher', 'Teacher'),
        ('coordinator', 'Coordinator'),
    )
    role = models.CharField(
        max_length=20,
        choices=options,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['role', 'name']
