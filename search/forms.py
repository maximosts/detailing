from django import forms

class SearchForm(forms.Form):
    item_name = forms.CharField(max_length=100, required=False, label='')
