# Generated by Django 4.2.6 on 2023-10-24 05:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('selling', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1fbefd1e-c425-4cad-8e0f-a04efa575266'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.UUIDField(default=uuid.UUID('c82a108d-2622-449a-b7e6-ba8f5f06bf91'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='items',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1cda359d-0ac2-45d2-a314-7d10e84efa06'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.UUID('42bb9c4f-eb92-4e4c-827a-9d2a7c9b571e'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='shopcard',
            name='id',
            field=models.UUIDField(default=uuid.UUID('23910f46-8022-4447-86ad-19dcc00afcd6'), editable=False, primary_key=True, serialize=False),
        ),
    ]
