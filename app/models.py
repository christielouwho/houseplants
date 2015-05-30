from django.db import models
from django_extensions.db.models import AutoSlugField
from django.core.urlresolvers import reverse

from model_utils.models import TimeStampedModel
from taggit.managers import TaggableManager

from .constants import TEMPERATURE_CHOICES, MOISTURE_CHOICES, DIFFICULTY_CHOICES


def image_upload_to(instance, filename):
    return 'plant_avatars/{}/{}'.format(instance.pk, filename)


class Houseplant(TimeStampedModel):
    common_name = models.CharField(max_length=100)
    latin_name = models.CharField(max_length=200, blank=True, null=True)
    slug = AutoSlugField(populate_from=['common_name'], unique=True)
    avatar = models.ImageField(upload_to=image_upload_to, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    care_notes = models.TextField(blank=True, null=True)
    temperature = models.CharField(max_length=30, choices=TEMPERATURE_CHOICES)
    moisture = models.CharField(max_length=30, choices=MOISTURE_CHOICES)
    difficulty = models.CharField(max_length=30, choices=DIFFICULTY_CHOICES)
    light_high = models.BooleanField(default=True)
    light_low = models.BooleanField(default=True)
    edible = models.BooleanField(default=False)
    flowering = models.BooleanField(default=False)
    poisonous = models.BooleanField(default=False)

    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.common_name

    def get_absolute_url(self):
        return 'plants/' + self.slug
        # return reverse('houseplant_detail', args=(self.slug, ))
