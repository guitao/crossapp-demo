# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/practice/pratice.proto',
  package='protoFile.practice.pratice',
  serialized_pb='\n protoFile/practice/pratice.proto\x12\x1aprotoFile.practice.pratice\"s\n\x0epraticeRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x11\n\tmonsterId\x18\x02 \x02(\x05\x12\x16\n\x0esingleExpBonus\x18\x03 \x02(\x05\x12\x14\n\x0cmonsterCount\x18\x04 \x02(\x05\x12\x14\n\x0cmonsterLevel\x18\x05 \x02(\x05\"h\n\x0fpraticeResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x34\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32&.protoFile.practice.pratice.DataPacket\"\x1c\n\nDataPacket\x12\x0e\n\x06status\x18\x01 \x01(\t')




_PRATICEREQUEST = descriptor.Descriptor(
  name='praticeRequest',
  full_name='protoFile.practice.pratice.praticeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.practice.pratice.praticeRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='monsterId', full_name='protoFile.practice.pratice.praticeRequest.monsterId', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='singleExpBonus', full_name='protoFile.practice.pratice.praticeRequest.singleExpBonus', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='monsterCount', full_name='protoFile.practice.pratice.praticeRequest.monsterCount', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='monsterLevel', full_name='protoFile.practice.pratice.praticeRequest.monsterLevel', index=4,
      number=5, type=5, cpp_type=1, label=2,
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
  serialized_start=64,
  serialized_end=179,
)


_PRATICERESPONSE = descriptor.Descriptor(
  name='praticeResponse',
  full_name='protoFile.practice.pratice.praticeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.practice.pratice.praticeResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.practice.pratice.praticeResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='protoFile.practice.pratice.praticeResponse.data', index=2,
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
  serialized_end=285,
)


_DATAPACKET = descriptor.Descriptor(
  name='DataPacket',
  full_name='protoFile.practice.pratice.DataPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='status', full_name='protoFile.practice.pratice.DataPacket.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=287,
  serialized_end=315,
)

_PRATICERESPONSE.fields_by_name['data'].message_type = _DATAPACKET
DESCRIPTOR.message_types_by_name['praticeRequest'] = _PRATICEREQUEST
DESCRIPTOR.message_types_by_name['praticeResponse'] = _PRATICERESPONSE
DESCRIPTOR.message_types_by_name['DataPacket'] = _DATAPACKET

class praticeRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PRATICEREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.practice.pratice.praticeRequest)

class praticeResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PRATICERESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.practice.pratice.praticeResponse)

class DataPacket(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DATAPACKET
  
  # @@protoc_insertion_point(class_scope:protoFile.practice.pratice.DataPacket)

# @@protoc_insertion_point(module_scope)
