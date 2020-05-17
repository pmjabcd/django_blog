from django.db import models
from django.utils.timezone import now

# Create your models here.
class Article(models. Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    category = models.CharField(max_length=30, default='movie')
    time = models.DateTimeField(default=now, blank=True)

# class Article(models. Model):
#     def __ str __ (self):
#         return "첫번째"

def __str__(self):
    return self.title 