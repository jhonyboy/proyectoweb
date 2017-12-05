# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField()),
                ('score', models.PositiveIntegerField(default=0, null=True, blank=True)),
                ('user', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(default='../static/user.png', null=True, upload_to='perfil_proyecto/', blank=True)),
                ('friends', models.ManyToManyField(related_name='friends_rel_+', to='DAA.Perfil', blank=True)),
                ('user_perfil', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('score', models.PositiveIntegerField(default=0, null=True, blank=True)),
                ('unscored', models.PositiveIntegerField(default=0, null=True, blank=True)),
                ('user', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='publication',
            field=models.ForeignKey(to='DAA.Publication'),
        ),
    ]
