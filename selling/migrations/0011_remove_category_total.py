# Generated by Django 4.2.6 on 2023-10-25 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selling', '0010_alter_category_id_alter_customer_id_alter_items_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='total',
        ),
    ]