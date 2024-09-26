from django.db import models
from django.utils.text import slugify
from datetime import datetime

class Events(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    body = models.TextField()
    date = models.DateField(default=datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug or (self.pk and self.name != Events.objects.get(pk=self.pk).name):
            self.slug = slugify(self.name)
            counter = 1
            new_slug = self.slug
            
            while Events.objects.filter(slug=new_slug).exists():
                new_slug = f"{self.slug}-{counter}"
                counter += 1
            self.slug = new_slug
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name