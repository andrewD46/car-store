from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'

    def __str__(self):
        return self.name


# class CarModel(models.Model):
#     parent_brand = models.ForeignKey(Brand, related_name='brands', on_delete=models.CASCADE)
#     car_model = models.CharField(max_length=30)
#
#     class Meta:
#         ordering = ('car_model',)
#         verbose_name = 'Модель'
#         verbose_name_plural = 'Модели'
#
#     def __str__(self):
#         return f"{self.parent_brand.name} {self.car_model}"
