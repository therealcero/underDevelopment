# Generated by Django 5.0.6 on 2024-06-02 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_requests'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='user_id',
            field=models.CharField(default='None', max_length=255),
        ),
    ]