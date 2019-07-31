
from django.contrib import admin
from django.conf.urls import url,include
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/',include('rangi.api.urls',namespace="api")),
    url(r'^home/',include('rangi.urls')),

]
