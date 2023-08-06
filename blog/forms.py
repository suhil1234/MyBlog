from django import forms
from .models import Comments, Posts

class PostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=['title','content']
        widgets = {
          'content': forms.Textarea(attrs={'rows':4}),
        }

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='', widget=forms.TextInput(attrs={'placeholder': 'Add comment here....'}))
    class Meta:
        model=Comments
        fields=['content']
