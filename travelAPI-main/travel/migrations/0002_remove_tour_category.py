# Generated by Django 5.1.2 on 2024-10-11 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='category',
        ),
    ]
