# myapp/api.py
from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import ReadOnlyAuthorization, DjangoAuthorization
from tastypie.serializers import Serializer
from .models import Apps, Email

class AppResource(ModelResource):

    class Meta:
        queryset = Apps.objects.all()
        resource_name = 'app'
        serializer = Serializer()
        authentication = ApiKeyAuthentication()
        authorization = ReadOnlyAuthorization()


class EmailResource(ModelResource):

    class Meta:
        queryset = Apps.objects.all()
        resource_name = 'email'
        serializer = Serializer()
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()