from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Student, Employee


def is_student(user: User) -> bool:
    return Student.objects.filter(user=user).exists()


def is_employee(user: User) -> bool:
    return Employee.objects.filter(user=user).exists()


def login_view(request: HttpRequest) -> HttpResponse:
    """Handles user login."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        profile = request.POST.get('profile')

        print(f"Username: {username}, Profile: {profile}")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if profile == 'student':
                if not is_student(user):
                    messages.error(request, 'Invalid student credentials.')
                    return redirect('login')

                login(request, user)

                return redirect('student_dashboard')
            elif profile == 'employee':
                if not is_employee(user):
                    messages.error(request, 'Invalid employee credentials.')
                    return redirect('login')

                login(request, user)

                employee = Employee.objects.get(user=user)

                if employee.role == 'coordinator':
                    return redirect('coordinator_dashboard')
                elif employee.role == 'teacher':
                    return redirect('teacher_dashboard')
                else:
                    messages.error(request, 'User does not have a valid role.')
            else:
                messages.error(request, 'User does not have a valid profile.')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')
