# Generated by Django 5.0 on 2024-04-16 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heart_app', '0028_doctor_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heart_medical_history',
            name='date_recorded',
            field=models.DateField(auto_now_add=True),
        ),
    ]