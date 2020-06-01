from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

from ads.forms import AdForm
from ads.models import Ad
from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
from django.forms import formset_factory, modelformset_factory

from users.models import User


def create(request):
    if request.method == 'GET':
        ads = Ad.objects.all()
        form = AdForm()
        return render(request, 'create.html', context={
            "form": form,
            'ads': ads,
        })
    elif request.method == 'POST':
        ads = Ad.objects.all()
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user
            form.save()
            return render(request, 'create_success.html', context={
                "ads": ads
            })
        else:
            return render(request, 'create.html', context={
                "form": form,
                "ads": ads
            })


def all_ads(request):
    if request.method == 'GET':
        ads = Ad.objects.all()
        return render(request, 'ads.html', context={
            'ads': ads,
        })


def retrieve(request, id=None):
    ad = Ad.objects.get(pk=id)
    return render(request, 'retrieve.html', context={
        'ad': ad,
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
