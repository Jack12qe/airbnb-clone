from email.policy import default
from tkinter import Widget
from django import forms
from django_countries.fields import CountryField
from users import models as user_models
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


class CreatePhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ("caption", "file")

    def save(self, pk, *args, **kwargs):
        """This method complete the form"""

        photo = super().save(commit=False)
        room = models.Room.objects.get(pk=pk)
        photo.room = room
        photo.save()


class CreateRoomForm(forms.ModelForm):
    class Meta:
        model = models.Room
        fields = (
            "name",
            "description",
            "country",
            "city",
            "price",
            "address",
            "guests",
            "beds",
            "bedrooms",
            "baths",
            "check_in",
            "check_out",
            "instant_book",
            "room_type",
            "amenities",
            "facilities",
            "house_rules",
        )

    def save(self, host, *args, **kwargs):
        room = super().save(commit=False)
        room.host = host
        room.save()
        room.save_m2m()
        return room
