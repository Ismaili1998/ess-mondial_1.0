# Generated by Django 4.2.7 on 2023-11-19 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_nbr', models.CharField(max_length=30, unique=True)),
                ('client_name', models.CharField(max_length=150, null=True)),
                ('email1', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('email2', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('fax', models.CharField(blank=True, max_length=40, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=40, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number1', models.CharField(blank=True, max_length=40, null=True)),
                ('phone_number2', models.CharField(blank=True, max_length=40, null=True)),
                ('credit_limit', models.FloatField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'client',
                'ordering': ['client_nbr'],
            },
        ),
        migrations.CreateModel(
            name='Client_contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'client_contact',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name_fr', models.CharField(max_length=200, unique=True)),
                ('country_name_en', models.CharField(max_length=200, unique=True)),
                ('abbreviation', models.CharField(max_length=4, unique=True)),
            ],
            options={
                'db_table': 'country',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'currency',
            },
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'destination',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=100, unique=True)),
                ('language_code', models.CharField(max_length=4, unique=True)),
            ],
            options={
                'db_table': 'language',
            },
        ),
        migrations.CreateModel(
            name='Local_contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('fax', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'local_contact',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'payment',
            },
        ),
        migrations.CreateModel(
            name='Representative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('fax', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'representative',
            },
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'shipping',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_nbr', models.CharField(max_length=30, null=True)),
                ('supplier_name', models.CharField(max_length=150, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=40, null=True)),
                ('fax', models.CharField(blank=True, max_length=40, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('website', models.URLField(blank=True, max_length=150, null=True)),
                ('delivery_type', models.CharField(blank=True, max_length=100, null=True)),
                ('comment', models.TextField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='project.country')),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='project.language')),
            ],
            options={
                'db_table': 'supplier',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='TimeUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'time_unit',
            },
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'transport',
            },
        ),
        migrations.CreateModel(
            name='Supplier_contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('supplier', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='project.supplier')),
            ],
            options={
                'db_table': 'supplier_contact',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_nbr', models.CharField(max_length=30, unique=True)),
                ('project_name', models.CharField(max_length=150, null=True)),
                ('our_ref', models.CharField(max_length=50, null=True)),
                ('client_ref', models.CharField(blank=True, max_length=50, null=True)),
                ('project_description', models.TextField(blank=True, max_length=500, null=True)),
                ('to_do', models.TextField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project.client')),
                ('client_contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='project.client_contact')),
                ('local_contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='project.local_contact')),
            ],
            options={
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='project_files/')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
            options={
                'db_table': 'file',
            },
        ),
        migrations.AddField(
            model_name='client',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='project.country'),
        ),
        migrations.AddField(
            model_name='client',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='project.language'),
        ),
        migrations.AddField(
            model_name='client',
            name='representative',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='project.representative'),
        ),
    ]
