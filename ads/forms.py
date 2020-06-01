from django import forms
from ads.models import Ad


class AdForm(forms.ModelForm):

    class Meta:
        model = Ad
        exclude = [
            'available',
            'author',
            'created_at',
        ]

        widgets = {
            'description': forms.Textarea(attrs={'rows': '3'}),
        }

        labels = {
            'brand': 'Марка',
            'car_model': 'Модель',
            'car_type': 'Тип двигателя',
            'year': 'Год выпуска',
            'equipment': 'Комплектация',
            'mileage': 'Пробег (км)',
            'capacity': 'Емкость аккумулятора (кВт•ч)',
            'price': 'Цена (USD)',
            'description': 'Описание',
            'image': 'Выберите фото',
        }

#
# class PhotoForm(forms.ModelForm):

    # class Meta:
    #     model = Photos
    #     fields = [
    #         'image',
    #     ]
    #
    #     widgets = {
    #         'brand': forms.TextInput(attrs={'class': 'form-control'}),
    #         'car_model': forms.TextInput(attrs={'class': 'form-control'}),
    #         'year': forms.NumberInput(attrs={'class': 'form-control'}),
    #         'equipment': forms.TextInput(attrs={'class': 'form-control'}),
    #         'mileage': forms.NumberInput(attrs={'class': 'form-control'}),
    #         'capacity': forms.NumberInput(attrs={'class': 'form-control'}),
    #         'price': forms.NumberInput(attrs={'class': 'form-control'}),
    #         'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
    #     }
    #
    #     labels = {
    #         'brand': 'Марка',
    #         'car_model': 'Модель',
    #         'year': 'Год выпуска',
    #         'equipment': 'Комплектация',
    #         'mileage': 'Пробег (км)',
    #         'capacity': 'Емкость аккумулятора (кВт•ч)',
    #         'price': 'Цена (USD)',
    #         'description': 'Описание',
    #     }