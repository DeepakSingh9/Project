from django import forms
from django.contrib.auth.models import User
from .models import Profile,Skill



class LoginForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('username','password','first_name','last_name','email',)




class RegisterationForm(forms.ModelForm):

    class Meta:
        model=Profile
        fields=('description',)




class ImageUpload(forms.ModelForm):

    class Meta:
        model=Profile
        fields=('profile_image',)



class AboutMeForm(forms.ModelForm):

    class Meta:
        model=Profile
        fields=('about_me',)


class AddSkillsForm(forms.ModelForm):


    class Meta:
        model=Profile
        fields=('skills',)
        widgets={
            'skills':forms.CheckboxSelectMultiple()
        }



class SkillClassForm(forms.ModelForm):

    class Meta:
        model=Skill
        fields=('name',)


class ContactForm(forms.ModelForm):

    class Meta:
        model=Profile
        fields=('mobile_number','place',)






