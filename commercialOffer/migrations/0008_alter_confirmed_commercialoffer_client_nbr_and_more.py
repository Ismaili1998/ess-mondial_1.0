# Generated by Django 4.2.7 on 2023-12-02 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercialOffer', '0007_alter_commercialoffer_client_nbr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmed_commercialoffer',
            name='client_nbr',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='confirmed_commercialoffer',
            name='confirmation_nbr',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
