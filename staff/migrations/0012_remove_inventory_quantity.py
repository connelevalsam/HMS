# Generated by Django 2.1.7 on 2019-05-20 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0011_expense_action_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='quantity',
        ),
    ]
