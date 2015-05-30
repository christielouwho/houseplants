from model_utils import Choices
from django.utils.translation import ugettext_lazy as _


TEMPERATURE_CHOICES = Choices(
    ('cool', 'COOL', _('Cool (50-70 F)')),
    ('warm', 'WARM', _('Warm (60-85 F)')),
    ('either', 'EITHER', _('Either')),
)

MOISTURE_CHOICES = Choices(
    ('wet', 'WET', _('Wet')),
    ('moist', 'MOIST', _('Moist')),
    ('dry', 'DRY', _('Dry')),
)

DIFFICULTY_CHOICES = Choices(
    ('easy', 'EASY', _('Easy')),
    ('medium', 'MEDIUM', _('Medium')),
    ('hard', 'HARD', _('Hard')),
)
