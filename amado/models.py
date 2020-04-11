import os

from django.conf import settings
from django.db import models
from django.utils.html import mark_safe
from django.conf.urls.static import static


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='prod_images')
    desc = models.CharField(max_length=500)
    price = models.FloatField()
    is_stock_available = models.BooleanField(default=True)

    def image_tag(self):
        print(self.img)
        return mark_safe('<img src="{}{}" width="48" height="48" />'.format(settings.MEDIA_URL, self.img))

    image_tag.allow_tags = True


class ProductImages(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    img_prod = models.ImageField(upload_to='prod_images')
