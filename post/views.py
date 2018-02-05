# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from django.shortcuts import get_object_or_404
# Create your views here.

from django.shortcuts import render
from forms import PostForm
# Create your views here.

def post(request):
    user=request.user
    return render(request,'post/post.html',{'user':user})



def uploadskills(request):
    if request.method == 'POST':
        user = request.user
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = user
            post.save()


            return redirect('/dashboard')
        else:
            print form.errors

    else:
        form=PostForm()
    return render(request,'post/uploadskills.html',{'form':form})



def like(request,pk):
    user=request.user
    post=Post.objects.get(pk=pk)
    like.objects.create(user=user,post=post)





