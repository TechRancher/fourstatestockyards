from django.shortcuts import render


def index(request, *args, **kwargs):
    return render(request, "home.html", {})


def contactRep_view(request, *args, **kwargs):
    return render(request, "contactRep.html", {})


def salesInfo_view(request, *args, **kwargs):
    return render(request, "salesInfo.html", {})


def otherMarket_view(request, *args, **kwargs):
    return render(request, "otherMarkets.html", {})


def contactUs_view(request, *args, **kwargs):
    return render(request, "contactUs.html", {})


def facility_view(request, *args, **kwargs):
    return render(request, "facility.html", {})


def info_view(request, *args, **kwargs):
    return render(request, "info.html", {})
