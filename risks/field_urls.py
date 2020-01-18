from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from risks import views
 
app_name = 'fields'

urlpatterns = [
    url(r'^$', views.FieldList.as_view(), name='field-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.FieldDetail.as_view(), name='field-detail'),
    url(r'^risk/(?P<pk>[0-9]+)/$', views.FieldRiskList.as_view(), name='field-list')
]
