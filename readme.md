
```shell

    py -m grpc_tools.protoc --proto_path=./user/grpc/protos --python_out=./user/grpc --grpc_python_out=./user/grpc ./user/grpc/protos/user.proto
    
    cd product/grpc
    py -m grpc_tools.protoc --proto_path=./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/user.proto

```

```shell
    py manage.py grpcrunserver --dev
```