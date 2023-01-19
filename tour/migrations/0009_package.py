# Generated by Django 4.1.2 on 2023-01-10 04:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("tour", "0008_destination_destination_images_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Package",
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
                ("package_name", models.CharField(max_length=20)),
                ("Package_description", models.CharField(max_length=200)),
                ("package_image", models.ImageField(upload_to="packages")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
