from . models import Postings
from django import forms

class JobPostForm(forms.ModelForm):

    class Meta:
        model=Postings
        fields=('position_name','no_of_positions','organisation','location','salary_range','requirements','description','category')




