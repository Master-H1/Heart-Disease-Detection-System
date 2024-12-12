# Generated by Django 5.0 on 2024-04-12 09:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('0', 'Female'), ('1', 'Male')], max_length=1)),
                ('district', models.CharField(max_length=200)),
                ('sector', models.CharField(max_length=200)),
                ('cell', models.CharField(max_length=200)),
                ('village', models.CharField(max_length=100)),
                ('phone', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Patients',
            },
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Specializations',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('0', 'Female'), ('1', 'Male')], max_length=1)),
                ('title', models.CharField(choices=[('Dr.', 'Dr.'), ('Nurse', 'Nurse')], max_length=100)),
                ('phone', models.IntegerField(default=0)),
                ('specialization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='heart_app.specialization')),
            ],
            options={
                'verbose_name_plural': 'Doctors',
            },
        ),
    ]
