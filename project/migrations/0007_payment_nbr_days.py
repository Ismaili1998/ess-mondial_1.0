# Generated by Django 4.2.7 on 2023-11-30 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_rename_client_contact_project_buyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='nbr_days',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
