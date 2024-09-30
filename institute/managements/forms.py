from django import forms
from .models import Managements
from tinymce.widgets import TinyMCE

class ManagementsForm(forms.ModelForm):
    detail = forms.CharField(
        widget=TinyMCE(attrs={'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full', 'rows': 5})
    )

    class Meta:
        model = Managements
        fields = ['name', 'position', 'detail', 'image', 'priority']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full'}),
            'position': forms.TextInput(attrs={'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full'}),
            'image': forms.FileInput(attrs={'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full'}),
            'priority': forms.NumberInput(attrs={'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full'}),
        }
