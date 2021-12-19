# Generated by Django 3.2.9 on 2021-12-17 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apicar', '0003_auto_20211217_2103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='car_id',
        ),
        migrations.AddField(
            model_name='rating',
            name='car_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='apicar.car'),
        ),
    ]
