# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Category,Postings
from .forms import JobPostForm
from dashboard.models import Organization_Profile
from django.utils import timezone
from django.http import HttpResponse

# Create your views here.
def list(request):
    pass


def AddPosting(request):
    user=request.user
    organisation=Organization_Profile.objects.get(user=user)
    if request.method=='POST':
        form=JobPostForm(request.POST)
        if form.is_valid():
            posting = form.save(commit=False)
            posting.organisation=organisation
            posting.posted_on=timezone.now()
        else:
            return HttpResponse('Please fill the form properly')

    else:
        form=JobPostForm()
    return render(request,'jobboard/add_posting.html',{'form':form})


