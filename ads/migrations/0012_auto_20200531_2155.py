# Generated by Django 3.0.6 on 2020-05-31 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0011_ad_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='capacity',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.ImageField(null=True, upload_to='img'),
        ),
    ]
