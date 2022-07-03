from email.policy import default
from tkinter import Widget
from django import forms
from django_countries.fields import CountryField
from . import models


class SearchForm(forms.Form):
    """Search Form Definition"""

    city = forms.CharField(initial="Anywhere")
    country = CountryField(default="JP").formfield()
    room_type = forms.ModelChoiceField(
        required=False, queryset=models.RoomType.objects.all()
    )
    price = forms.IntegerField(required=False, min_value=0)
    bedrooms = forms.IntegerField(required=False)
    beds = forms.IntegerField(required=False)
    baths = forms.IntegerField(required=False)
    instant_book = forms.BooleanField(required=False)
    superhost = forms.BooleanField(required=False)
    amenities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Amenity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    facilities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Facility.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
