from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    username = models.CharField(max_length=20)
    location = models.CharField(max_length=30, blank=True)
    password = models.CharField(max_length=15)
    profile_pic = models.ImageField(upload_to='pic_folder/', default = 'pic_folder/None/no-img.png', verbose_name='profilepic')
    cover_pic = models.ImageField(upload_to='pic_folder/', default = 'pic_folder/None/no-img.png', verbose_name='coverpic')

