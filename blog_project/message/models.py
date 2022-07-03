from django.db import models
from django.contrib.auth.models import User
from pages.models import Post
from django.urls import reverse
from ckeditor.fields import RichTextField


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    #name =  models.CharField(max_length=30)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.author)
    
    def get_absolute_url(self):
        return reverse('page:post-detail', args=(str(self.post.pk)) )
