from django.shortcuts import render
import json
from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import FileUploadParser

from .serializers import JsonSerializer
from .models import jsonData
# Create your views here.


def convert_json(data):
    '''
        validation for user uploaded json file
    '''
    data = data.read().decode('utf-8')
    data = data.replace('\n', '')
    data = data.replace('\r', '')
    return json.loads(data)


class jsonViewSet(viewsets.ModelViewSet):
    serializer_class = JsonSerializer
    queryset = jsonData.objects.all()

    # permission_classes = (,)
    parser_class = (FileUploadParser,)

    def create(self, request, *args, **kwargs):

        data = request.data.pop('data', None)[0]
        try:
            if data:
                if 'json' in data.content_type.split('/')[1]:
                    query_data = convert_json(data)
                    serializer_data = self.serializer_class(data=query_data, many=True)
                    serializer_data.is_valid(raise_exception=True)
                    self.perform_create(serializer_data)
                    return Response(serializer_data.data)
                else:
                    return Response({'filepath': ['upload json document']})
        except:
            return Response({'error': 'Data already exists'})


