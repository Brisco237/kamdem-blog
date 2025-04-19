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


class Articles(models.Model):
    image = models.ImageField(upload_to='images_articles/')
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now=True)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def get_absolute_url(self):
        return reverse("articlesdetails", kwargs={"pk": self.pk})
    

class Comments(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='commentaires')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Un commentaire de {self.article.author } sur l'article: {self.article.title} de la categorie :{self.article.category} le {self.article.date} a {self.article.time}"
    
    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'