from django.contrib import admin
from django.contrib.admin import ModelAdmin
from products.models import Product


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('title', 'serie_number',)
    search_fields = ('title',)
