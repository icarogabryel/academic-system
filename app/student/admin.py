from django.contrib import admin
from .models import student


@admin.register(student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('registration', 'name', 'phone')
    search_fields = ('registration', 'name')
    list_filter = ('registration',)
    ordering = ('name',)
    list_per_page = 10
