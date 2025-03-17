from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=75)
    author = models.CharField(max_length=75)
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(upload_to='banners/', default='default_book.jpg', blank = True)

    def __str__(self):
        return self.title