from csv import writer
from django.conf import settings
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 200, default = '세은')
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    pub_date = models.DateTimeField('data published')
    body = models.TextField(blank=True)
    feelings = models.CharField(blank=True, null=True)
    
    def __str__(self):
        return self.title
