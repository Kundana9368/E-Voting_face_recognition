"""Evoting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url

from admins import views as admin_views

urlpatterns = [
    
    url('admin/', admin.site.urls),

    url(r'^$', admin_views.index, name='index' ),

    url(r'^about$', admin_views.about, name='about' ),

    url(r'^login$', admin_views.login, name='login' ),

    url(r'^gallery$', admin_views.gallery, name='gallery' ),

    url(r'^contact$', admin_views.contact, name='contact' ),

    url(r'^AdminHome/$', admin_views.AdminHome, name='AdminHome'),

    url(r'^ServerHome/$', admin_views.ServerHome, name='ServerHome'),

    url(r'^VoteCandidate/$', admin_views.VoteCandidate, name='VoteCandidate'),

    url(r'^VoterSubmit/$', admin_views.VoterSubmit, name='VoterSubmit')


    
     

]


