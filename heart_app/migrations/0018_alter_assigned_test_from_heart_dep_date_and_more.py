# Generated by Django 5.0 on 2024-04-13 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heart_app', '0017_alter_assigned_test_from_heart_dep_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assigned_test_from_heart_dep',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='recordsfromconsult',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]