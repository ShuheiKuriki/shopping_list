from django.forms import ModelForm
from django import forms
from .models import Shopping
# from django.utils import timezone

class DateInput(forms.DateInput):
    input_type = 'date'

class ShoppingForm(ModelForm):
    class Meta:
        model = Shopping
        fields = ['name','shop','price','date']
        forms.CheckboxInput(attrs={'class': 'check'})

class SortForm(forms.Form):
    keys = [('buy_or_not','購入済'),("shop",'店')]
    key = forms.ChoiceField(choices=keys,required=True)

