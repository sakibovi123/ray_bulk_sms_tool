# Generated by Django 4.1.3 on 2022-11-16 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_sendmessagemodel_customers_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenttemplate',
            name='content',
            field=models.TextField(max_length=255),
        ),
    ]
