# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/friend/searchCharacterByName.proto',
  package='protoFile.friend.searchCharacterByName',
  serialized_pb='\n,protoFile/friend/searchCharacterByName.proto\x12&protoFile.friend.searchCharacterByName\"[\n\x1csearchCharacterByNameRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x10\n\x08nickName\x18\x02 \x02(\t\x12\x0e\n\x06ziduan\x18\x03 \x01(\x05\x12\r\n\x05guize\x18\x04 \x01(\x05\"\x7f\n\x1dsearchCharacterByNameResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12=\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32/.protoFile.friend.searchCharacterByName.Friends\"J\n\x07\x46riends\x12?\n\x07\x66riends\x18\x01 \x03(\x0b\x32..protoFile.friend.searchCharacterByName.Friend\"\x81\x01\n\x06\x46riend\x12\x0e\n\x06roleId\x18\x01 \x01(\x05\x12\x10\n\x08roleName\x18\x02 \x01(\t\x12\x16\n\x0eroleProfession\x18\x03 \x01(\x05\x12\r\n\x05level\x18\x04 \x01(\x05\x12\x0c\n\x04\x63omp\x18\x05 \x01(\t\x12\x14\n\x0clastLoadTime\x18\x06 \x01(\t\x12\n\n\x02zx\x18\x07 \x01(\x05')




_SEARCHCHARACTERBYNAMEREQUEST = descriptor.Descriptor(
  name='searchCharacterByNameRequest',
  full_name='protoFile.friend.searchCharacterByName.searchCharacterByNameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.friend.searchCharacterByName.searchCharacterByNameRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='nickName', full_name='protoFile.friend.searchCharacterByName.searchCharacterByNameRequest.nickName', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ziduan', full_name='protoFile.friend.searchCharacterByName.searchCharacterByNameRequest.ziduan', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='guize', full_name='protoFile.friend.searchCharacterByName.searchCharacterByNameRequest.guize', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=88,
  serialized_end=179,
)


_SEARCHCHARACTERBYNAMERESPONSE = descriptor.Descriptor(
  name='searchCharacterByNameResponse',
  full_name='protoFile.friend.searchCharacterByName.searchCharacterByNameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.friend.searchCharacterByName.searchCharacterByNameResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.friend.searchCharacterByName.searchCharacterByNameResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='protoFile.friend.searchCharacterByName.searchCharacterByNameResponse.data', index=2,
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
  serialized_start=181,
  serialized_end=308,
)


_FRIENDS = descriptor.Descriptor(
  name='Friends',
  full_name='protoFile.friend.searchCharacterByName.Friends',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='friends', full_name='protoFile.friend.searchCharacterByName.Friends.friends', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=310,
  serialized_end=384,
)


_FRIEND = descriptor.Descriptor(
  name='Friend',
  full_name='protoFile.friend.searchCharacterByName.Friend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='roleId', full_name='protoFile.friend.searchCharacterByName.Friend.roleId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='roleName', full_name='protoFile.friend.searchCharacterByName.Friend.roleName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='roleProfession', full_name='protoFile.friend.searchCharacterByName.Friend.roleProfession', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='level', full_name='protoFile.friend.searchCharacterByName.Friend.level', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='comp', full_name='protoFile.friend.searchCharacterByName.Friend.comp', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='lastLoadTime', full_name='protoFile.friend.searchCharacterByName.Friend.lastLoadTime', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='zx', full_name='protoFile.friend.searchCharacterByName.Friend.zx', index=6,
      number=7, type=5, cpp_type=1, label=1,
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
  serialized_start=387,
  serialized_end=516,
)

_SEARCHCHARACTERBYNAMERESPONSE.fields_by_name['data'].message_type = _FRIENDS
_FRIENDS.fields_by_name['friends'].message_type = _FRIEND
DESCRIPTOR.message_types_by_name['searchCharacterByNameRequest'] = _SEARCHCHARACTERBYNAMEREQUEST
DESCRIPTOR.message_types_by_name['searchCharacterByNameResponse'] = _SEARCHCHARACTERBYNAMERESPONSE
DESCRIPTOR.message_types_by_name['Friends'] = _FRIENDS
DESCRIPTOR.message_types_by_name['Friend'] = _FRIEND

class searchCharacterByNameRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SEARCHCHARACTERBYNAMEREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.friend.searchCharacterByName.searchCharacterByNameRequest)

class searchCharacterByNameResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SEARCHCHARACTERBYNAMERESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.friend.searchCharacterByName.searchCharacterByNameResponse)

class Friends(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FRIENDS
  
  # @@protoc_insertion_point(class_scope:protoFile.friend.searchCharacterByName.Friends)

class Friend(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FRIEND
  
  # @@protoc_insertion_point(class_scope:protoFile.friend.searchCharacterByName.Friend)

# @@protoc_insertion_point(module_scope)
