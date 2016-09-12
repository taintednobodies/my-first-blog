from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


'''
class Lesson(models.Model):
    author = models.ForeignKey('auth.User')
    className = models.CharField(max_length=35)
    date = models.DateTimeField(
            blank=True, null=True)
    unit = models.CharField(max_length=35)
    chapter = models.CharField(max_length=35)
    summary = models.TextField()
    materials = models.TextField()
    description = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.unit
'''
