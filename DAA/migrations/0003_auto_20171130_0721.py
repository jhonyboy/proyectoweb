# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DAA', '0002_auto_20171129_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='image',
            field=models.ImageField(default='../static/user.png', null=True, upload_to='perfil_DAA/', blank=True),
        ),
    ]
