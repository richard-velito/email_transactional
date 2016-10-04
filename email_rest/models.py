from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Apps(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Email(models.Model):
    to = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    is_html = models.IntegerField(default=1)

class Attachments(models.Model):
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    body = models.TextField()
    type = models.CharField(max_length=100)