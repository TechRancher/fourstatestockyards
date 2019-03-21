from django.contrib import admin
from .models import LivestockSummary


class LivestockSummaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'sale_type', 'sale_date',
                    'receipts', 'is_published')
    list_display_links = ('id', 'sale_type')
    list_filter = ('sale_date', 'receipts')
    list_editable = ('is_published',)
    search_fields = ('sale_date', 'sale_decription',
                     'receipts', 'sale_type')
    list_per_page = 50


admin.site.register(LivestockSummary, LivestockSummaryAdmin)
