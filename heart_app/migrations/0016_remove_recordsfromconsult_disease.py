# Generated by Django 5.0 on 2024-04-13 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heart_app', '0015_patients_disease'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recordsfromconsult',
            name='disease',
        ),
    ]
