from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Apps(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    class Meta:
        verbose_name = 'App'
        verbose_name_plural = 'Apps'
    def __unicode__(self):
        return 'app : ' + self.name

class Email(models.Model):
    to = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    tag = models.CharField(max_length=255, default="", blank=True, null=True)
    is_html = models.IntegerField(default=1, blank=True, null=True)
    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'
    def __unicode__(self):
        return 'email : ' + self.subject

class Attachments(models.Model):
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    path = models.TextField()
    type = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Attachment'
        verbose_name_plural = 'Attachments'