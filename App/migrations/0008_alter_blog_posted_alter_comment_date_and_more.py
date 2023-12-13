# Generated by Django 4.2.6 on 2023-12-12 20:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_remove_orders_description_remove_orders_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 12, 12, 23, 16, 59, 707639), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 12, 12, 23, 16, 59, 708640), verbose_name='Дата комментария'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 12, 12, 23, 16, 59, 709637), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 12, 12, 23, 16, 59, 708640), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 12, 12, 23, 16, 59, 708640), verbose_name='Опубликована'),
        ),
    ]