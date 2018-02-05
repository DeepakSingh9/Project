# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Profile,Organization_Profile,Skill


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','date_of_birth','description',]

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['organisation_name','organisation_description','number_of_employees','location','organisation_image']


class SkillAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Organization_Profile,OrganizationAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill,SkillAdmin)



