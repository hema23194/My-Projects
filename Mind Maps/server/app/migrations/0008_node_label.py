# Generated by Django 3.1.4 on 2024-01-15 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20240111_0445'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='label',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
