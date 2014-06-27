# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('slug', models.SlugField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=30)),
                ('slug', models.SlugField()),
                ('contenido', models.TextField()),
                ('imagen', models.ImageField(upload_to=b'fotos_articulos')),
                ('categoria', models.ManyToManyField(to='articulos.Categoria')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
