# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/afk/DianShiChengJi2802.proto',
  package='protoFile.afk.DianShiChengJi2802',
  serialized_pb='\n&protoFile/afk/DianShiChengJi2802.proto\x12 protoFile.afk.DianShiChengJi2802\"#\n\x15\x44ianShiChengJiRequest\x12\n\n\x02id\x18\x01 \x02(\x05\"9\n\x16\x44ianShiChengJiResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\x08')




_DIANSHICHENGJIREQUEST = descriptor.Descriptor(
  name='DianShiChengJiRequest',
  full_name='protoFile.afk.DianShiChengJi2802.DianShiChengJiRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.afk.DianShiChengJi2802.DianShiChengJiRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
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
  serialized_start=76,
  serialized_end=111,
)


_DIANSHICHENGJIRESPONSE = descriptor.Descriptor(
  name='DianShiChengJiResponse',
  full_name='protoFile.afk.DianShiChengJi2802.DianShiChengJiResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.afk.DianShiChengJi2802.DianShiChengJiResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.afk.DianShiChengJi2802.DianShiChengJiResponse.result', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=113,
  serialized_end=170,
)

DESCRIPTOR.message_types_by_name['DianShiChengJiRequest'] = _DIANSHICHENGJIREQUEST
DESCRIPTOR.message_types_by_name['DianShiChengJiResponse'] = _DIANSHICHENGJIRESPONSE

class DianShiChengJiRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DIANSHICHENGJIREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.afk.DianShiChengJi2802.DianShiChengJiRequest)

class DianShiChengJiResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DIANSHICHENGJIRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.afk.DianShiChengJi2802.DianShiChengJiResponse)

# @@protoc_insertion_point(module_scope)
