from django.contrib import admin
from .models import Subject, Section, Enrollment, Assignment


admin.site.register(
    [
        Subject,
        Section,
        Enrollment,
        Assignment,
    ]
)
