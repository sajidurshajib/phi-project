# Generated by Django 5.0.1 on 2024-09-28 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_rename_event_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='address',
            field=models.TextField(default=''),
        ),
    ]
