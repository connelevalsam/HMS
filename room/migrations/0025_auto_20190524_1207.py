# Generated by Django 2.1.7 on 2019-05-24 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0020_salary'),
        ('room', '0024_auto_20190524_1206'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='room_images',
            new_name='room_image',
        ),
    ]
