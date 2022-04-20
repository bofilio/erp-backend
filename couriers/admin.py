from django.contrib import admin,messages
from .models import *
from inline_actions.admin import InlineActionsModelAdminMixin
from commun.util import Util
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

media_root = settings.MEDIA_ROOT
admin.site.site_header = "Application Courier"
admin.site.site_title = "Courier"
admin.site.index_title = "Bienvenu à l'application Courier"



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
    list_display = ("name","file",)
##############
class AttachmentTabular(admin.TabularInline):
    model = Attachment
    extra = 1
@admin.register(Courier)
class CourierAdmin(InlineActionsModelAdminMixin,admin.ModelAdmin):
    inlines = [AttachmentTabular]
    autocomplete_fields = ("expediteur","destinataires","visible_a")
    inline_actions = ('send_by_mail','delete')
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return  qs.filter(deleted=False)
    def get_list_display(self, request):
        list=("objet","expediteur","date_expedition","date_arrivee","type","classification","status")
        if request.user.is_superuser:
            return list+('deleted',)+ (super().get_list_display(request).pop(),)
        return list+(super().get_list_display(request).pop(),)

    def send_by_mail(self, request, obj:Courier, parent_obj):
        dists=obj.visible_a.all()
        to=[]
        for dist in dists:
            to.append(dist.getExpediteur().email)
        source=obj.expediteur.getExpediteur().email
        attachments=list(obj.attachments.all())
        arr=list()
        files=list()
        for dist in dists:
            arr.append(dist.email)
        for attch in attachments:
            files.append(attch.file.name)
        try:
            res=Util.send_email(subject=obj.objet, message=obj.objet, source=source, to=to, cc=[], attachments=files)
            messages.success(request, _("Email Envoyé"))
        except Exception :
            messages.error(request, _("Erreur d'envoie"))

    send_by_mail.short_description = 'envoyer email'

    def delete(self, request, obj:Courier, parent_obj):
        obj.deleted=True
        obj.save()
    delete.short_description = 'supprimer'
