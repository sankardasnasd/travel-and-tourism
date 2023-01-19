# Generated by Django 4.1.2 on 2023-01-17 06:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("tour", "0015_package_package_days"),
    ]

    operations = [
        migrations.CreateModel(
            name="Amenities",
            fields=[
                (
                    "uid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateField(auto_now=True)),
                ("updated_at", models.DateField(auto_now=True)),
                ("amenity_name", models.CharField(max_length=100)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Hotel",
            fields=[
                (
                    "uid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateField(auto_now=True)),
                ("updated_at", models.DateField(auto_now=True)),
                ("hotel_name", models.CharField(max_length=100)),
                ("hotel_price", models.IntegerField()),
                ("description", models.TextField()),
                ("room_count", models.IntegerField(default=10)),
                ("amenities", models.ManyToManyField(to="tour.amenities")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="HotelImages",
            fields=[
                (
                    "uid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateField(auto_now=True)),
                ("updated_at", models.DateField(auto_now=True)),
                ("images", models.ImageField(upload_to="hotels")),
                (
                    "hotel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="tour.hotel",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]