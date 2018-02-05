from django.conf.urls import url
from . import views

urlpatterns=[url(r'^$',views.dashboard,name='home'),
             url(r'account/(?P<pk>\d+)/$',views.account,name='account'),
             url(r'^login/$',views.user_login,name='login'),
             url(r'^registration/$',views.user_registration,name='registration'),
             url(r'^logout/$',views.user_logout,name='logout'),
             url(r'^upload/$',views.profile_image_upload,name='imageupload'),
             url(r'account/(?P<pk>\d+)/about/$',views.about,name='about'),
             url(r'account/(?P<pk>\d+)/edit_about/$',views.edit_about,name='edit_about'),
             url(r'addskill/(?P<pk>\d+)/$',views.addskill,name='addskill'),
             url(r'removeskill/(?P<pk>\d+)/(?P<skill_id>\d+)/$',views.removeskill,name='removeskill'),
             url(r'skilllistadd/(?P<pk>\d+)/$',views.addskilltoskilllist,name='skilllistadd'),
             url(r'contacform/(?P<pk>\d+)/$',views.edit_contact,name='contactform'),
]