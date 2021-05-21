from django.contrib import admin
from home.models import UrlModel

@admin.register(UrlModel)
class clipBoardAdmin(admin.ModelAdmin):
    list_display = ['main_url','short_url','date']
