# Generated by Django 3.0.6 on 2020-05-28 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_auto_20200528_1506'),
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CarModel',
        ),
    ]