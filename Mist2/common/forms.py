from django import forms

from Mist2.common.models import Comment


class SearchForm(forms.Form):
    game_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Name'
    }))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
        widgets = {
            'comment_text': forms.Textarea(attrs={'placeholder': 'Add comment...'})
        }
