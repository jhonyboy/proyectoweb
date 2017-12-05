# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DAA', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='image',
            field=models.ImageField(default='../static/user.png', null=True, upload_to='perfil_FaceRay/', blank=True),
        ),
    ]
