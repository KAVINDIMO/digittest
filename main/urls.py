from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include


urlpatterns=[
path("",views.basic,name="basic"),
path("basic/",views.basic,name="basic"),
path("contactus/basic/",views.basic,name="basic"),
path("pybot/",views.pybot,name="pybot"),
path("tmembers/",views.tmembers,name="tmembers"),
path("aboutus/",views.aboutus,name="aboutus"),
path("contactus/",views.contactus,name="contactus"),
path("comment/",views.comment,name="comment"),
path("comment/add_comment/",views.add_comment,name="add_comment"),
path("register/",views.register,name="register"),
path("newspost/",views.newspost,name="newspost"),
path("showinfo/",views.showinfo,name="newspost"),
path('upload/', views.newspostupload,name="newspostupload"),
path('uploadevents/', views.eventspostupload,name="eventspostupload"),
path('events/',views.eventpost,name="events"),
path('basic/profile/',views.profile,name="bprofile"),
path('tmembers/profile/<tager>/',views.profile,name="tprofile"),
#path('edit_profile/',views.edit_profile,name="edit"),
path('members/',views.members,name="members"),
path('members/profile/<tager>/',views.profile,name="tprofile"),
path('profile/<tager>/',views.profile,name="profile"),
path('project/',views.pproject,name="project"),
#path('news/',views.newspage,name="newspage"),
path('news/',views.newspage,name="newspage"),
path('viewprofile/',views.viewprofile,name="viewprofile"),
path('members/viewprofile/',views.viewprofile,name="viewprofile"),
path('basic/viewprofile/',views.viewprofile,name="viewprofile"),
path('uploadproject/',views.projectupload,name="projectupload"),
path('achievements/',views.aachievements,name="achievements"),
path('addachievements/',views.addachievements,name="addachievements"),
path('dispprofile/',views.DispProfile,name="dispprofile"),
path('reportnews/',views.reportupload,name="reportnews"),
path('viewinfo/<tager>/',views.viewinfo,name="viewinfo"),
path('newspost/viewinfo/<tager>/',views.viewinfo,name="viewinfo"),

]