from django.db import models

class Product(models.Model):
    product_id=models.IntegerField
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to="photos/%Y/%m/%d/")
    content=models.TextField(blank=True)
    author=models.TextField(blank=True)
    price=models.IntegerField

