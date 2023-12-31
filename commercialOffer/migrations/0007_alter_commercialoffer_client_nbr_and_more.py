# Generated by Django 4.2.7 on 2023-12-02 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercialOffer', '0006_alter_commercialoffer_warranty_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commercialoffer',
            name='client_nbr',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='confirmed_commercialoffer',
            name='confirmation_nbr',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
