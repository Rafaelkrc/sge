# Generated by Django 5.0.6 on 2024-11-23 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outflows', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='outflows',
            old_name='descriptio',
            new_name='description',
        ),
    ]
