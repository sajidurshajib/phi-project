from django.db import models
from django.utils.text import slugify
from datetime import datetime
from tinymce.models import HTMLField
import os
import uuid

def upload_to(instance, filename):
    base, ext = os.path.splitext(filename)
    return f'projects/{instance.slug}-{uuid.uuid4()}-{ext}'


class Projects(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = HTMLField()
    status = models.TextField(default='')
    start_date = models.DateField(default=datetime.now)    
    end_date = models.DateField(default=datetime.now)
    pdfUpload = models.FileField(upload_to=upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Generate slug if it doesn't exist or title has changed
        if not self.slug or (self.pk and self.title != Projects.objects.get(pk=self.pk).title):
            self.slug = slugify(self.title)
            counter = 1
            new_slug = self.slug
            
            while Projects.objects.filter(slug=new_slug).exists():
                new_slug = f"{self.slug}-{counter}"
                counter += 1
            self.slug = new_slug

    def __str__(self):
        return self.title
