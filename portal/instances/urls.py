from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from instances import views

urlpatterns = [
    url(r'', views.InstanceList.as_view()),
    url(r'(?P<pk>[0-9]+)/$', views.InstanceDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
