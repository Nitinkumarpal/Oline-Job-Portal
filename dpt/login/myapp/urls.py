from django.urls import path
from . import views
from myapp.templates import *


app_name = 'myapp'  # here for namespacing of urls.

urlpatterns = [
  path("login", views.login_request, name="login"), 
  #path("login1", views.login1, name="login1"),
 # path("log", views.log, name="log"), 
  path(r'^(?P<id>\d+)/(?P<name>[-\w]+)/$',views.jobseeker_detail,name='jobseeker_detail'),

  path(r'^(?P<id>\d+)/(?P<Company_name>[-\w]+)/$',views.company_detail,name='company_detail'),
  path("home", views.home, name="home"),
  path("register", views.register, name="register"),
  path("indexx", views.indexx, name="indexx"),
  path('logout/',views.user_logout,name='logout'), 



  
]