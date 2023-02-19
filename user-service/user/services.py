import grpc
from google.protobuf import empty_pb2
from django_grpc_framework.services import Service
from .models import User
from .serializers import UserProtoSerializer
# from .grpc import user_pb2_grpc
from django_grpc_proto.py_grpc import user_pb2_grpc


class UserService(user_pb2_grpc.UserServiceServicer):
    def ListUsers(self, request, context):
        users = User.objects.all()
        serializer = UserProtoSerializer(users, many=True)
        for msg in serializer.message:
            yield msg

    def CreateUser(self, request, context):
        serializer = UserProtoSerializer(message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def get_object(self, pk):
        user = User.objects.filter(pk=pk).first()
        if not user:
            self.context.abort(grpc.StatusCode.NOT_FOUND, f'User {pk} not found')
        return user

    def GetUser(self, request, context):
        user = self.get_object(request.id)
        serializer = UserProtoSerializer(user)
        return serializer.message

    def UpdateUser(self, request, context):
        user = self.get_object(request.id)
        serializer = UserProtoSerializer(user, message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def DeleteUser(self, request, context):
        user = self.get_object(request.id)
        user.delete()
        return empty_pb2.Empty()
