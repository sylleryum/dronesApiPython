# Generated by Django 3.1.5 on 2021-01-23 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drones', '0009_auto_20210123_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drone',
            name='drone_categoryss',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theDronesx', to='drones.dronecategory'),
        ),
    ]
