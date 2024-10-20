# Generated by Django 5.0.1 on 2024-10-02 22:33

import tinymce.models
import trainings.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', tinymce.models.HTMLField()),
                ('pdfUpload', models.FileField(upload_to=trainings.models.upload_to)),
                ('image', models.ImageField(blank=True, null=True, upload_to='trainings_image/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
