from django.shortcuts import render, redirect
from . models import Job
from .forms import JobForm
# Create your views here.


def jobs(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/jobs.html', {"jobs": jobs})


def job(request, pk):
    specific_job = Job.objects.get(id=pk)
    return render(request, 'jobs/single-job.html', {"job": specific_job})

def createJob(request):
    form = JobForm(request.POST, request.FILES)

    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobs')

    context = {"form": form}
    return render(request, 'jobs/job_form.html', context=context)


def updateJob(request, pk):
    job = Job.objects.get(id=pk)
    form = JobForm(instance=job)

    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            form.save()
            return redirect('jobs')

    context = {"form": form}
    return render(request, 'jobs/job_form.html', context=context)


def deleteJob(request, pk):
    job = Job.objects.get(id=pk)

    if request.method == "POST":
        job.delete()
        return redirect('jobs')

    context = {'object': job}
    return render(request, 'jobs/delete_template.html', context=context)