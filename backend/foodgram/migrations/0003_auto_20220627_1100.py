# Generated by Django 2.2.19 on 2022-06-27 11:00

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodgram', '0002_auto_20220621_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=colorfield.fields.ColorField(default='#49B64E', image_field=None, max_length=18, samples=None, verbose_name='HEX-цвет тега'),
        ),
    ]
