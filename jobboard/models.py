# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from dashboard.models import Organization_Profile

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=128,blank=True,null=True)


    def __str__(self):
        return self.name



class Postings(models.Model):
    position_name=models.CharField(max_length=128,blank=True,null=True)
    no_of_positions=models.IntegerField()
    organisation=models.ForeignKey(Organization_Profile)
    location=models.CharField(max_length=128,blank=True,null=True)
    salary_range=models.CharField(max_length=128,blank=True,null=True)
    requirements=models.TextField()
    description=models.TextField()
    category=models.ForeignKey(Category)
    posted_on=models.DateField(auto_now_add=True)




    def __str__(self):
        return self.position_name+self.organisation.organisation_name





