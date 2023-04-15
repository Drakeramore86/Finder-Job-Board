from django.forms import ModelForm, widgets
from django import forms
from .models import Job

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company_name', 'location', 'remote', 'tags', 'description', 'payment']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

