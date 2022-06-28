from distutils.command.upload import upload
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Page(models.Model):
    title = models.CharField('Título', max_length=40)
    subtitle = models.CharField('Subtítulo', max_length=130)
    date = models.DateTimeField('Fecha de creación', auto_now = False, auto_now_add=True)
    image = models.ImageField(upload_to='photos', null=True, blank=True)
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    content_post = RichTextField('Contenido del post')
    

    def __str__(self):
        return f'{self.title} -- Fecha de creación: {self.date} -- {self.account}'


