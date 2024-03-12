from django import forms
from .models import Event
from .models import Place
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'location', 'address', 'preview_image', 'short_description', 'full_description', 'category', 'start_datetime', 'end_datetime']

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'address', 'city', 'image', 'short_description', 'full_description', 'phone_number')
