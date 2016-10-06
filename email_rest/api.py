# myapp/api.py
from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import ReadOnlyAuthorization
from tastypie.serializers import Serializer
from .models import Apps

class AppResource(ModelResource):

    class Meta:
        queryset = Apps.objects.all()
        resource_name = 'app'
        authentication = ApiKeyAuthentication()
        serializer = Serializer()
        authorization = ReadOnlyAuthorization()

