from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET

from django.conf import settings
from ads.models import Ad


@require_GET
def main(request):
    # query = request.GET.get("q", "")
    page = request.GET.get("page", 1)
    ads = Ad.objects.filter().order_by("-created_at")

    p = Paginator(ads, settings.ITEMS_PER_PAGE)
    return render(request, 'main.html', context={
        'page': p.page(page)
    })


def about(request):
    return render(request, 'about.html')
