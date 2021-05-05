from django.db import models
from datetime import datetime
# Create your models here.

class Song(models.Model):

    Name = models.CharField(max_length=100, blank=False, null=False)
    Duration = models.PositiveIntegerField(blank=False, null=False)
    Uploaded_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.Name


class Podcast(models.Model):

    Name = models.CharField(max_length=100, blank=False, null=False)
    Duration = models.PositiveIntegerField(blank=False, null=False)
    Uploaded_time = models.DateTimeField(blank=False)
    Host = models.CharField(blank=False, max_length=100)
    Participants = models.TextField(blank=True)

    def __str__(self):
        return self.Name



class Audiobook(models.Model):

    Title = models.CharField(max_length=100, blank=False, null=False)
    Author = models.CharField(max_length=100, blank=False, null=False)
    Narrator = models.CharField(max_length=100, blank=False, null=False)
    Duration = models.PositiveIntegerField(blank=False, null=False)
    Uploaded_time = models.DateTimeField(blank=False)

    def __str__(self):
        return self.Title


