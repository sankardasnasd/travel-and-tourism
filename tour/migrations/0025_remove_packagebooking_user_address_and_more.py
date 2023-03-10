# Generated by Django 4.1.2 on 2023-01-18 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tour", "0024_remove_package_user_address_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="packagebooking",
            name="user_address",
        ),
        migrations.RemoveField(
            model_name="packagebooking",
            name="user_phone",
        ),
        migrations.AddField(
            model_name="hotelbooking",
            name="user_address",
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="hotelbooking",
            name="user_phone",
            field=models.TextField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
