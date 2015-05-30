# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import app.models
import django.utils.timezone
import taggit.managers
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Houseplant',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('common_name', models.CharField(max_length=100)),
                ('latin_name', models.CharField(null=True, blank=True, max_length=200)),
                ('slug', django_extensions.db.fields.AutoSlugField(populate_from=['common_name'], editable=False, blank=True, unique=True)),
                ('avatar', models.ImageField(upload_to=app.models.image_upload_to, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('care_notes', models.TextField(null=True, blank=True)),
                ('temperature', models.CharField(choices=[('cool', 'Cool (50-70 F)'), ('warm', 'Warm (60-85 F)'), ('either', 'Either')], max_length=30)),
                ('moisture', models.CharField(choices=[('wet', 'Wet'), ('moist', 'Moist'), ('dry', 'Dry')], max_length=30)),
                ('difficulty', models.CharField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], max_length=30)),
                ('light_high', models.BooleanField(default=True)),
                ('light_low', models.BooleanField(default=True)),
                ('edible', models.BooleanField(default=False)),
                ('flowering', models.BooleanField(default=False)),
                ('poisonous', models.BooleanField(default=False)),
                ('tags', taggit.managers.TaggableManager(through='taggit.TaggedItem', verbose_name='Tags', help_text='A comma-separated list of tags.', blank=True, to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
