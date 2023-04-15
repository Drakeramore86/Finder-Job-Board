from django.shortcuts import render
from .models import Profile, Employer
from django.shortcuts import get_object_or_404
# Create your views here.
def profiles(request):
    employers = Employer.objects.all()
    profiles = Profile.objects.all()
    context = {"employers": employers, "employees": profiles}
    return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
    profile = get_object_or_404(Profile, id=pk)
    employer = None
    is_employer = False

    if hasattr(profile, 'employer'):
        employer = profile.employer
        is_employer = True

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    context = {
        'profile': profile,
        'topSkills': topSkills,
        'otherSkills': otherSkills,
        'is_employer': is_employer,
        'employer': employer,
    }
    return render(request, 'users/single-profile.html', context)