from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    url(r'^$', lambda r: HttpResponseRedirect('memoraid/')),
    url(r'^memoraid/', include('memoraid.urls', namespace="memoraid")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', auth_views.login),	
    url(r'^accounts/logout/$', auth_views.logout),


)
