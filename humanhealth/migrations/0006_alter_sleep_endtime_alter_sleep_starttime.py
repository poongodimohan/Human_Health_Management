# Generated by Django 5.0.4 on 2024-04-12 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humanhealth', '0005_location_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sleep',
            name='Endtime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='sleep',
            name='Starttime',
            field=models.DateTimeField(),
        ),
    ]
