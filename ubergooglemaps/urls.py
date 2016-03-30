from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$','rides.views.index',name='rides'),
    url(r'^sendemail$','rides.views.sendemail',name='email'),
    url(r'^setReminder$','rides.views.setReminder',name='remainder'),
    
]

