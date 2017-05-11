from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^instance/$', views.instance_list),
    url(r'^instance/(?P<pk>[0-9]+)/$', views.instance_detail),
]
