# Generated by Django 5.0.6 on 2024-06-01 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_blooddonor_donor_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddonor',
            name='donor_id',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
