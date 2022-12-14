# Generated by Django 4.1.3 on 2022-11-15 17:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('country_code', models.CharField(max_length=255)),
                ('state_code', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='SendMessageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.contenttemplate')),
                ('customers', models.ManyToManyField(blank=True, to='api.customer')),
                ('number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.numbergroup')),
            ],
            options={
                'verbose_name': 'SendMessage',
                'verbose_name_plural': 'SendMessages',
                'ordering': ['-created_at'],
            },
        ),
    ]
