# Generated by Django 2.1.7 on 2019-05-24 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0020_salary'),
        ('room', '0026_auto_20190524_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='reserve_action_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reserved_by', to='staff.employee'),
        ),
    ]
