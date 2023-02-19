from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ["email", "firstname", "id", "is_active", "lastname", "role"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    LASTNAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    email: str
    firstname: str
    id: str
    is_active: bool
    lastname: str
    role: str
    def __init__(self, id: _Optional[str] = ..., email: _Optional[str] = ..., firstname: _Optional[str] = ..., lastname: _Optional[str] = ..., role: _Optional[str] = ..., is_active: bool = ...) -> None: ...

class UserListRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UserRetrieveRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...
