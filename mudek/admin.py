from django.contrib import admin
from .models import MudekDocument

class DocumentAdmin(admin.ModelAdmin):
    list_display = ['lesson','publishing_date']
    list_display_links=['lesson', 'publishing_date']
    list_filter=['publishing_date']
    search_fields = ["lesson"]



admin.site.register(MudekDocument, DocumentAdmin)