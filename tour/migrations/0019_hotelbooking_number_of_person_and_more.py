# Generated by Django 4.1.2 on 2023-01-18 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tour", "0018_hotelbooking"),
    ]

    operations = [
        migrations.AddField(
            model_name="hotelbooking",
            name="number_of_person",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="hotelbooking",
            name="user_address",
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
