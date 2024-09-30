from django import forms
from .models import Resources

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resources
        fields = ['title', 'pdfUpload']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full'}),
            'pdfUpload': forms.ClearableFileInput(attrs={'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full'}),
        }

    def clean_pdfUpload(self):
        pdf = self.cleaned_data.get('pdfUpload')

        if pdf:
            # Check if the uploaded file is a PDF by its content type
            if not pdf.content_type == 'application/pdf':
                raise forms.ValidationError('Please upload a valid PDF file.')

            # Optionally, you can also check the file size here
            # if pdf.size > 5 * 1024 * 1024:  # 5 MB limit
            #     raise forms.ValidationError('The file size must be under 5 MB.')

        return pdf
