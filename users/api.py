# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from users.permissions import UserPermission
from users.serializers import UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status


class UserListAPI(GenericAPIView):

    pagination_class = PageNumberPagination
    permission_classes = (UserPermission,)

    def get(self, request):
        users = User.objects.all()
        self.paginate_queryset(users)  # pagino el resultado
        serializer = UserSerializer(users, many=True)
        return self.get_paginated_response(serializer.data)  # devuelvo una respuesta paginada

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPI(GenericAPIView):

    permission_classes = (UserPermission,)

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)  # compruebo si el usuario autenticado puede hacer GET en este user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)  # compruebo si el usuario autenticado puede hacer PUT en este user
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)  # compruebo si el usuario autenticado puede hacer DELETE en este user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)