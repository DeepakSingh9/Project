from __future__ import unicode_literals
from django.db import models

from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.conf import settings
from django.contrib.auth.models import User
class Section(models.Model):
    title=models.CharField(max_length=128,default='RANDOM')
    created=models.DateField(auto_now=True)
    rank=models.PositiveIntegerField(blank=True,default=100)


class Post(models.Model):
    title = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to='videos/')
    priority = models.BooleanField(default=False, blank=True)
    profile = models.ForeignKey(User, blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True)
    section=models.ForeignKey(Section,blank=True,default=100)


    def __str__(self):
        return self.title


class Like(models.Model):
    like=models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.post.title





