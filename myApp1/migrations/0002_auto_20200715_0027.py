# Generated by Django 3.0.8 on 2020-07-14 23:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloger',
            name='created',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
