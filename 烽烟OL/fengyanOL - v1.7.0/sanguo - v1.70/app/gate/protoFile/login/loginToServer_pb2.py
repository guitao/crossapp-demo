# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/login/loginToServer.proto',
  package='protoFile.login.loginToServer',
  serialized_pb='\n#protoFile/login/loginToServer.proto\x12\x1dprotoFile.login.loginToServer\"6\n\x14loginToServerRequest\x12\x0c\n\x04user\x18\x01 \x02(\t\x12\x10\n\x08password\x18\x02 \x02(\t\"o\n\x15loginToServerResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x35\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\'.protoFile.login.loginToServer.UserInfo\"v\n\x08UserInfo\x12\x0e\n\x06userId\x18\x01 \x01(\x05\x12\x0b\n\x03len\x18\x02 \x01(\x05\x12\x11\n\tdefaultId\x18\x03 \x01(\x05\x12:\n\tcharacter\x18\x04 \x03(\x0b\x32\'.protoFile.login.loginToServer.RoleInfo\"\\\n\x08RoleInfo\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08nickname\x18\x02 \x01(\t\x12\r\n\x05level\x18\x03 \x01(\x05\x12\x12\n\nprofession\x18\x04 \x01(\t\x12\x0f\n\x07viptype\x18\x05 \x01(\x05')




_LOGINTOSERVERREQUEST = descriptor.Descriptor(
  name='loginToServerRequest',
  full_name='protoFile.login.loginToServer.loginToServerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='user', full_name='protoFile.login.loginToServer.loginToServerRequest.user', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='password', full_name='protoFile.login.loginToServer.loginToServerRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=70,
  serialized_end=124,
)


_LOGINTOSERVERRESPONSE = descriptor.Descriptor(
  name='loginToServerResponse',
  full_name='protoFile.login.loginToServer.loginToServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.login.loginToServer.loginToServerResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.login.loginToServer.loginToServerResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='protoFile.login.loginToServer.loginToServerResponse.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=126,
  serialized_end=237,
)


_USERINFO = descriptor.Descriptor(
  name='UserInfo',
  full_name='protoFile.login.loginToServer.UserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='userId', full_name='protoFile.login.loginToServer.UserInfo.userId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='len', full_name='protoFile.login.loginToServer.UserInfo.len', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='defaultId', full_name='protoFile.login.loginToServer.UserInfo.defaultId', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='character', full_name='protoFile.login.loginToServer.UserInfo.character', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=239,
  serialized_end=357,
)


_ROLEINFO = descriptor.Descriptor(
  name='RoleInfo',
  full_name='protoFile.login.loginToServer.RoleInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.login.loginToServer.RoleInfo.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='nickname', full_name='protoFile.login.loginToServer.RoleInfo.nickname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='level', full_name='protoFile.login.loginToServer.RoleInfo.level', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='profession', full_name='protoFile.login.loginToServer.RoleInfo.profession', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='viptype', full_name='protoFile.login.loginToServer.RoleInfo.viptype', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=359,
  serialized_end=451,
)

_LOGINTOSERVERRESPONSE.fields_by_name['data'].message_type = _USERINFO
_USERINFO.fields_by_name['character'].message_type = _ROLEINFO
DESCRIPTOR.message_types_by_name['loginToServerRequest'] = _LOGINTOSERVERREQUEST
DESCRIPTOR.message_types_by_name['loginToServerResponse'] = _LOGINTOSERVERRESPONSE
DESCRIPTOR.message_types_by_name['UserInfo'] = _USERINFO
DESCRIPTOR.message_types_by_name['RoleInfo'] = _ROLEINFO

class loginToServerRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOGINTOSERVERREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.login.loginToServer.loginToServerRequest)

class loginToServerResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOGINTOSERVERRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.login.loginToServer.loginToServerResponse)

class UserInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _USERINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.login.loginToServer.UserInfo)

class RoleInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROLEINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.login.loginToServer.RoleInfo)

# @@protoc_insertion_point(module_scope)
