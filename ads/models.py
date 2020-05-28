from django.db import models
from brands.models import Brand
from users.models import User


class Ad(models.Model):
    brand = models.ForeignKey(Brand, related_name='brand', on_delete=models.CASCADE)
    car_model = models.CharField(max_length=200)
    year = models.CharField(max_length=4)
    equipment = models.CharField(max_length=200)
    mileage = models.CharField(max_length=8)
    capacity = models.CharField(max_length=5)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    # phone = models.ForeignKey(User.phone, related_name='phone', on_delete=models.CASCADE)

    class Meta:
        ordering = ('brand',)
        # index_together = (('id', 'slug'),)
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return f"{self.car_model} ({self.author})"

    def __unicode__(self):
        return self.photo


class Photos(models.Model):
    ad = models.ForeignKey(Ad, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="img")
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = 'create_at'
        ordering = ['create_at']
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return f"{self.ad.car_model} ({self.ad.author}) photo"
