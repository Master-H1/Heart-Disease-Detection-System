# Generated by Django 5.0 on 2024-04-14 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heart_app', '0018_alter_assigned_test_from_heart_dep_date_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Assigned_Test_from_Heart_dep',
            new_name='Assigned_Test_from_Doctor_dep',
        ),
    ]
