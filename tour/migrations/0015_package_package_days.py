# Generated by Django 4.1.2 on 2023-01-10 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tour", "0014_remove_package_package_image_package_package_images"),
    ]

    operations = [
        migrations.AddField(
            model_name="package",
            name="package_days",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]