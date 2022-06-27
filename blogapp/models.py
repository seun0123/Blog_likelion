from csv import writer
from django.conf import settings
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, default = '제목')
    author = models.CharField(max_length=100, default = '세은')
    pub_date = models.DateTimeField('data published')
    body = models.TextField(blank=True)
    feelings = models.CharField(max_length=100,blank=True, null=True)
    
    def __str__(self):
        return self.title
