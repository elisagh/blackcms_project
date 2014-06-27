# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='autor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1, to_field='id'),
            preserve_default=False,
        ),
    ]
