# Generated by Django 3.2.6 on 2021-08-26 22:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_auto_20210826_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='curso_publicado',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 26, 17, 36, 45, 456772), verbose_name='Fecha de publicación'),
        ),
    ]