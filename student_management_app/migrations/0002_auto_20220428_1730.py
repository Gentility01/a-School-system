# Generated by Django 3.0.7 on 2022-04-28 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Classes',
            new_name='Courses',
        ),
    ]
