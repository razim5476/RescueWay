# Generated by Django 5.1.1 on 2024-10-10 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disaster_management', '0003_remove_disaster_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='disaster',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
