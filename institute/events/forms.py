from django import forms
from .models import Events
from tinymce.widgets import TinyMCE

class EventForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE(attrs={'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full', 'rows': 5}))

    class Meta:
        model = Events
        fields = ['name', 'body', 'address', 'date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full'}),
            'address': forms.TextInput(attrs={'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full'}),
            'date': forms.SelectDateWidget(attrs={'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full'}),
        }
