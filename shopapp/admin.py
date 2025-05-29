from django.contrib import admin
from . models import *

class CatagoryAdmin(admin.ModelAdmin):
   list_display = ('name', 'description')

class ProductAdmin(admin.ModelAdmin):
   list_display = ('name', 'catagory', 'rating', 'quantity', 'original_price', 'selling_price')

admin.site.register(Catagory, CatagoryAdmin)
admin.site.register(Product, ProductAdmin)