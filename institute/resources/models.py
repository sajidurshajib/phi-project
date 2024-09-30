from django.db import models
from django.utils.text import slugify
import os
import uuid

def upload_to(instance, filename):
    base, ext = os.path.splitext(filename)
    return f'resources/{instance.slug}-{uuid.uuid4()}-{ext}'


class Resources(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    pdfUpload = models.FileField(upload_to=upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Resources, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
