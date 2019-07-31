from django.conf.urls import url
from .views import home,CreateUser,CreateRangi,CreateCompany


urlpatterns = [
    url(r'^$',home.as_view(),name='home'),
    url(r'^register/$',CreateUser.as_view(),name='user_create'),
    url(r'^rangi/$',CreateRangi.as_view(),name='rangi-create'),
    url(r'^company/$',CreateCompany.as_view(),name='company-create'),




]
