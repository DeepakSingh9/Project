# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category,Postings

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class PostingAdmin(admin.ModelAdmin):
    list_display = ['position_name','no_of_positions','organisation','category','location','salary_range','requirements','description','posted_on']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Postings,PostingAdmin)


