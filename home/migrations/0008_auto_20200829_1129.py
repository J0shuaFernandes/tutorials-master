# Generated by Django 2.0.7 on 2020-08-29 05:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200828_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 29, 11, 29, 20, 458424), verbose_name='Date Published'),
        ),
    ]