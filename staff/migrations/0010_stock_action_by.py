# Generated by Django 2.1.7 on 2019-05-20 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0009_auto_20190520_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='action_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.employee'),
        ),
    ]
