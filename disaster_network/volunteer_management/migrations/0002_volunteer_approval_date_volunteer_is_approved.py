# Generated by Django 5.1.1 on 2024-10-13 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='approval_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='is_approved',
            field=models.BooleanField(default=True),
        ),
    ]
