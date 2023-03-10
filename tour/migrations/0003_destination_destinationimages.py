# Generated by Django 4.1.2 on 2023-01-09 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tour", "0002_signup"),
    ]

    operations = [
        migrations.CreateModel(
            name="Destination",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("destination_name", models.CharField(max_length=100)),
                ("destination_details", models.CharField(max_length=500)),
                ("destination_price", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="DestinationImages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("images", models.ImageField(upload_to="destination")),
                (
                    "destination",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="tour.destination",
                    ),
                ),
            ],
        ),
    ]
