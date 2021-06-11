# Generated by Django 3.1.5 on 2021-03-22 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Matricula', models.CharField(max_length=10)),
                ('Nombre', models.CharField(max_length=50)),
                ('ApellidoPater', models.CharField(max_length=20)),
                ('ApellidoMater', models.CharField(max_length=20)),
                ('Correo', models.EmailField(max_length=254)),
                ('Telefono', models.CharField(max_length=10)),
                ('TipoPeriodo', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Alumno',
                'verbose_name_plural': 'Alumnos',
            },
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Cuatrimestral', models.BooleanField()),
                ('NumCuatrimestres', models.IntegerField()),
                ('Semestral', models.BooleanField()),
                ('NumSemestres', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Carrera',
                'verbose_name_plural': 'Carreras',
            },
        ),
    ]
