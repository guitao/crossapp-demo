# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/guild/CrusadeCorps.proto',
  package='protoFile.guild.CrusadeCorps',
  serialized_pb='\n\"protoFile/guild/CrusadeCorps.proto\x12\x1cprotoFile.guild.CrusadeCorps\"2\n\x13\x43rusadeCorpsRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0f\n\x07\x63orpsId\x18\x02 \x02(\x05\"7\n\x14\x43rusadeCorpsResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t')




_CRUSADECORPSREQUEST = descriptor.Descriptor(
  name='CrusadeCorpsRequest',
  full_name='protoFile.guild.CrusadeCorps.CrusadeCorpsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.guild.CrusadeCorps.CrusadeCorpsRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='corpsId', full_name='protoFile.guild.CrusadeCorps.CrusadeCorpsRequest.corpsId', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=68,
  serialized_end=118,
)


_CRUSADECORPSRESPONSE = descriptor.Descriptor(
  name='CrusadeCorpsResponse',
  full_name='protoFile.guild.CrusadeCorps.CrusadeCorpsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.guild.CrusadeCorps.CrusadeCorpsResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.guild.CrusadeCorps.CrusadeCorpsResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=120,
  serialized_end=175,
)

DESCRIPTOR.message_types_by_name['CrusadeCorpsRequest'] = _CRUSADECORPSREQUEST
DESCRIPTOR.message_types_by_name['CrusadeCorpsResponse'] = _CRUSADECORPSRESPONSE

class CrusadeCorpsRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CRUSADECORPSREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.guild.CrusadeCorps.CrusadeCorpsRequest)

class CrusadeCorpsResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CRUSADECORPSRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.guild.CrusadeCorps.CrusadeCorpsResponse)

# @@protoc_insertion_point(module_scope)
