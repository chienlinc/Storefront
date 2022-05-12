from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    title       = forms.CharField(
                            label='Product Title',
                            widget=forms.TextInput(
                                attrs={
                                    'placeholder': 'Title',
                                }
                            ))
    description = forms.CharField(
                            required=False, 
                            widget=forms.Textarea(
                                attrs={
                                    'placeholder': "Enter the description here...",
                                    'rows': 5,
                                    'cols': 100,
                                }
                            ))
    price       = forms.DecimalField(initial=199.99)
    summary     = forms.CharField(required=False)
    featured    = forms.BooleanField(required=False)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'summary',
            'featured',
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if all([c.isalpha() for c in title]):
            return title
        else:
            raise forms.ValidationError("Only albhabets!")

class RawProductForm(forms.Form):
    title       = forms.CharField(
                            label='Product Title',
                            widget=forms.TextInput(
                                attrs={
                                    'placeholder': 'Title',
                                }
                            ))
    description = forms.CharField(
                            required=False, 
                            widget=forms.Textarea(
                                attrs={
                                    'placeholder': "Enter the description here...",
                                    'rows': 5,
                                    'cols': 100,
                                }
                            ))
    price       = forms.DecimalField(initial=199.99)
    summary     = forms.CharField(required=False)
    featured    = forms.BooleanField()


