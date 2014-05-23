# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/lobby/restOperate.proto',
  package='protoFile.lobby.restOperate',
  serialized_pb='\n!protoFile/lobby/restOperate.proto\x12\x1bprotoFile.lobby.restOperate\"O\n\x12restOperateRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0c\n\x04type\x18\x02 \x02(\t\x12\x0f\n\x07payType\x18\x03 \x02(\t\x12\x0e\n\x06payNum\x18\x04 \x02(\x05\"m\n\x13restOperateResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x35\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\'.protoFile.lobby.restOperate.DataPacket\"}\n\nDataPacket\x12\n\n\x02hp\x18\x01 \x01(\x05\x12\n\n\x02mp\x18\x02 \x01(\x05\x12\x0e\n\x06\x65nergy\x18\x03 \x01(\x05\x12\x0c\n\x04gold\x18\x04 \x01(\x05\x12\x0e\n\x06\x63oupon\x18\x05 \x01(\x05\x12\x0c\n\x04\x63oin\x18\x06 \x01(\x05\x12\x0c\n\x04type\x18\x07 \x01(\t\x12\r\n\x05\x63ount\x18\x08 \x01(\x05')




_RESTOPERATEREQUEST = descriptor.Descriptor(
  name='restOperateRequest',
  full_name='protoFile.lobby.restOperate.restOperateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.lobby.restOperate.restOperateRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='protoFile.lobby.restOperate.restOperateRequest.type', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='payType', full_name='protoFile.lobby.restOperate.restOperateRequest.payType', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='payNum', full_name='protoFile.lobby.restOperate.restOperateRequest.payNum', index=3,
      number=4, type=5, cpp_type=1, label=2,
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
  serialized_start=66,
  serialized_end=145,
)


_RESTOPERATERESPONSE = descriptor.Descriptor(
  name='restOperateResponse',
  full_name='protoFile.lobby.restOperate.restOperateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.lobby.restOperate.restOperateResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.lobby.restOperate.restOperateResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='protoFile.lobby.restOperate.restOperateResponse.data', index=2,
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
  serialized_start=147,
  serialized_end=256,
)


_DATAPACKET = descriptor.Descriptor(
  name='DataPacket',
  full_name='protoFile.lobby.restOperate.DataPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='hp', full_name='protoFile.lobby.restOperate.DataPacket.hp', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='mp', full_name='protoFile.lobby.restOperate.DataPacket.mp', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='energy', full_name='protoFile.lobby.restOperate.DataPacket.energy', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='gold', full_name='protoFile.lobby.restOperate.DataPacket.gold', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='coupon', full_name='protoFile.lobby.restOperate.DataPacket.coupon', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='coin', full_name='protoFile.lobby.restOperate.DataPacket.coin', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='protoFile.lobby.restOperate.DataPacket.type', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='count', full_name='protoFile.lobby.restOperate.DataPacket.count', index=7,
      number=8, type=5, cpp_type=1, label=1,
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
  serialized_start=258,
  serialized_end=383,
)

_RESTOPERATERESPONSE.fields_by_name['data'].message_type = _DATAPACKET
DESCRIPTOR.message_types_by_name['restOperateRequest'] = _RESTOPERATEREQUEST
DESCRIPTOR.message_types_by_name['restOperateResponse'] = _RESTOPERATERESPONSE
DESCRIPTOR.message_types_by_name['DataPacket'] = _DATAPACKET

class restOperateRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESTOPERATEREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.lobby.restOperate.restOperateRequest)

class restOperateResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESTOPERATERESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.lobby.restOperate.restOperateResponse)

class DataPacket(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DATAPACKET
  
  # @@protoc_insertion_point(class_scope:protoFile.lobby.restOperate.DataPacket)

# @@protoc_insertion_point(module_scope)
