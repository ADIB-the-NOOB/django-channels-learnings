from . import models
from rest_framework import serializers

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Message
        fields = ('id', 'message', 'created_at', 'updated_at')