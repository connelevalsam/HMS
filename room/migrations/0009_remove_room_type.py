# Generated by Django 2.1.7 on 2019-05-18 16:04

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('room', '0008_auto_20190518_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='type',
        ),
    ]
