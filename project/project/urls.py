from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from core.api.resources import ServidorResource, AplicacaoResource

v1_api = Api(api_name='v1')
v1_api.register(ServidorResource())
v1_api.register(AplicacaoResource())


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
