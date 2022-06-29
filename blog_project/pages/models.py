from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Post(models.Model):
    title = models.CharField(max_length=60, blank=False)
    title_tag = models.CharField(max_length=60)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=True)
    post_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('page:post-detail', args=(str(self.pk)) )