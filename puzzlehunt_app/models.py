from django.db import models

# Create your models here.
class Puzzle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    answer = models.CharField(max_length=30)