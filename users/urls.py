from django.urls import path
from users import views


urlpatterns = [
    path('register/', views.register),
    path('verify/', views.verify),
    path('login/', views.login_user),
    path('logout/', views.logout_user),
]