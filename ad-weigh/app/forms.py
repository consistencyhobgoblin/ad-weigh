"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

from app.models import metric_grouping, metric_category, metric_type, metric_value

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class ValuesEntryForm(forms.ModelForm):
    model = metric_value
    when_metric_begin=forms.DateField(widget=forms.SelectDateWidget)
    when_metric_end=forms.DateField(widget=forms.SelectDateWidget)
    numeric_value=forms.CharField(widget=forms.NumberInput)
    notes=forms.CharField(widget=forms.TextInput(attrs={'size':'40'}))