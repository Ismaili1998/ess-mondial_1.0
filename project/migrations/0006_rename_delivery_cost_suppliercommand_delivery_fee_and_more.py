# Generated by Django 4.1.7 on 2023-08-15 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
        ('project', '0005_remove_quoterequest_articles_suppliercommand'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suppliercommand',
            old_name='delivery_cost',
            new_name='delivery_fee',
        ),
        migrations.RenameField(
            model_name='suppliercommand',
            old_name='packaging',
            new_name='packaging_fee',
        ),
        migrations.RenameField(
            model_name='suppliercommand',
            old_name='total',
            new_name='transport_fee',
        ),
        migrations.RenameField(
            model_name='suppliercommand',
            old_name='due_date',
            new_name='validity_date',
        ),
        migrations.AddField(
            model_name='suppliercommand',
            name='currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='client.currency'),
        ),
        migrations.AddField(
            model_name='suppliercommand',
            name='quoteRequest',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.quoterequest'),
        ),
    ]