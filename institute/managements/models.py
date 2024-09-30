import uuid
from django.db import models
from django.utils.text import slugify
from PIL import Image
from io import BytesIO
from tinymce.models import HTMLField
from django.core.files.uploadedfile import InMemoryUploadedFile


def optimize_and_convert_to_jpeg(image):
    img = Image.open(image)

    max_size = 1024 * 1024  # Max size in bytes
    quality = 100
    buffer = BytesIO()

    if buffer.tell() <= max_size:
        img.save(buffer, format='JPEG', quality=quality)
        buffer.seek(0)
        return InMemoryUploadedFile(buffer, None, f"{uuid.uuid4()}.jpeg", 'image/jpeg', buffer.getbuffer().nbytes, None)
    
    while True:
        buffer = BytesIO()
        img.save(buffer, format='JPEG', quality=quality)
        if buffer.tell() <= max_size or quality <= 50:
            break
        quality -= 5
        buffer.seek(0)
        img = Image.open(buffer)

    return InMemoryUploadedFile(buffer, None, f"{uuid.uuid4()}.jpeg", 'image/jpeg', buffer.getbuffer().nbytes, None)



class Managements(models.Model):
    name = models.CharField(max_length=100)  
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    position = models.CharField(max_length=100)
    detail = HTMLField()
    image = models.ImageField(upload_to='management_image/', blank=True, null=True)  
    priority = models.IntegerField(default=0) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Generate slug if it doesn't exist or name has changed
        if not self.slug or (self.pk and self.name != Managements.objects.get(pk=self.pk).name):
            self.slug = slugify(self.name)
            counter = 1
            new_slug = self.slug
            
            while Managements.objects.filter(slug=new_slug).exists():
                new_slug = f"{self.slug}-{counter}"
                counter += 1
            self.slug = new_slug

        # Optimize image and rename using UUID
        if self.image:
            self.image = optimize_and_convert_to_jpeg(self.image)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.position}"
