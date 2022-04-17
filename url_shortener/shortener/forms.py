from dataclasses import field
from django.forms import ModelForm

from .models import Urls


class UrlsForm(ModelForm):
    class Meta:
        model = Urls
        fields = ('http_url',)
