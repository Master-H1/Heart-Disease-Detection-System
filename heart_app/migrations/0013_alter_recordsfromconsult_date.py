# Generated by Django 5.0 on 2024-04-13 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heart_app', '0012_recordsfromconsult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordsfromconsult',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
