from django.db import models

# Create your models here.

class GalleryImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery_images/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
