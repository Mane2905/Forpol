from django.db import models
from datetime import datetime

class Content(models.Model):
    thumbnail = models.TextField(blank=False)
    shortthumb = models.TextField(blank=False,default="null")
    img = models.ImageField(upload_to='photos/%Y/%m/%d/')
    cont=models.TextField(blank=False)
    Date = models.DateTimeField(default=datetime.now, blank=True)
    is_published=models.BooleanField(default=True)
    def __str__(self):
        return self.thumbnail