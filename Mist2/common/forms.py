from django import forms


class SearchForm(forms.Form):
    game_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Name'
    }))
