from django import forms
from .models import Projects
from tinymce.widgets import TinyMCE


class ProjectsForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full', 'rows': 5}))

    class Meta:
        model = Projects
        fields = ['title', 'description', 'status', 'start_date', 'end_date', 'pdfUpload']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full'}),
            'status': forms.TextInput(attrs={'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full'}),
            'start_date': forms.SelectDateWidget(attrs={'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full'}),
            'end_date': forms.SelectDateWidget(attrs={'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full'}),
            'pdfUpload': forms.ClearableFileInput(attrs={'class': 'mt-1 outline-none border-2 border-gray-200 p-2 w-full'}),
        }

    def clean_pdfUpload(self):
        pdf = self.cleaned_data.get('pdfUpload')

        if pdf:
            if hasattr(pdf, 'content_type'):
                # Check if the uploaded file is a PDF by its content type
                if not pdf.content_type == 'application/pdf':
                    raise forms.ValidationError('Please upload a valid PDF file.')

            # Optionally, you can also check the file size here
            # if pdf.size > 5 * 1024 * 1024:  # 5 MB limit
            #     raise forms.ValidationError('The file size must be under 5 MB.')

        return pdf
