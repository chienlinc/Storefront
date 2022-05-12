from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):

    title       = forms.CharField(
                            label='Article Title',
                            widget=forms.TextInput(
                                attrs={
                                    'placeholder': 'Title',
                                }
                            ))
    content = forms.CharField(
                            required=False, 
                            widget=forms.Textarea(
                                attrs={
                                    'placeholder': "Enter your content here...",
                                    'rows': 10,
                                    'cols': 150,
                                }
                            ))
    active    = forms.BooleanField(required=False)

    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active',
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if all([not c.isdigit() for c in title]):
            return title
        else:
            raise forms.ValidationError("Only albhabets!")