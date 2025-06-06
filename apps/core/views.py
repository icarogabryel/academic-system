from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def student_dashboard_view(request):
    """Renders the dashboard view."""
    return render(request, 'student/dashboard.html')


@login_required
def teacher_dashboard_view(request):
    """Renders the teacher dashboard view."""
    return render(request, 'teacher/dashboard.html')


@login_required
def coordinator_dashboard_view(request):
    """Renders the coordinator dashboard view."""
    return render(request, 'coordinator/dashboard.html')
