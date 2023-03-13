# Generated by Django 4.1.7 on 2023-03-13 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0003_remove_user_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organization",
            name="photo",
            field=models.ImageField(default="default-profile-pic.png", upload_to="."),
        ),
        migrations.AlterField(
            model_name="volunteer",
            name="photo",
            field=models.ImageField(default="default-profile-pic.png", upload_to="."),
        ),
    ]
