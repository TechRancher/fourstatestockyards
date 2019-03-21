from django.contrib import admin
from .models import LivestockReport


class LivestockAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_Livestock', 'market_Date',
                    'head_Count', 'livestock_weight', 'high_price', 'low_price', 'remarks')
    list_display_links = ('id', 'type_Livestock')
    list_filter = ('market_Date', 'type_Livestock')
    search_fields = ('market_Date', 'type_Livestock',
                     'livestock_weight', 'hight_price', 'low_price', 'remarks')
    list_per_page = 50


admin.site.register(LivestockReport, LivestockAdmin)
