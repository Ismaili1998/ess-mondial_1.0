# Generated by Django 4.2.7 on 2023-11-19 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommercialOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_nbr', models.CharField(max_length=20, unique=True)),
                ('margin', models.DecimalField(decimal_places=2, max_digits=4)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('local_contact', models.BooleanField(default=1)),
                ('confirmed', models.BooleanField(default=0)),
                ('delivery_time_interval', models.CharField(blank=True, max_length=20, null=True)),
                ('duration_in_days', models.IntegerField(blank=True, null=True)),
                ('valid_date', models.DateField(blank=True, null=True)),
                ('shipping_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('transport_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('currency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='project.currency')),
                ('delivery_time_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='project.timeunit')),
                ('destination', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='project.destination')),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='project.payment')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project.project')),
                ('shipping', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='project.shipping')),
                ('transport', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='project.transport')),
            ],
            options={
                'db_table': 'commercial_offer',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Confirmed_commercialOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmation_nbr', models.CharField(max_length=20, unique=True)),
                ('client_nbr', models.CharField(max_length=20, unique=True)),
                ('commission', models.DecimalField(decimal_places=2, max_digits=4)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('commercialOffer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='commercialOffer.commercialoffer')),
            ],
            options={
                'db_table': 'confirmed_commercial_offer',
                'ordering': ['-id'],
            },
        ),
    ]