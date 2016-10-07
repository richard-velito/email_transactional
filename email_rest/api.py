# myapp/api.py
from django.conf.urls import url
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from tastypie.http import HttpGone, HttpMultipleChoices
from tastypie.fields import ForeignKey
from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import ReadOnlyAuthorization, DjangoAuthorization
from tastypie.serializers import Serializer
from tastypie.utils import trailing_slash
from .models import Apps, Email, Attachments

from .services import Helper

class AppResource(ModelResource):

    class Meta:
        queryset = Apps.objects.all()
        resource_name = 'app'
        serializer = Serializer()
        allowed_methods = ['get']
        authentication = ApiKeyAuthentication()
        authorization = ReadOnlyAuthorization()

class EmailResource(ModelResource):

    class Meta:
        queryset = Email.objects.all()
        resource_name = 'email'
        serializer = Serializer()
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()

    #send email
    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/(?P<pk>\w[\w/-]*)/send_email%s$" % (self._meta.resource_name, trailing_slash()),
                self.wrap_view('send_email'), name="api_send_email"),
            url(r"^(?P<resource_name>%s)/get_events%s$" % (self._meta.resource_name, trailing_slash()),
                self.wrap_view('get_events'), name="api_get_events"),
        ]

    def send_email(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        self.is_authenticated(request)

        try:
            bundle = self.build_bundle(data={'pk': kwargs['pk']}, request=request)
            obj = self.cached_obj_get(bundle=bundle, **self.remove_api_resource_names(kwargs))
        except ObjectDoesNotExist:
            return HttpGone()
        except MultipleObjectsReturned:
            return HttpMultipleChoices("More than one resource is found at this URI.")

        results = Helper().send_email(obj.pk)

        result_list = {
            'results': results,
        }

        return self.create_response(request, result_list)

    def get_events(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        self.is_authenticated(request)

        result_list = {
            'results': Helper().get_logs_events().json(),
        }

        return self.create_response(request, result_list)


class AttachmentsResource(ModelResource):
    email = ForeignKey(EmailResource, 'email')
    class Meta:
        queryset = Attachments.objects.all()
        resource_name = 'attachments'
        serializer = Serializer()
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()