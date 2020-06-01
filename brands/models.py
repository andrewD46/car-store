from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'

    def __str__(self):
        return self.name


class CarType(models.Model):
    car_type = models.CharField(max_length=100, db_index=True, unique=True)

    class Meta:
        ordering = ('car_type',)
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return f"{self.car_type}"
