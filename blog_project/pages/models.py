from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=60, blank=False)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    subtitle = models.CharField(max_length=130, blank=False, null=True)
    title_tag = models.CharField(max_length=60)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('page:post-detail', args=(str(self.pk)) )