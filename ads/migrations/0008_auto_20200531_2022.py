# Generated by Django 3.0.6 on 2020-05-31 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0007_auto_20200531_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='image',
            field=models.ImageField(default='', upload_to='img', verbose_name='Image'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Photos',
        ),
    ]
