# Generated by Django 4.1.7 on 2023-03-30 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0001_initial"),
        ("opportunityboard", "0009_remove_opportunity_volunteer_opportunity_volunteer"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="opportunity",
            name="volunteer",
        ),
        migrations.AddField(
            model_name="opportunity",
            name="volunteer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="profiles.volunteer",
            ),
        ),
    ]
