from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text':'Your Comment'}
        widgets = {
            'text':forms.Textarea(attrs={
                'class':'form-control',
                'rows':4,
                'placeholder':'Please let us kno what you think!'
            })
        }