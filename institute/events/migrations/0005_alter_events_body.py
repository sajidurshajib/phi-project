# Generated by Django 5.0.1 on 2024-09-28 21:19

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_events_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
    ]
