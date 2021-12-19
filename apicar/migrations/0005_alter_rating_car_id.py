# Generated by Django 3.2.9 on 2021-12-17 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apicar', '0004_auto_20211217_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='car_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='apicar.car'),
        ),
    ]
