# Generated by Django 5.0.6 on 2024-06-02 05:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_requests_description_alter_requests_sent_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='time_slot',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='requests',
            name='sent_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
