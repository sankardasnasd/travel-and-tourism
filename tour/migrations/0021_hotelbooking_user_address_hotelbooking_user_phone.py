# Generated by Django 4.1.2 on 2023-01-18 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tour", "0020_remove_hotelbooking_number_of_person_and_more"),
    ]

    operations = [
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
