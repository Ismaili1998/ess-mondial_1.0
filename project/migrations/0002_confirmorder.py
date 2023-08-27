# Generated by Django 4.1.7 on 2023-08-05 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirm_nbr', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'confirm_order',
            },
        ),
    ]