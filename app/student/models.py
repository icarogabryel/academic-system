from django.db import models
from django.contrib.auth.models import User


class student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # username and password
    registration = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
