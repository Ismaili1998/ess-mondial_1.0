# Generated by Django 4.2.7 on 2023-11-19 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='country_name_en',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='country',
            name='country_name_fr',
            field=models.CharField(max_length=200),
        ),
    ]
