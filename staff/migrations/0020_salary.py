# Generated by Django 2.1.7 on 2019-05-23 11:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0019_revenue_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_date', models.DateTimeField(blank=True, null=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('action_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_employee', to='staff.employee')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hotel_employee', to='staff.employee')),
            ],
        ),
    ]