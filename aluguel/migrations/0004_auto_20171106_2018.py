# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluguel', '0003_auto_20171106_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluguel',
            name='valor',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='aluguel',
            name='imagem',
            field=models.ImageField(upload_to='aluguel/'),
        ),
    ]
