from django.http import HttpResponse
from django.shortcuts import render
from ads.models import Ad


def main(request):
    ads = Ad.objects.all()
    return render(request, 'main.html', context={
        'ads': ads
    })
