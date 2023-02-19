# Generated by Django 4.1.5 on 2023-02-02 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voluncheer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=256)),
                ('user_id', models.IntegerField(default=4294967295)),
                ('user_email', models.CharField(max_length=256)),
                ('user_address_city', models.CharField(max_length=256)),
                ('user_address_zipcode', models.IntegerField()),
                ('user_image', models.CharField(max_length=256)),
            ],
        ),
        migrations.RenameField(
            model_name='job',
            old_name='work_location',
            new_name='job_image',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='work_time',
            new_name='job_location',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='pub_date',
            new_name='job_pubdate',
        ),
        migrations.RenameField(
            model_name='organization',
            old_name='name',
            new_name='organization_name',
        ),
        migrations.AddField(
            model_name='job',
            name='job_id',
            field=models.IntegerField(default=4294967295),
        ),
        migrations.AddField(
            model_name='job',
            name='job_organization',
            field=models.IntegerField(default=4294967295),
        ),
        migrations.AddField(
            model_name='job',
            name='job_worktime',
            field=models.CharField(default='Not Specified', max_length=256),
        ),
        migrations.AddField(
            model_name='organization',
            name='organization_id',
            field=models.IntegerField(default=4294967295),
        ),
    ]
