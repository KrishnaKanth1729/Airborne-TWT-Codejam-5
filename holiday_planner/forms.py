from django.forms import ModelForm
from .models import *


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['city', 'country', 'types', 'image_url', 'description']



class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'text', 'rating']

from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label='query', max_length=100)

class EmailForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'feedback']
