# Generated by Django 4.2.7 on 2023-11-23 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commission', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advancepayment',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]
