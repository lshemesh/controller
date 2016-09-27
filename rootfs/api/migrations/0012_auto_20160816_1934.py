# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-16 19:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0011_auto_20160810_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppSettings',
            fields=[
                ('uuid', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='UUID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('maintenance', models.NullBooleanField(default=None)),
                ('routable', models.NullBooleanField(default=None)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.App')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'created',
                'ordering': ['-created'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='appsettings',
            unique_together=set([('app', 'uuid')]),
        ),
    ]