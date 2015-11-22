"""college URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from social.views import login
from social import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/',views.signup),
    url(r'^thanks/',views.tq),
    url(r'^authenticate/',views.autho),
   # url(r'^login/',views.login),
    url(r'^home(\d)/',views.home),
    url(r'^index/',views.index),
    url(r'^logout/',views.logout),
    #url(r'^initial',views.initial),
    url(r'^chat/',include('djangoChat.urls')),
    url(r'^welcome/',views.welcome),
    url(r'^login/', views.login),
    url(r'^in/',views.intr)
#url(r'^ccs2.0/',views.welcome),
]

