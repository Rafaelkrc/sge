from django.contrib import admin
from django.contrib.admin import ModelAdmin
from suppliers.models import Supplier


@admin.register(Supplier)
class SupplierAdmin(ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name',)
