from django.conf.urls import url
from . import views

urlpatterns=[url(r'^$',views.post,name='post'),
             url(r'^uploadskills/$',views.uploadskills,name='uploadskills'),
             url(r'^like/$',views.like,name='like'),
             ]