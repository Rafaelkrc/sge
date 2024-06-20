from django.contrib import admin
from django.contrib.admin import ModelAdmin
from outflows.models import Outflows


@admin.register(Outflows)
class OutflowsAdmin(ModelAdmin):
    list_display = ('product', 'quantity', 'created_at', 'updated_at',)
    search_fields = ('product__title',)
