from django.db import models
from django.contrib.auth.models import User
from pages.models import Page


class Comment(models.Model):
    post = models.ForeignKey(Page, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=144)
    date = models.DateTimeField('Fecha del comentario', auto_now = False, auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.user)