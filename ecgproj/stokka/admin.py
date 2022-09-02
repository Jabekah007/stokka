from django.contrib import admin
from .models import Inventory,Asset_location


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['Asset_Type','Asset_Name','asset_location','Asset_Model','Serial_No']
    search_fields= ['Asset_Type','Asset_Name','asset_location','Asset_Model','Serial_No']

admin.site.register(Inventory,ProductAdmin)
admin.site.register(Asset_location)
