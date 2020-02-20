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

#class ValuesEntryForm(forms.ModelForm):
#    model = metric_value
#    when_metric_begin=forms.DateField(widget=forms.SelectDateWidget)
#    when_metric_end=forms.DateField(widget=forms.SelectDateWidget)
#    numeric_value=forms.CharField(widget=forms.NumberInput)
#    notes=forms.CharField(widget=forms.TextInput(attrs={'size':'40'}))


class ValuesEntryForm(forms.ModelForm):
    lstYears = ['1900', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030']
    model = metric_value
    es_attrs = {'class': 'form-control'}
    nm_attrs = {'class': 'form-control', 'step': 0.01}
    when_metric_begin=forms.DateField(widget=forms.SelectDateWidget(years=lstYears))
    when_metric_end=forms.DateField(widget=forms.SelectDateWidget(years=lstYears))
    #when_metric_end=forms.DateField(widget=forms.SelectDateWidget(years=range(2017, 2040)))
    numeric_value=forms.CharField(widget=forms.NumberInput(attrs=nm_attrs))
    notes=forms.CharField(widget=forms.TextInput(attrs=es_attrs))