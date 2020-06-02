from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone

from brands.models import Brand, CarType
from users.models import User
from django.urls import reverse


class Ad(models.Model):
    brand = models.ForeignKey(Brand, related_name='brand', on_delete=models.CASCADE)
    car_model = models.CharField(max_length=200)
    car_type = models.ForeignKey(CarType, related_name='type', on_delete=models.CASCADE)
    year = models.CharField(max_length=4)
    equipment = models.CharField(max_length=200)
    mileage = models.CharField(max_length=8)
    price = models.CharField(max_length=20)
    available = models.BooleanField(default=True)
    description = models.TextField()
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="img", blank=False, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    # author_first_name = models.ForeignKey(User, related_name='author_first_name', on_delete=models.CASCADE)
    # phone = models.ForeignKey(User.phone, related_name='phone', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return f"{self.car_model} ({self.author})"


def get_image_filename(instance, filename):
    pass


# class Photos(models.Model):
#     ad = models.ForeignKey(Ad, related_name='photos', on_delete=models.CASCADE)
#     image = models.ImageField(upload_to=get_image_filename,
#                               verbose_name='Image')
#     # create_at = models.DateTimeField(auto_now_add=True)
#     #
#     # class Meta:
#     #     get_latest_by = 'create_at'
#     #     ordering = ['create_at']
#     #     verbose_name = 'Фотография'
#     #     verbose_name_plural = 'Фотографии'
#     #
#     # def __str__(self):
#     #     return f"{self.ad.car_model} ({self.ad.author}) photo"
