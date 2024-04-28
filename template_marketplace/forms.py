from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('name', 'file', 'description', 'image_banner')  # Include the new fields
