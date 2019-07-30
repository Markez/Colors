from django.conf.urls import url
from .views import CompanyApiView,RangiApiView,CompanyRudApiView,RangiRudApiView

app_name = "rangi"

urlpatterns = [
    # the RUD view must be followed by a pk value to view one object alone

    url(r'^company/(?P<pk>[0-9]+)$',CompanyRudApiView.as_view(),name="company-list"),
    url(r'^rangi/(?P<pk>[0-9]+)$',RangiRudApiView.as_view(),name="rangi-list"),
    url(r'^company/$',CompanyApiView.as_view(),name="company-create"),
    url(r'^rangi/$',RangiApiView.as_view(),name="rangi-create"),

]