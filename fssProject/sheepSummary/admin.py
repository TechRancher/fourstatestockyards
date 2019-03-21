from django.contrib import admin
from .models import SheepSummary


class SheepSummaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'sale_type', 'sale_date',
                    'receipts', 'is_published')
    list_display_links = ('id', 'sale_type')
    list_editable = ('is_published',)
    list_filter = ('sale_date', 'receipts')
    search_fields = ('sale_date', 'sale_decription',
                     'receipts', 'sale_type')
    list_per_page = 50


admin.site.register(SheepSummary, SheepSummaryAdmin)
