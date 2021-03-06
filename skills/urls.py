from django.conf.urls import url
from . import views

urlpatterns=[url(r'^$',views.skills,name='skills'),
             url(r'^bio/$',views.bio,name='bio'),
             url(r'^edit_bio/(?P<pk>\d+)/$',views.edit_bio,name='edit_bio'),
             url(r'^certification/$',views.certification,name='certification'),
             url(r'^edit_certification/(?P<pk>\d+)/$',views.edit_certification,name='edit_certification'),
             url(r'^workexp/$',views.workexp,name='workexp'),
             url(r'^edit_workexp/(?P<pk>\d+)/$',views.edit_workexp,name='edit_workexp'),
             url(r'^interest/$',views.interest,name='interest'),
             url(r'^edit_interest/(?P<pk>\d+)/$',views.edit_interest,name='edit_interest'),
             url(r'^project/$',views.project,name='project'),
             url(r'^edit_project/(?P<pk>\d+)/$',views.edit_project,name='edit_project'),
             url(r'^delete_project/(?P<pk>\d+)/$',views.delete_project,name='delete_project'),
             url(r'^delete_certification/(?P<pk>\d+)/$',views.delete_certification,name='delete_certification'),
             url(r'^delete_interest/(?P<pk>\d+)/$',views.delete_interest,name='delete_interest'),
             url(r'^delete_workexp/(?P<pk>\d+)/$',views.delete_workexp,name='delete_workexp'),
              ]