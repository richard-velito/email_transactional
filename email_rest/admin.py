from django.contrib import admin

# Register your models here.
from .models import Apps, Email, Attachments



class AttachmentsInline(admin.TabularInline):
    model = Attachments

class EmailAdmin(admin.ModelAdmin):
    inlines = [
        AttachmentsInline,
    ]

admin.site.register(Apps)
admin.site.register(Email, EmailAdmin)