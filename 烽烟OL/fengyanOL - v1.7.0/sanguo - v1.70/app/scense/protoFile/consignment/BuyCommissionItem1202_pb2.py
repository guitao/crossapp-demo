# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/consignment/BuyCommissionItem1202.proto',
  package='protoFile.consignment.BuyCommissionItem1202',
  serialized_pb='\n1protoFile/consignment/BuyCommissionItem1202.proto\x12+protoFile.consignment.BuyCommissionItem1202\"J\n\x18\x42uyCommissionItemRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x14\n\x0c\x63ommissionId\x18\x02 \x02(\x05\x12\x0c\n\x04type\x18\x03 \x02(\x05\"<\n\x19\x42uyCommissionItemResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t')




_BUYCOMMISSIONITEMREQUEST = descriptor.Descriptor(
  name='BuyCommissionItemRequest',
  full_name='protoFile.consignment.BuyCommissionItem1202.BuyCommissionItemRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.consignment.BuyCommissionItem1202.BuyCommissionItemRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='commissionId', full_name='protoFile.consignment.BuyCommissionItem1202.BuyCommissionItemRequest.commissionId', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='protoFile.consignment.BuyCommissionItem1202.BuyCommissionItemRequest.type', index=2,
      number=3, type=5, cpp_type=1, label=2,
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
  serialized_start=98,
  serialized_end=172,
)


_BUYCOMMISSIONITEMRESPONSE = descriptor.Descriptor(
  name='BuyCommissionItemResponse',
  full_name='protoFile.consignment.BuyCommissionItem1202.BuyCommissionItemResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.consignment.BuyCommissionItem1202.BuyCommissionItemResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.consignment.BuyCommissionItem1202.BuyCommissionItemResponse.message', index=1,
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
  serialized_start=174,
  serialized_end=234,
)

DESCRIPTOR.message_types_by_name['BuyCommissionItemRequest'] = _BUYCOMMISSIONITEMREQUEST
DESCRIPTOR.message_types_by_name['BuyCommissionItemResponse'] = _BUYCOMMISSIONITEMRESPONSE

class BuyCommissionItemRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BUYCOMMISSIONITEMREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.consignment.BuyCommissionItem1202.BuyCommissionItemRequest)

class BuyCommissionItemResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BUYCOMMISSIONITEMRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.consignment.BuyCommissionItem1202.BuyCommissionItemResponse)

# @@protoc_insertion_point(module_scope)
