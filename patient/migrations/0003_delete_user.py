# Generated by Django 4.2.7 on 2023-11-23 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
