# Generated by Django 4.1.7 on 2023-03-13 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_alter_client_email1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='credit_limit',
            field=models.FloatField(),
        ),
    ]