# Generated by Django 5.2 on 2025-05-16 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("My_App", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="deleted_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
