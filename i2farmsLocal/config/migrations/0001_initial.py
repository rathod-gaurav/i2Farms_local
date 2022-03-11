# Generated by Django 3.2.12 on 2022-03-11 12:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigTop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop_name', models.CharField(max_length=50)),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('no_growth_stages', models.PositiveSmallIntegerField()),
                ('life_span', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
