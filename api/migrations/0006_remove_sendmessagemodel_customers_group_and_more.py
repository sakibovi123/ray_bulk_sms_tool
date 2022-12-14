# Generated by Django 4.1.3 on 2022-11-16 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_customer_country_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sendmessagemodel',
            name='customers',
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(max_length=255)),
                ('customers', models.ManyToManyField(to='api.customer')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='sendmessagemodel',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.group'),
        ),
    ]
