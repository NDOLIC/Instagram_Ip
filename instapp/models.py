# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver



class UserProfile(models.Model):
    photo=models.ImageField(upload_to='images/')
    bio=models.TextField()
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    follow=models.NullBooleanField(default=False)
    
    def save_profile(self):
        self.save()
    def delete_profile(self):
       self.delete()

    def update_bio(self,bio):
         self.bio=bio
         self.save()

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)

class IGPost(models.Model):
    user_profile = models.ForeignKey(UserProfile, null=True, blank=True)
    title = models.CharField(max_length=100)
    image = ProcessedImageField(upload_to='posts',
                                #processors=[ResizeToFill(200,200)],
                                format='JPEG',
                                options={ 'quality': 100})
    posted_on = models.DateTimeField(default=datetime.now)

    def get_number_of_likes(self):
        return self.like_set.count()

    def get_number_of_comments(self):
        return self.comment_set.count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('IGPost')
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=100)
    posted_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.comment


class Like(models.Model):
    post = models.ForeignKey('IGPost')
    user = models.ForeignKey(User)

    class Meta:
        unique_together = ("post", "user")

    def __str__(self):
        return 'Like: ' + self.user.username + ' ' + self.post.title
