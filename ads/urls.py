from django.urls import path
from ads import views


urlpatterns = [
    path('create/', views.create),
]
