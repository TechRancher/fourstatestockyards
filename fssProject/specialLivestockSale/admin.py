from django.contrib import admin
from .models import SpecialLivestockSale


class SpecialLivestockSaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'sale_type', 'sale_date',
                    'is_published', 'post_date')
    list_display_links = ('id', 'sale_type')
    list_filter = ('sale_type', 'sale_date', 'post_date')
    list_editable = ('is_published',)
    search_fields = ('id', 'sale_type', 'sale_date',
                     'sale_description', 'post_date')
    list_per_page = 50


admin.site.register(SpecialLivestockSale, SpecialLivestockSaleAdmin)
