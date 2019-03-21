from django.shortcuts import render
from .models import LivestockReport
from sheep.models import SheepReport
from livestockSummary.models import LivestockSummary
from sheepSummary.models import SheepSummary
from datetime import date, timedelta


def livestock_report(request):
    today = date.today()
    dayLess7 = today - timedelta(7)
    lastMonth = today - timedelta(30)
    livestock = LivestockReport.objects.order_by('type_Livestock').filter(
        market_Date__gte=dayLess7, market_Date__lte=date.today())
    summaryReport = LivestockSummary.objects.filter(is_published=True).filter(
        sale_date__gte=dayLess7, sale_date__lte=date.today())
    sheepstock = SheepReport.objects.order_by('type_Livestock').filter(
        market_Date__gte=lastMonth, market_Date__lte=date.today())
    summarySheep = SheepSummary.objects.filter(is_published=True).filter(
        sale_date__gte=lastMonth, sale_date__lte=date.today())

    content = {
        'livestock': livestock,
        'summaryReport': summaryReport,
        'sheepstock': sheepstock,
        'summarySheep': summarySheep
    }
    return render(request, 'livestockReport.html', content)


