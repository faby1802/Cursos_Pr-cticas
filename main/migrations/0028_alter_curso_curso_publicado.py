# Generated by Django 3.2.6 on 2021-08-25 21:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_alter_curso_curso_publicado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='curso_publicado',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 25, 16, 21, 13, 656065), verbose_name='Fecha de publicación'),
        ),
    ]