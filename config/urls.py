from django.contrib import admin
from django.urls import path
from apps.users.views import login_view
from apps.core.views import (
    student_dashboard_view,
    teacher_dashboard_view,
    coordinator_dashboard_view
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path(
        'student/dashboard/',
        student_dashboard_view,
        name='student_dashboard'
    ),
    path(
        'teacher/dashboard/',
        teacher_dashboard_view,
        name='teacher_dashboard'
    ),
    path(
        'coordinator/dashboard/',
        coordinator_dashboard_view,
        name='coordinator_dashboard'
    ),
]
