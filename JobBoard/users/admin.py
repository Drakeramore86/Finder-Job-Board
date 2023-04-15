from django.contrib import admin

# Register your models here.
from .models import Profile, Employer, Skill

admin.site.register(Profile)
admin.site.register(Employer)
admin.site.register(Skill)