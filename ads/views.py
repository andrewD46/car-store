from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

from ads.forms import AdForm
from ads.models import Ad
from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
from django.forms import formset_factory, modelformset_factory

from django.conf import settings
from users.models import User


def create(request):
    page = request.GET.get("page", 1)
    ads = Ad.objects.filter().order_by("-created_at")
    p = Paginator(ads, settings.ITEMS_PER_PAGE)
    if request.method == 'GET':
        ads = Ad.objects.all()
        form = AdForm()
        return render(request, 'create.html', context={
            "form": form,
            'page': p.page(page),
        })
    elif request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user
            form.save()
            return render(request, 'create_success.html', context={
                'page': p.page(page),
            })
        else:
            return render(request, 'create.html', context={
                "form": form,
                'page': p.page(page),
            })


def all_ads(request):
    query = request.GET.get("q", "")
    page = request.GET.get("page", 1)
    ads = Ad.objects.filter(Q(brand__name__icontains=query) | Q(car_model__icontains=query)).order_by("-id")

    p = Paginator(ads, settings.ITEMS_PER_PAGE)
    return render(request, 'ads.html', context={
        'page': p.page(page)
    })
    # if request.method == 'GET':
    #     ads = Ad.objects.all()
    #     return render(request, 'ads.html', context={
    #         'ads': ads,
    #     })


def retrieve(request, id=None):
    ad = Ad.objects.get(pk=id)
    return render(request, 'retrieve.html', context={
        'ad': ad,
    })


def delete(request, id=None):
    page = request.GET.get("page", 1)
    ads = Ad.objects.filter().order_by("-created_at")
    p = Paginator(ads, settings.ITEMS_PER_PAGE)
    Ad.objects.filter(pk=id).delete()
    return render(request, 'delete_success.html', context={
            'page': p.page(page),
        })


# @login_required
# def create(request):
#     ImageFormSet = modelformset_factory(Photos, form=PhotoForm, extra=3)
#
#     if request.method == 'POST':
#
#         adForm = AdForm(request.POST)
#         formset = ImageFormSet(request.POST, request.FILES, queryset=Photos.objects.none())
#
#         if adForm.is_valid() and formset.is_valid():
#             ad_form = adForm.save(commit=False)
#             ad_form.author = request.user
#             ad_form.save()
#             # return HttpResponse(formset.cleaned_data)
#             for f in formset.cleaned_data:
#                 image = f['image']
#                 photo = Photos(ad=ad_form, image=image)
#                 photo.save()
#
#             # messages.success(request,
#             #                  "Yeeew, check it out on the home page!")
#             return HttpResponseRedirect("/")
#         else:
#             print(adForm.errors, formset.errors)
#     else:
#         adForm = AdForm()
#         formset = ImageFormSet(queryset=Photos.objects.none())
#     return render(request, 'create.html',
#                   {'adForm': adForm, 'formset': formset},
#                   context_instance=RequestContext(request))
# #
