# Generated by Django 5.0.6 on 2024-06-02 01:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_long_blooddonor_lgs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=500)),
                ('status', models.IntegerField()),
                ('sent_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]