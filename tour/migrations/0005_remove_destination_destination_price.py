# Generated by Django 4.1.2 on 2023-01-09 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tour", "0004_remove_destination_id_remove_destinationimages_id_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="destination",
            name="destination_price",
        ),
    ]