# Generated by Django 3.2.8 on 2023-03-23 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunityboard', '0008_alter_opportunity_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='staffing',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
