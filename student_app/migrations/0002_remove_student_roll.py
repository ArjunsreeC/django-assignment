# Generated by Django 3.1.1 on 2020-10-07 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='roll',
        ),
    ]
