# Generated by Django 5.2.1 on 2025-05-30 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ['name'], 'verbose_name': 'Subject', 'verbose_name_plural': 'Subjects'},
        ),
        migrations.AddField(
            model_name='subject',
            name='name',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
    ]
