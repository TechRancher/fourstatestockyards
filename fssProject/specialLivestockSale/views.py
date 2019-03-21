from django.shortcuts import render
from .models import SpecialLivestockSale


def special_livestock_sale(request):
    specialSale = SpecialLivestockSale.objects.filter(is_published=True)

    content = {
        'specialSale': specialSale
    }

    return render(request, 'specialSales.html', content)
