# Generated by Django 3.1.5 on 2021-03-08 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210307_2311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='created',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='updated',
        ),
    ]
