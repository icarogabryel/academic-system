from django.contrib import admin
from .models import Subject, Section


admin.site.register(
    [Subject, Section]
)
