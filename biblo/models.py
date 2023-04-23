from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Product(models.Model):
    product_id=models.IntegerField
    name=models.CharField(max_length=255, verbose_name="title")
    slug=models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    image=models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="image")
    content=models.TextField(blank=True, verbose_name="content")
    author=models.TextField(blank=True, verbose_name="author")
    price=models.IntegerField
    is_published =models.BooleanField(default=True, verbose_name="publicasia")
    cat=models.ForeignKey('Category', on_delete=models.PROTECT,verbose_name="Категории")
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering =['id']

class Category(models.Model):
    name=models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    def __str__(self):
          return self.name

    def get_absolute_url(self):
      return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'