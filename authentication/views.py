from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from authentication.models import User
from authentication.permission import IsAuthorOrReadOnly
from authentication.serializer import UserCreateSerializer, UserSerializerList, UserDeleteSerializer, \
    UserDetailSerializer


class UserCreateView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer


class Logout(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return JsonResponse(status=status.HTTP_200_OK)


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerList
    permission_classes = [IsAuthenticated]


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDeleteSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]

