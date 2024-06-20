from django.contrib import admin
from django.contrib.admin import ModelAdmin
from inflows.models import Inflow


@admin.register(Inflow)
class InflowAdmin(ModelAdmin):
    list_display = ('supplier', 'product', 'quantity', 'created_at', 'updated_at',)
    search_fields = ('supplier__name', 'product__title',)
