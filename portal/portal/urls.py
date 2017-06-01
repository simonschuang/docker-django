from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
#from django.contrib.auth.models import User
#from rest_framework import routers, serializers, viewsets
#from rest_framework.schemas import get_schema_view
#from instances.views import InstanceList, InstanceDetail


urlpatterns = [
    url(r'^docs/', include('rest_framework_docs.urls')),

    # API
    url(r'^devices/', view=include('devices.urls')),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
