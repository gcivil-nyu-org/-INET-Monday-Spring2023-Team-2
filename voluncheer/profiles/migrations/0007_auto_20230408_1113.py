# Generated by Django 3.2.8 on 2023-04-08 15:13

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0006_alter_volunteer_badges"),
    ]

    operations = [
        migrations.AlterField(
            model_name="badge",
            name="img",
            field=models.ImageField(
                storage=django.core.files.storage.FileSystemStorage(location=None),
                upload_to="badges",
            ),
        ),
        migrations.AlterField(
            model_name="badge",
            name="type",
            field=models.IntegerField(choices=[(0, "VOLUNTEER_LEVEL")]),
        ),
    ]
