from django.contrib import admin
from django.contrib.admin import ModelAdmin
from categories.models import Category


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name',)
