# Generated by Django 4.0.6 on 2022-07-16 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stokka', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Asset_Model',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='product',
            name='Asset_Name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='product',
            name='Asset_Type',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='product',
            name='HHD_Size',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='Mac_address',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='product',
            name='Memmory_Size',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='Serial_No',
            field=models.CharField(max_length=15),
        ),
    ]
