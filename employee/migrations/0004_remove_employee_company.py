# Generated by Django 3.0.5 on 2022-07-01 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_employee_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='company',
        ),
    ]
