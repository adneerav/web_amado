import admin_thumbnails
from django.contrib import admin

from .models import Products, ProductImages


@admin_thumbnails.thumbnail('img')
class AdminProduct(admin.ModelAdmin):
    model = Products
    list_display = ['name', 'price', 'image_tag']

    def get_name(self, obj):
        return obj.product.name

    get_name.admin_order_field = 'name'


class AdminProductImage(admin.ModelAdmin):
    model = Products
    list_display = ['get_name']

    def get_name(self, obj):
        print(obj.product.name)
        return obj.product.name


admin.site.register(Products, AdminProduct)
admin.site.register(ProductImages, AdminProductImage)
# Register your models here.
