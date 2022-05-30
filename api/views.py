from django.shortcuts import render
import json
from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import FileUploadParser
from rest_framework.decorators import action

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
    '''
        Viewset for list and upload json data
    '''
    serializer_class = JsonSerializer
    queryset = jsonData.objects.all()

    permission_classes = (AllowAny,)
    parser_class = (FileUploadParser,)

    def create(self, request, *args, **kwargs):
        data = request.data.pop('data', None)
        try:
            if data:
                data = data[0]
                if 'json' in data.content_type.split('/')[1]:
                    query_data = convert_json(data)
                    serializer_data = self.serializer_class(data=query_data, many=True)
                    serializer_data.is_valid(raise_exception=True)
                    self.perform_create(serializer_data)
                    return Response(serializer_data.data)
                else:
                    return Response({'filepath': ['upload json document']}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'No data attached'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'Data already exists'}, status=status.HTTP_400_BAD_REQUEST)


    @action(methods=['post'], detail=False)
    def delete(self, request, *args, **kwargs):
        '''

        :param request:
        :param args:
        :param kwargs:
        :return:
            API for delete JSON data
        '''

        data = jsonData.objects.all()
        data.delete()
        return Response({'success': 'Data deleted successfully !! '}, status=status.HTTP_202_ACCEPTED)