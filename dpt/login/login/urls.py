"""login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myapp.views import *
from myapp.models import *
from django.urls import path
from myapp import urls

# from .views import list_view


from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth import views #as auth_views
from myapp import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
  
    path('',home),
   path('', views.LoginView.as_view(),name='home'),

    path('google/',google),
    path('reg/',reg),
    # path('log/',log),
   
     path('hcl/',hcl),
    path('cp/',createpost),
    path('cp1/',createpost1),

    path('add_jobseaker', add_jobseaker, name='add_jobseaker'),
    path('add_company', add_company, name='add_company'),

    path('add_login', add_login, name='add_login'),

    path('company_data',company_data),
    path('jobseaker_data',jobseaker_data),
    path('index2',index2),
    path("register/", register),
    path("myapp/",login_form),

    path("login/",login_request),
   # path("login1",login1),

    path('register1',register1,name='register1'),
    path('user_login',user_login,name='user_login'),

    path("register/",views.LoginView.as_view(template_name='register.html'),name='register'),
    path('login/',views.LoginView.as_view(template_name='login.html'),name='login'),
    path("myapp/",include('myapp.urls')),
    path('newpage/',new_page,  name="my_function"),  
    # path('s', hom),

#  path('admin/',auth_views.LoginView.as_view(),name='admin.site.urls'),
    #path('login1',login1),    #path("logout",logout_request),
    #path("logout", auth_views.logout_request.as_view(), name="logout"),
    #path("register/", include('django.contrib.auth.urls')),
    path('logout/',user_logout,name='logout'), # path('^$',myapp),    #
   # path('stu/',stu),

]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)#MEDIA_URL