from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from risks import views
 
app_name = 'risks'

urlpatterns = [
    url(r'^$', views.RiskList.as_view(), name='risk-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.RiskDetail.as_view(), name='risk-detail'),
]
