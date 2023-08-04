from django.contrib import admin
from .models import *

# Register your models here.
class adminProduct(admin.ModelAdmin):
    list_display = ('product_name', 'product_quantity', 'product_price', 'product_description')

admin.site.register(Product, adminProduct)

class adminProduct_Image(admin.ModelAdmin):
    list_display = ('product_image', 'product')

admin.site.register(Product_Image, adminProduct_Image)
