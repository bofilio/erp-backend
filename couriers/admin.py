from django.contrib import admin
from .models import *
from inline_actions.admin import InlineActionsModelAdminMixin
from .util import Util
admin.site.site_header = "Application Courier"
admin.site.site_title = "Courier"
admin.site.index_title = "Bienvenu à l'application Courier"
from django.conf import settings
import os
media_root = settings.MEDIA_ROOT

@admin.register(Entity)
class ExpediteurAdmin(admin.ModelAdmin):
    list_display = ("name","email")
    search_fields = ("name","email")

@admin.register(TypeCourier)
class TypeCourierAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Classification)
class ClassificationAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ("file",)
##############
class AttachmentTabular(admin.TabularInline):
    model = Attachment
    extra = 1
@admin.register(Courier)
class CourierAdmin(InlineActionsModelAdminMixin,admin.ModelAdmin):
    list_display = ("objet","expediteur","date_expedition","date_arrivee","type","classification","status")
    inlines = [AttachmentTabular]
    autocomplete_fields = ("expediteur","destinataires","visible_a")
    inline_actions = ('send_by_mail',)
    def send_by_mail(self, request, obj:Courier, parent_obj):
        dists=obj.destinataires.all()
        attachments=list(obj.files.all())
        arr=list()
        files=list()
        for dist in dists:
            arr.append(dist.email)
        for attch in attachments:
            file=os.path.join(media_root,attch.file.name)
            print(file)
            files.append(file)
        print(arr)
        res=Util.send_email(subject=obj.objet,message=obj.objet,source="h.talha@al-mouradia.dz",to=arr,cc=[],attachments=files)
        print("response is " + str(res))
        obj.save()
    send_by_mail.short_description = 'envoyer email'
