from django.forms import ModelForm
from .models import Job

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company_name', 'location', 'remote', 'tags', 'description']