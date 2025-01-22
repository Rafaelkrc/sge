from django.contrib import admin
from ai import models


@admin.register(models.AIResult)
class AIResultAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'result')
