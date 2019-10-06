# Generated by Django 2.1.7 on 2019-05-18 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0005_auto_20190518_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='room_types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=25, null=True)),
                ('no_of_rooms', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='room',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_type', to='room.room_types'),
        ),
    ]