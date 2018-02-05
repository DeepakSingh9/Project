from __future__ import unicode_literals

from django.contrib import admin
from .models import Post,Like

class PostAdmin(admin.ModelAdmin):
    list_display = ['video','created','modified','title']

admin.site.register(Post,PostAdmin)


class LikeAdmin(admin.ModelAdmin):
    list_display = ['like','post','user']

admin.site.register(Like,LikeAdmin)