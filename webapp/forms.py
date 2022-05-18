from django import forms

from webapp.models import MyTariff


class SearchForm(forms.Form):
    searchsms = forms.CharField(max_length=100, required=False)
    searchmin = forms.CharField(max_length=100, required=False)
    searchgb = forms.CharField(max_length=100, required=False)


class MyTariffForm(forms.ModelForm):
    class Meta:
        model = MyTariff
        exclude = ['user', 'tariff']
