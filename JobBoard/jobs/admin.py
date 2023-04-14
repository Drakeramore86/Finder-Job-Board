from django.contrib import admin
from .models import Job, Tag, Review

# Register your models here.
admin.site.register(Job)
admin.site.register(Review)
admin.site.register(Tag)