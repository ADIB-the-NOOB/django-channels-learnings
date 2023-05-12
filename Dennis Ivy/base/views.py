from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from . import models, serializers
# Create your views here.

def index(request):
    return render(request, 'index.html')

class MessageView(views.APIView):
    def get(self, request, *args, **kwargs):
        msg_obj = models.Message.objects.all()
        serializer = serializers.MessageSerializer(msg_obj, many=True)
        return Response(serializer.data)
    