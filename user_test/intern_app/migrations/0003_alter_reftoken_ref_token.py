# Generated by Django 4.2.8 on 2024-04-11 15:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('intern_app', '0002_reftoken_delete_refcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reftoken',
            name='ref_token',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
