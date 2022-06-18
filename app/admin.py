from django.contrib import admin
from .models import Currency


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ["value", "currency", "nation", "count", "updated"]


admin.site.register(Currency, CurrencyAdmin)
