# Generated by Django 4.1 on 2022-08-07 14:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stokka', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset_location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asset_Type', models.CharField(choices=[('Laptop', 'Laptop'), ('Desktop', 'Desktop'), ('UPS', 'UPS'), ('Printer', 'Printer'), ('Scanner', 'Scanner')], max_length=10, null=True)),
                ('Asset_Name', models.CharField(max_length=15)),
                ('Asset_Model', models.CharField(max_length=15)),
                ('Serial_No', models.CharField(max_length=15)),
                ('Mac_address', models.CharField(max_length=15)),
                ('RAM_Size', models.CharField(max_length=10)),
                ('HDD_Size', models.CharField(max_length=10)),
                ('Power_capacity', models.CharField(max_length=10)),
                ('time_created', models.DateTimeField(default=datetime.datetime.now)),
                ('asset_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stokka.asset_location')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]