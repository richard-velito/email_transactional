from django.conf.urls import url, include
from .api import AppResource, EmailResource, AttachmentsResource

from . import views

from tastypie.api import Api
v1_api = Api(api_name='v1')
v1_api.register(AppResource())
v1_api.register(EmailResource())
v1_api.register(AttachmentsResource())

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/', include(v1_api.urls)),
]