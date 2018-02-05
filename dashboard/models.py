from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.conf import settings



class Skill(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.name








class Profile(models.Model):
    user=models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE,)
    date_of_birth=models.DateField(blank=True,null=True)
    description=models.CharField(blank=False,null=False,max_length=50,default='not sure')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile_number = models.CharField(validators=[phone_regex], blank=True, max_length=128)
    profile_image=models.ImageField(upload_to='profilepic/',blank=True)
    about_me=models.TextField(max_length=150,blank=True)
    skills=models.ManyToManyField(Skill,blank=True,null=True,related_name='has_skills')
    place=models.CharField(max_length=20,blank=True,null=True)


    def __str__(self):
        return self.user.username





class Organization_Profile(models.Model):
    user=models.OneToOneField(User,default=1)
    organisation_name=models.CharField(max_length=128,blank=False,default='something')
    organisation_description=models.TextField(max_length=500,blank=False)
    number_of_employees=models.IntegerField(blank=True,null=True)
    location=models.CharField(max_length=128,blank=True,null=True)
    organisation_image=models.ImageField(upload_to='profilepic/',blank=True)

    def __str__(self):
        return self.organisation_name


































