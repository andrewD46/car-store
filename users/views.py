from django.contrib.auth import login, authenticate, logout
from django.core.exceptions import NON_FIELD_ERRORS
from django.http import Http404
from django.shortcuts import render, redirect

from ads.models import Ad
from users.form import RegistrationForm, LoginForm
from users.models import User


def register(request):
    if request.method == 'GET':
        ads = Ad.objects.all()
        form = RegistrationForm()
        return render(request, 'register.html', context={
            "form": form,
            'ads': ads,
        })

    elif request.method == 'POST':
        ads = Ad.objects.all()
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.send_verification_email()
            login(request, user)
            return render(request, 'register_success.html', context={
                "ads": ads
            })
        else:
            return render(request, 'register.html', context={
                "form": form,
                "ads": ads
            })


def verify(request):
    user = request.user
    data = request.GET
    if user.is_token_correct(data['token']):
        user.verify_email()
        return render(request, 'email_verified.html')
    else:
        return Http404("Non found")


def login_user(request):
    ads = Ad.objects.all()
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', context={
            'form': form,
            'ads': ads,
        })
    elif request.method == 'POST':
        ads = Ad.objects.all()
        form = LoginForm(request.POST)
        form.is_valid()
        user = form.get_user(request)
        if user:
            login(request, user)
            return redirect("/")
        else:
            form.errors[NON_FIELD_ERRORS] = 'Cannot perform login with this credentials'
            return render(request, "login.html", context={
                'form': form,
                "ads": ads
            })


def logout_user(request):
    logout(request)
    return redirect("/")
