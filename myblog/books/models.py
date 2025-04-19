import datetime
from django.db import models
from django.urls import reverse
from authapp.models import User
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Books(models.Model):
    covert_page = models.ImageField(upload_to='books_covert/')
    file = models.FileField(upload_to='pdf_books/', blank=True, null=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    date_add = models.DateField(auto_now_add=True)
    synopsis = RichTextField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title
    
    def get_file_url(self):
        return self.file.url if self.file else None
    
    def get_absolute_url(self):
        return reverse("booksdetails", kwargs={"pk": self.pk})
    