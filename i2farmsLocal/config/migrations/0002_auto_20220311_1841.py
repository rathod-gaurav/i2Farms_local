# Generated by Django 3.2.12 on 2022-03-11 13:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop_name', models.CharField(max_length=50)),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('stage_name', models.CharField(default=1, max_length=50)),
                ('span', models.PositiveSmallIntegerField()),
                ('t1_ll', models.DecimalField(decimal_places=2, max_digits=4)),
                ('t1_ul', models.DecimalField(decimal_places=2, max_digits=4)),
                ('t1_err', models.DecimalField(decimal_places=2, default=0.1, max_digits=4)),
                ('h1_ll', models.DecimalField(decimal_places=2, max_digits=4)),
                ('h1_ul', models.DecimalField(decimal_places=2, max_digits=4)),
                ('h1_err', models.DecimalField(decimal_places=2, default=0.1, max_digits=4)),
                ('t2_ll', models.DecimalField(decimal_places=2, max_digits=4)),
                ('t2_ul', models.DecimalField(decimal_places=2, max_digits=4)),
                ('t2_err', models.DecimalField(decimal_places=2, default=0.1, max_digits=4)),
                ('h2_ll', models.DecimalField(decimal_places=2, max_digits=4)),
                ('h2_ul', models.DecimalField(decimal_places=2, max_digits=4)),
                ('h2_err', models.DecimalField(decimal_places=2, default=0.1, max_digits=4)),
                ('pH_ll', models.DecimalField(decimal_places=2, max_digits=4)),
                ('pH_ul', models.DecimalField(decimal_places=2, max_digits=4)),
                ('pH_err', models.DecimalField(decimal_places=2, default=0.1, max_digits=4)),
                ('tds_ll', models.DecimalField(decimal_places=2, max_digits=4)),
                ('tds_ul', models.DecimalField(decimal_places=2, max_digits=4)),
                ('tds_err', models.DecimalField(decimal_places=2, default=0.1, max_digits=4)),
            ],
        ),
        migrations.RenameModel(
            old_name='ConfigTop',
            new_name='AddPlant',
        ),
    ]
