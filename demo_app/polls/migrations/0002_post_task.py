# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=64, verbose_name=b'title')),
                ('slug', models.SlugField(max_length=64)),
                ('content', models.TextField(verbose_name=b'content')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
            options={
                'get_latest_by': 'created_at',
                'permissions': (('view_post', 'Can view post'),),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('summary', models.CharField(max_length=32)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('reported_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('view_task', 'View task'),),
            },
            bases=(models.Model,),
        ),
    ]
