from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=20)
    date = models.DateField(auto_now=True)
    description = models.CharField(max_length=100)
    url = models.URLField(blank=True)
