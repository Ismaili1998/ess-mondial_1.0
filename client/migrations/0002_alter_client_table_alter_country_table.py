# Generated by Django 4.1.7 on 2023-03-12 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='client',
            table='client',
        ),
        migrations.AlterModelTable(
            name='country',
            table='country',
        ),
    ]