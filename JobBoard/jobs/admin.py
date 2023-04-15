from django.contrib import admin
from .models import Job, Tag, Review, JobApplication, SavedJob

# Register your models here.
admin.site.register(Job)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(JobApplication)
admin.site.register(SavedJob)