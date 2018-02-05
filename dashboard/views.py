# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm,RegisterationForm,ImageUpload,AboutMeForm,AddSkillsForm,SkillClassForm,ContactForm
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile,Skill
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
# Create your views here.



def dashboard(request):
    return render(request,'dashboard/home.html',{})




def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('account',pk=user.pk)
            else:
                return HttpResponse('Your account is disabled')
        else:
            print "invalid login details.{0} {1}".format(username,password)
            return HttpResponse('invalid login details')

    return render(request,'dashboard/login.html',{})






def user_registration(request):
    if request.method=='POST':


        userlogin=LoginForm(request.POST)
        userregister=RegisterationForm(request.POST)
        username=request.POST['username']
        password=request.POST['password']

        if userlogin.is_valid() and userregister.is_valid():
            user=userlogin.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile=userregister.save(commit=False)
            profile.user=user
            profile.save()


            login(request,authenticate(username=userlogin.cleaned_data['username'],password=userlogin.cleaned_data['password']))
            return redirect('account',pk=user.pk)
        else:
            print userlogin.errors,userregister.errors


    else:
        userlogin=LoginForm()
        userregister=RegisterationForm()
    return render(request,'dashboard/home.html',{'userlogin':userlogin,'userregister':userregister,})



@login_required()
def user_logout(request):
    logout(request)
    return redirect('/dashboard')



@login_required()
def profile_image_upload(request):
    image=False
    user = request.user
    profile = get_object_or_404(Profile, pk=user.id)
    if request.method =='POST':
        form = ImageUpload(request.POST,request.FILES)
        if form.is_valid():
            profile.profile_image=request.FILES['file']
            form.save()
            profile.save()
            image=True
            return redirect('/dashboard')
        else:
            return HttpResponse('please choose an image')
    else:
        form=ImageUpload()
    return render(request,'dashboard/imageupload.html',{'form':form,'profile':profile,'user':user,'image':image})




def account(request,pk):
    user=get_object_or_404(User,pk=pk)
    profile=get_object_or_404(Profile,pk=pk)
    return render(request,'dashboard/account.html',{'profile':profile,'user':user})
# -*- coding: utf-8 -*-



def about(request,pk):
    profile=Profile.objects.get(pk=pk)
    user=User.objects.get(pk=profile.pk)
    if request.method=='POST':
        aboutform = AboutMeForm(request.POST)
        if aboutform.is_valid():
            profile.about_me=request.POST['about_me']
            profile.save()
            return redirect('account',pk=user.id)
    else:
        aboutform=AboutMeForm()
    return render(request,'dashboard/aboutform.html',{'aboutform':aboutform})



def edit_about(request,pk):
    profile=Profile.objects.get(pk=pk)
    if request.method=='POST':
        aboutform=AboutMeForm(request.POST,instance=profile)
        if aboutform.is_valid():
            profile.about_me=request.POST['about_me']
            profile.save()
            return redirect('account',pk=profile.pk)
    else:
        aboutform=AboutMeForm(instance=profile)
    return render(request,'dashboard/aboutform.html',{'aboutform':aboutform})





def addskill(request,pk):
    profile=Profile.objects.get(pk=pk)
    if request.method=='POST':

        profileskillform=AddSkillsForm(request.POST,instance=profile)

        if profileskillform.is_valid():
            skills = profileskillform.cleaned_data['skills']
            profileskillform=profileskillform.save(commit=False)
            profile.user=request.user
            for all in skills:
                profile.skills.add(all)
            profileskillform = profileskillform.save()
            return redirect('account',pk=pk)
    else:
        profileskillform=AddSkillsForm(instance=profile)
    return render(request,'dashboard/addskill.html',{'profileskillform':profileskillform})


def removeskill(request,pk,skill_id):
    profile=Profile.objects.get(pk=pk)
    skill=profile.skills.get(id=skill_id)
    profile.skills.remove(skill)
    return redirect('account',pk=pk)






def addskilltoskilllist(request,pk):
    profile=Profile.objects.get(pk=pk)
    if request.method=='POST':
        skillclassform=SkillClassForm(request.POST)
        if skillclassform.is_valid():
            skills=skillclassform.cleaned_data['name']
            skillclassform=skillclassform.save(commit=False)
            if not Skill.objects.filter(name__iexact=skills):
                newskill=Skill.objects.create(name=skills)
                profile.skills.add(newskill)
            return redirect('addskill',pk=pk)

    else:
        skillclassform=SkillClassForm()
    return render(request,'dashboard/addskill.html',{'skillclassform':skillclassform})


def edit_contact(request,pk):
    profile=get_object_or_404(Profile,pk=pk)
    if request.method=='POST':
        contactform=ContactForm(request.POST,instance=profile)
        if contactform.is_valid():
            mobile=contactform.cleaned_data['mobile_number']
            place=contactform.cleaned_data['place']
            contactform=contactform.save(commit=False)
            profile.place=place
            profile.mobile_number=mobile
            profile.save()
            contactform.save()
            return redirect('account',pk=pk)
    else:
        contactform=ContactForm(instance=profile)
    return render(request,'dashboard/contactform.html',{'contactform':contactform})


