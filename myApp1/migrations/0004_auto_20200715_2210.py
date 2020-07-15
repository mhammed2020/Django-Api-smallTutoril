# Generated by Django 3.0.8 on 2020-07-15 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp1', '0003_auto_20200715_0040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloger',
            name='subject',
        ),
        migrations.AddField(
            model_name='bloger',
            name='job_type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bloger',
            name='title',
            field=models.CharField(default='', max_length=80),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bloger',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]