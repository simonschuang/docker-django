from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from devices import views

urlpatterns = [
    url(r'^$', views.DeviceList.as_view()),
    url(r'(?P<pk>[0-9]+)/$', views.DeviceDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
