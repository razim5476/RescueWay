# Generated by Django 5.1.1 on 2024-10-11 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disaster_management', '0005_alert_is_active_customeuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomeUSer',
        ),
    ]
