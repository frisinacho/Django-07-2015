# -*- coding: utf-8 -*-
from files.models import File
from rest_framework.viewsets import ModelViewSet
from files.serializers import FileSerializer


class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer