from django import forms

from .constants import TEMPERATURE_CHOICES, MOISTURE_CHOICES, DIFFICULTY_CHOICES


class HouseplantSearchForm(forms.Form):
    q = forms.CharField(required=False)
    temperature = forms.ChoiceField(choices=TEMPERATURE_CHOICES, required=False)
    moisture = forms.ChoiceField(choices=MOISTURE_CHOICES, required=False)
    difficulty = forms.ChoiceField(choices=DIFFICULTY_CHOICES, required=False)
    light_high = forms.BooleanField(required=False, initial=True)
    light_low = forms.BooleanField(required=False, initial=True)
    edible = forms.BooleanField(required=False)
    flowering = forms.BooleanField(required=False)
    poisonous = forms.BooleanField(required=False)
