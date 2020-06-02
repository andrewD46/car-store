from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.core.exceptions import NON_FIELD_ERRORS
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect

from ads.models import Ad
from users.form import RegistrationForm, LoginForm
from users.models import User


def register(request):
    page = request.GET.get("page", 1)
    ads = Ad.objects.filter().order_by("-created_at")
    p = Paginator(ads, settings.ITEMS_PER_PAGE)
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'register.html', context={
            "form": form,
            'page': p.page(page)
        })

    elif request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.send_verification_email()
            login(request, user)
            return render(request, 'register_success.html', context={
                'page': p.page(page)
            })
        else:
            return render(request, 'register.html', context={
                "form": form,
                'page': p.page(page)
            })


def verify(request):
    page = request.GET.get("page", 1)
    ads = Ad.objects.filter().order_by("-created_at")
    p = Paginator(ads, settings.ITEMS_PER_PAGE)
    user = request.user
    data = request.GET
    if user.is_token_correct(data['token']):
        user.verify_email()
        return render(request, 'email_verified.html', context={
            'page': p.page(page),
        })
    else:
        return Http404("Non found")


def login_user(request):
    page = request.GET.get("page", 1)
    ads = Ad.objects.filter().order_by("-created_at")
    p = Paginator(ads, settings.ITEMS_PER_PAGE)
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', context={
            'form': form,
            'page': p.page(page),
        })
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        form.is_valid()
        user = form.get_user(request)
        if user:
            login(request, user)
            return redirect("/")
        else:
            form.errors[NON_FIELD_ERRORS] = form.error_class(['Невозможно выполнить вход с этими учетными данными'])
            return render(request, "login.html", context={
                'form': form,
                'page': p.page(page),
            })


def logout_user(request):
    logout(request)
    return redirect("/")
