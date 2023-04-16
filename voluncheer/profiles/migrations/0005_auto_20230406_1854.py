# Generated by Django 3.2.8 on 2023-04-06 22:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0004_alter_volunteer_hours_volunteered"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="volunteer",
            name="badges",
        ),
        migrations.AddField(
            model_name="volunteer",
            name="badges",
            field=models.ManyToManyField(related_name="badges", to="profiles.Badge"),
        ),
    ]
