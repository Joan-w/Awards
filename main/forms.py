from django import forms
from .models import *

# Project add form
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name',
            'image',
            'languages',
            'description',
            'projectLink'
            ]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']