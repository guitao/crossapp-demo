# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/guild/GetSingleUnionListRequest1322.proto',
  package='protoFile.guild.GetSingleUnionListRequest1322',
  serialized_pb='\n3protoFile/guild/GetSingleUnionListRequest1322.proto\x12-protoFile.guild.GetSingleUnionListRequest1322\"9\n\x19GetSingleUnionInfoRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x10\n\x08union_id\x18\x02 \x01(\x05\"\x8f\x02\n\x1aGetSingleUnionInfoResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07\x63orpsId\x18\x02 \x01(\x05\x12\x10\n\x08\x63orpsImg\x18\x03 \x01(\x05\x12\x11\n\tcorpsName\x18\x04 \x01(\t\x12\x12\n\ncorpsChief\x18\x05 \x01(\t\x12\x12\n\ncorpsLevel\x18\x06 \x01(\x05\x12\x0e\n\x06\x63urNum\x18\x07 \x01(\x05\x12\x0e\n\x06maxNum\x18\x08 \x01(\x05\x12\x15\n\ronApplication\x18\t \x01(\x08\x12\x12\n\ncorpsTitle\x18\n \x01(\t\x12\x19\n\x11\x63orpsAnnouncement\x18\x0b \x01(\t\x12\x10\n\x08leaderId\x18\x0c \x01(\x05\x12\x0b\n\x03msg\x18\r \x01(\t')




_GETSINGLEUNIONINFOREQUEST = descriptor.Descriptor(
  name='GetSingleUnionInfoRequest',
  full_name='protoFile.guild.GetSingleUnionListRequest1322.GetSingleUnionInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.guild.GetSingleUnionListRequest1322.GetSingleUnionInfoRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='union_id', full_name='protoFile.guild.GetSingleUnionListRequest1322.GetSingleUnionInfoRequest.union_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=102,
  serialized_end=159,
)


_GETSINGLEUNIONINFORESPONSE = descriptor.Descriptor(
  name='GetSingleUnionInfoResponse',
  full_name='protoFile.guild.GetSingleUnionListRequest1322.GetSingleUnionInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.guild.GetSingleUnionListRequest1322.GetSingleUnionInfoResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='corpsId', full_name='protoFile.guild.GetSingleUnionListRequest1322.GetSingleUnionInfoResponse.corpsId', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='corpsImg', full_name='protoFile.guild.GetSingleUnionListRequest1322.GetSingleUnionInfoResponse.corpsImg', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='corpsName', full_name='protoFile.guild.GetSingleUnionListRequest1322.GetSingleUnionInfoResponse.corpsName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='corpsChief', full_name='protoFile.guild.GetSingleUnionListRequest1322.GetSingleUnionInfoResponse.corpsChief', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='corpsLevel', full_name='protoFile.guild.GetSingleUnionListRequest1322.GetSingleUnionInfoResponse.corpsLevel', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='curNum', full_name='protoFile.guild.GetSingleUnionListRequest1322.GetSingleUnionInfoResponse.curNum', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='maxNum', full_name='protoFile.guild.GetSingleUnionListRequest1322.GetSingleUnionInfoResponse.maxNum', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='onApplication', full_name='protoFile.guild.GetSingleUnionListRequest1322.GetSingleUnionInfoResponse.onApplication', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='corpsTitle', full_name='protoFile.guild.GetSingleUnionListRequest1322.GetSingleUnionInfoResponse.corpsTitle', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='corpsAnnouncement', full_name='protoFile.guild.GetSingleUnionListRequest1322.GetSingleUnionInfoResponse.corpsAnnouncement', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='leaderId', full_name='protoFile.guild.GetSingleUnionListRequest1322.GetSingleUnionInfoResponse.leaderId', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='msg', full_name='protoFile.guild.GetSingleUnionListRequest1322.GetSingleUnionInfoResponse.msg', index=12,
      number=13, type=9, cpp_type=9, label=1,
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
  serialized_start=162,
  serialized_end=433,
)

DESCRIPTOR.message_types_by_name['GetSingleUnionInfoRequest'] = _GETSINGLEUNIONINFOREQUEST
DESCRIPTOR.message_types_by_name['GetSingleUnionInfoResponse'] = _GETSINGLEUNIONINFORESPONSE

class GetSingleUnionInfoRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETSINGLEUNIONINFOREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.guild.GetSingleUnionListRequest1322.GetSingleUnionInfoRequest)

class GetSingleUnionInfoResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETSINGLEUNIONINFORESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.guild.GetSingleUnionListRequest1322.GetSingleUnionInfoResponse)

# @@protoc_insertion_point(module_scope)
