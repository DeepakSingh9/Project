# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from dashboard.models import Profile
from django.contrib.auth.models import User

# Create your models here.


class Bio(models.Model):

    Degree_choice=(('High School','HIGH SCHOOL'),('undergrad','UNDERGRAD'),('postgrad','POSTGRAD'),)
    user=models.OneToOneField(User,blank=True,null=True)
    description=models.CharField(max_length=128,blank=True)
    skills=models.CharField(max_length=500,blank=True)
    highest_degree=models.CharField(max_length=50,choices=Degree_choice)


    def __str__(self):
        return self.description







class Project(models.Model):
    bio=models.ForeignKey(Bio)
    title= models.CharField(max_length=128)
    year = models.DateField()
    description = models.TextField()
    link = models.URLField(blank=True)
    organisation=models.CharField(max_length=128,blank=True)
    position=models.CharField(max_length=128,blank=True)

    def __str__(self):
        return self.title




class Certification(models.Model):
    bio=models.ForeignKey(Bio)
    title=models.CharField(max_length=128)
    year=models.DateField()
    description=models.TextField()
    link=models.URLField(blank=True)
    cert_image=models.FileField(upload_to='cert_images/',blank=True)

    def __str__(self):
        return self.title



class Interest(models.Model):
    bio=models.ForeignKey(Bio)
    name=models.CharField(max_length=128,blank=True)


    def __str__(self):
        return self.name



class WorkExperience(models.Model):
    bio=models.ForeignKey(Bio)
    organisation=models.CharField(max_length=128,blank=True,null=True)
    designation=models.CharField(max_length=128,blank=True,null=True)
    worked_from=models.DateTimeField()
    worked_till=models.DateTimeField()
    current=models.BooleanField(default=False)
    describe=models.TextField(blank=True)

    def __str__(self):
        return self.organisation
