# Generated by Django 2.1.7 on 2019-05-22 09:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0017_auto_20190521_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='revenue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('message', models.TextField(blank=True, default='n/a', null=True)),
                ('action_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.employee')),
            ],
        ),
    ]
