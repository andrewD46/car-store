from django.urls import path
from ads import views
# from ads.views import AdView


urlpatterns = [
    path('', views.all_ads),
    # path('', AdView.as_view(template_name='ads.html')),
    path('create/', views.create),
    path('delete/<int:id>/', views.delete),
    path('<int:id>/', views.retrieve),
]
