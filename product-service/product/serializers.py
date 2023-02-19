import grpc
from rest_framework import serializers
from django.conf import settings
from django_grpc_proto.py_grpc import user_pb2_grpc, user_pb2
from .models import Product

USER_GRPC_SERVER = settings.USER_GRPC_SERVER


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'owner_id': {'write_only': True}
        }

    def create(self, validated_data):
        owner_id = validated_data.get('owner_id', None)
        if owner_id:
            with grpc.insecure_channel(USER_GRPC_SERVER) as channel:
                stub = user_pb2_grpc.UserServiceStub(channel)
                res = stub.GetUser(user_pb2.UserRetrieveRequest(id=str(owner_id)))
                print(res, end='')
        return super().create(validated_data)

    def get_owner(self, instance):
        owner = {}
        with grpc.insecure_channel(USER_GRPC_SERVER) as channel:
            stub = user_pb2_grpc.UserServiceStub(channel)
            res = stub.GetUser(user_pb2.UserRetrieveRequest(id=str(instance.owner_id)))
            if res:
                owner.update({'id': res.id, 'email': res.email, 'firstname': res.firstname, 'lastname': res.lastname})
        return owner

