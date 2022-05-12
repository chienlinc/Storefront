from django import forms
from .models import Course

class CourseForm(forms.ModelForm):

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Title',
            }
        ))

    class Meta:
        model = Course
        fields = [
            'title'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if all([c.isalpha() or " " for c in title]):
            return title
        else:
            raise forms.ValidationError("Only albhabets!")