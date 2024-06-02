# Generated by Django 5.0.6 on 2024-06-01 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodDonor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor_id', models.CharField(max_length=255)),
                ('blood_type', models.CharField(max_length=5)),
                ('lat', models.DecimalField(decimal_places=4, max_digits=7)),
                ('long', models.DecimalField(decimal_places=4, max_digits=7)),
            ],
        ),
    ]
