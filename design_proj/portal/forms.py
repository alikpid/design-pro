from django import forms
from django.core.exceptions import ValidationError


class SearchForm(forms.Form):
    keyword = forms.CharField(required=False, max_length=20, label='')

