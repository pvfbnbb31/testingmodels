# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import memoraid.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=200, validators=[memoraid.validators.not_unauthorized_word])),
                ('votes', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Memoraid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('memoraid_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published', validators=[memoraid.validators.not_future])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='choice',
            name='memoraid',
            field=models.ForeignKey(to='memoraid.Memoraid'),
            preserve_default=True,
        ),
    ]
