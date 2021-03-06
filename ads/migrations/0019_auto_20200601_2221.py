# Generated by Django 3.0.6 on 2020-06-01 19:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0018_auto_20200601_1859'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'ordering': ('-created_at',), 'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterField(
            model_name='ad',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
