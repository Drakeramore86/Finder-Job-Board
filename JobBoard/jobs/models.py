from django.db import models
import uuid

# Create your models here.
class Job(models.Model):
    #owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=50)
    location = models.CharField(max_length=100, null=True, blank=True)
    remote = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag', blank=True)
    description = models.TextField(null=True, blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title', 'created']


class Review(models.Model):
    VOTE_TYPE = (
        ('one', 'One Star'),
        ('two', 'Two Stars'),
        ('three', 'Three Stars'),
        ('four', 'Four Stars'),
        ('five', 'Five Stars'),
    )
    # owner =
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    def __str__(self):
        return self.name