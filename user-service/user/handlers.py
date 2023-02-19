from .services import UserService
from django_grpc_proto.py_grpc import user_pb2_grpc


def grpc_handlers(server):
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
