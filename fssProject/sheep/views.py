from django.shortcuts import render
from sheep.models import SheepReport
from datetime import date, timedelta
from sheepSummary.models import SheepSummary


def sheep_report(request):
    today = date.today()
    lastMonth = today - timedelta(30)

    sheepstock = SheepReport.objects.order_by('type_Livestock').filter(
        market_Date__gte=lastMonth, market_Date__lte=date.today())
    summarySheep = SheepSummary.objects.filter(is_published=True).filter(
        sale_date__gte=lastMonth, sale_date__lte=date.today())

    content = {
        'sheepstock': sheepstock,
        'summarySheep': summarySheep
    }
    return render(request, 'sheepReport.html', content)
