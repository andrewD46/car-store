# Generated by Django 3.0.6 on 2020-05-31 19:04

import ads.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_auto_20200531_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='image',
            field=models.ImageField(upload_to=ads.models.get_image_filename, verbose_name='Image'),
        ),
    ]