# Generated by Django 5.2.1 on 2025-06-05 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_assignment_teacher'),
        ('users', '0003_remove_teacher_user_employee_delete_coordinator'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
