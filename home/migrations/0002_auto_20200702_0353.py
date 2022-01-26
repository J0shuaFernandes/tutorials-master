# Generated by Django 2.0.7 on 2020-07-01 22:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='description',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 2, 3, 53, 19, 171272), verbose_name='Date Published'),
        ),
    ]