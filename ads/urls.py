from django.urls import path
from ads import views


urlpatterns = [
    path('', views.all_ads),
    path('create/', views.create),
    path('delete/<int:id>/', views.delete),
    path('<int:id>/', views.retrieve),
]
