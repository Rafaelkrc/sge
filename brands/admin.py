from django.contrib import admin
from django.contrib.admin import ModelAdmin
from brands.models import Brand


@admin.register(Brand)
class BrandAdmin(ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name',)
    ordering = ('name',)
