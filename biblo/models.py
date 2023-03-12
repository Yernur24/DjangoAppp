from django.db import models
from django.urls import reverse


class Product(models.Model):
    product_id=models.IntegerField
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to="photos/%Y/%m/%d/")
    content=models.TextField(blank=True)
    author=models.TextField(blank=True)
    price=models.IntegerField
    cat=models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
      return reverse('post', kwargs={'post_id': self.pk})

class Category(models.Model):
    name=models.CharField(max_length=255, db_index=True)
    def __str__(self):
          return self.name

    def get_absolute_url(self):
      return reverse('category', kwargs={'cat_id': self.pk})