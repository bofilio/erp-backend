from rest_framework import serializers
from .models import *


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = "__all__"

class CourierSerializer(serializers.ModelSerializer):
    attachments = serializers.PrimaryKeyRelatedField(many=True,required=False, queryset=Attachment.objects.all())
    class Meta:
        model = Courier
        fields = '__all__'
        extra_fields = ['attachments']
        extra_kwargs = {'visible_a': {'allow_empty': True}}

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(CourierSerializer, self).get_field_names(declared_fields, info)
        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields


class ExpediteurSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expediteur
        fields = "__all__"

class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = "__all__"

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"

class TypeCourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeCourier
        fields = "__all__"



