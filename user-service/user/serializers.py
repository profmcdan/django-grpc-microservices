from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from django.utils.crypto import get_random_string
from rest_framework import serializers
from django_grpc_framework.proto_serializers import ModelProtoSerializer

from .models import User, Token
# from .grpc import user_pb2
from django_grpc_proto.py_grpc import user_pb2


class UserProtoSerializer(ModelProtoSerializer):
    class Meta:
        model = User
        proto_class = user_pb2.User
        fields = ['id', 'firstname', 'lastname', 'email', 'role', 'is_active']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'firstname', 'lastname', 'email', 'role', 'is_active']


class CreateUserSerializer(serializers.ModelSerializer):
    """Serializer for creating user object"""

    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'firstname', 'lastname', 'phone', 'image', 'role', 'created_at']

    def validate(self, attrs):
        if not self.instance:
            email = attrs.get('email', None)
            if email:
                email = attrs['email'].lower().strip()
                if get_user_model().objects.filter(email=email).exists():
                    raise serializers.ValidationError('Email already exists')
                # try:
                #     valid = validate_email(attrs['email'])
                #     attrs['email'] = valid.email
                #     return super().validate(attrs)
                # except Exception as e:
                #     raise serializers.ValidationError({'email': 'Invalid Email', 'e': e})
        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create_user(password='Password@@1', **validated_data)
        token, _ = Token.objects.update_or_create(
            user=user, token_type='ACCOUNT_VERIFICATION',
            defaults={'user': user, 'token_type': 'ACCOUNT_VERIFICATION',
                      'token': get_random_string(120)})
        # user_data = {
        #     'id': user.id, 'email': user.email,
        #     'fullname': f"{user.lastname} {user.firstname}",
        #     'url': f"{settings.CLIENT_URL}/create-password/?token={token.token}"}
        # send_new_user_email.delay(user_data)
        return user

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        if validated_data.get('password', False):
            instance.set_password(validated_data.get('password'))
        instance.save()
        return instance
