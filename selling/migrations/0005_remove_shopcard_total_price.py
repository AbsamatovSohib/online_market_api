# Generated by Django 4.2.6 on 2023-10-24 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selling', '0004_alter_shopcard_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopcard',
            name='total_price',
        ),
    ]
