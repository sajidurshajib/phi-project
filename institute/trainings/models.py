from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import os
import uuid


def optimize_and_convert_to_jpeg(image):
    img = Image.open(image)

    max_size = 1024 * 1024  # Max size in bytes
    quality = 100
    buffer = BytesIO()

    # Save image to buffer first, then check size
    img.save(buffer, format='JPEG', quality=quality)
    buffer.seek(0)

    if buffer.tell() <= max_size:
        return InMemoryUploadedFile(buffer, None, f"{uuid.uuid4()}.jpeg", 'image/jpeg', buffer.getbuffer().nbytes, None)

    while True:
        buffer = BytesIO()
        img.save(buffer, format='JPEG', quality=quality)
        buffer.seek(0)

        if buffer.tell() <= max_size or quality <= 50:
            break
        quality -= 5

    return InMemoryUploadedFile(buffer, None, f"{uuid.uuid4()}.jpeg", 'image/jpeg', buffer.getbuffer().nbytes, None)


def upload_to(instance, filename):
    base, ext = os.path.splitext(filename)
    return f'trainings_doc/{instance.slug}-{uuid.uuid4()}{ext}'


class Trainings(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = HTMLField()
    pdfUpload = models.FileField(upload_to=upload_to)
    image = models.ImageField(upload_to='trainings_image/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Generate slug if it doesn't exist or title has changed
        if not self.slug or (self.pk and self.title != Trainings.objects.get(pk=self.pk).title):
            self.slug = slugify(self.title)
            counter = 1
            new_slug = self.slug
            
            while Trainings.objects.filter(slug=new_slug).exists():
                new_slug = f"{self.slug}-{counter}"
                counter += 1
            self.slug = new_slug

        # Optimize image if present
        if self.image:
            self.image = optimize_and_convert_to_jpeg(self.image)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
