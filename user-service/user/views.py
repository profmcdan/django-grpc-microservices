from django.contrib.auth import get_user_model
from rest_framework import viewsets, filters

from .serializers import UserSerializer, CreateUserSerializer
from .models import User, Token


class UserViewSets(viewsets.ModelViewSet):
    """User ViewSets"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.action in ['create', 'partial_update']:
            return CreateUserSerializer
        return super().get_serializer_class()

