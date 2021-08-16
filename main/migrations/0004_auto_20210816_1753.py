# Generated by Django 3.2.6 on 2021-08-16 22:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210816_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='curso_costo',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='curso',
            name='curso_publicado',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 16, 17, 53, 18, 274000), verbose_name='Fecha de publicación'),
        ),
    ]
