# Generated by Django 3.0.7 on 2022-04-29 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0002_auto_20220428_1730'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Courses',
            new_name='Classes',
        ),
    ]
