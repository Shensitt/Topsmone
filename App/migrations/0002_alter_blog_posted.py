# Generated by Django 4.2.6 on 2023-12-02 11:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 12, 2, 14, 21, 39, 603582), verbose_name='Опубликована'),
        ),
    ]
