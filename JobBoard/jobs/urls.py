from django.urls import path
from . import views

urlpatterns = [
    path("", views.jobs, name="jobs"),
    path("jobs/<str:pk>/", views.job, name="job"),

    path('create-project/', views.createJob, name="create-job"),
    path('update-project/<str:pk>/', views.updateJob, name="update-job"),
    path('delete-project/<str:pk>/', views.deleteJob, name="delete-job"),
]