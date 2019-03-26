# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from .models import UserProfile, IGPost, Comment, Like

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(IGPost)
admin.site.register(Comment)
admin.site.register(Like)
