# Generated by Django 4.1.2 on 2023-01-18 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tour", "0023_remove_packagebooking_user_address_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="package",
            name="user_address",
        ),
        migrations.RemoveField(
            model_name="package",
            name="user_phone",
        ),
        migrations.AddField(
            model_name="packagebooking",
            name="user_address",
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="packagebooking",
            name="user_phone",
            field=models.TextField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
