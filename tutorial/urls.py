from django.conf.urls import url
from tutorial import views

urlpatterns = [
  url(r'^$', views.home, name='home'),
  url(r'^home/$', views.home, name='home'),
  url(r'^mail/$', views.mail, name='mail'),
  url(r'^gettoken/$', views.gettoken, name='gettoken'),
]
