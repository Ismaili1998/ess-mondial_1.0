# Generated by Django 4.1.7 on 2023-08-11 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_delete_confirmorder_commercialoffer_confirmed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commercialoffer',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='commercialoffer',
            name='confirmation_nbr',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]