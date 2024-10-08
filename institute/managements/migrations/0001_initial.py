# Generated by Django 5.0.1 on 2024-09-28 21:19

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Managements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('position', models.CharField(max_length=100)),
                ('detail', tinymce.models.HTMLField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='management_images/')),
            ],
        ),
    ]
