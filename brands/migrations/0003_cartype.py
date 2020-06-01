# Generated by Django 3.0.6 on 2020-06-01 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0002_delete_carmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_type', models.CharField(db_index=True, max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
                'ordering': ('car_type',),
            },
        ),
    ]