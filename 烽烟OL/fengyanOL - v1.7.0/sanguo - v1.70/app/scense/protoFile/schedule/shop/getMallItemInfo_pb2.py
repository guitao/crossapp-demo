# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/shop/getMallItemInfo.proto',
  package='protoFile.shop.getMallItemInfo',
  serialized_pb='\n$protoFile/shop/getMallItemInfo.proto\x12\x1eprotoFile.shop.getMallItemInfo\"F\n\x16getMallItemInfoRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x12\n\ncategories\x18\x02 \x02(\x05\x12\x0c\n\x04page\x18\x03 \x02(\x05\"v\n\x17getMallItemInfoResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12:\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32,.protoFile.shop.getMallItemInfo.ResponseData\"i\n\x0cResponseData\x12\x12\n\ncategories\x18\x01 \x01(\x05\x12\x0c\n\x04goal\x18\x02 \x01(\x05\x12\x37\n\x05items\x18\x03 \x03(\x0b\x32(.protoFile.shop.getMallItemInfo.ItemIifo\"\xaf\x03\n\x08ItemIifo\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0c\n\x04icon\x18\x04 \x01(\t\x12\x14\n\x0cqualityLevel\x18\x05 \x01(\x05\x12\x14\n\x0clevelRequire\x18\x06 \x01(\x05\x12\x11\n\tminDamage\x18\x07 \x01(\x05\x12\x11\n\tmaxDamage\x18\x08 \x01(\x05\x12\x0f\n\x07\x64\x65\x66\x65nse\x18\t \x01(\x05\x12\x19\n\x11professionRequire\x18\n \x01(\x05\x12\x12\n\nstrRequire\x18\x0b \x01(\x05\x12\x12\n\ndexRequire\x18\x0c \x01(\x05\x12\x12\n\nvitRequire\x18\r \x01(\x05\x12\x0c\n\x04type\x18\x0e \x01(\x05\x12\x12\n\ndurability\x18\x0f \x01(\x05\x12\x0c\n\x04\x62ind\x18\x10 \x01(\x05\x12\x11\n\taliveTime\x18\x11 \x01(\x05\x12\x10\n\x08\x62odyType\x18\x12 \x01(\x05\x12\x11\n\tpromotion\x18\x13 \x01(\x05\x12\r\n\x05price\x18\x14 \x01(\x05\x12\x11\n\tpriceType\x18\x15 \x01(\x05\x12\x10\n\x08restrict\x18\x16 \x01(\x05\x12\x10\n\x08maxstack\x18\x17 \x01(\x05')




_GETMALLITEMINFOREQUEST = descriptor.Descriptor(
  name='getMallItemInfoRequest',
  full_name='protoFile.shop.getMallItemInfo.getMallItemInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.shop.getMallItemInfo.getMallItemInfoRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='categories', full_name='protoFile.shop.getMallItemInfo.getMallItemInfoRequest.categories', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='page', full_name='protoFile.shop.getMallItemInfo.getMallItemInfoRequest.page', index=2,
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
  serialized_start=72,
  serialized_end=142,
)


_GETMALLITEMINFORESPONSE = descriptor.Descriptor(
  name='getMallItemInfoResponse',
  full_name='protoFile.shop.getMallItemInfo.getMallItemInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.shop.getMallItemInfo.getMallItemInfoResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.shop.getMallItemInfo.getMallItemInfoResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='protoFile.shop.getMallItemInfo.getMallItemInfoResponse.data', index=2,
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
  serialized_start=144,
  serialized_end=262,
)


_RESPONSEDATA = descriptor.Descriptor(
  name='ResponseData',
  full_name='protoFile.shop.getMallItemInfo.ResponseData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='categories', full_name='protoFile.shop.getMallItemInfo.ResponseData.categories', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='goal', full_name='protoFile.shop.getMallItemInfo.ResponseData.goal', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='items', full_name='protoFile.shop.getMallItemInfo.ResponseData.items', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=264,
  serialized_end=369,
)


_ITEMIIFO = descriptor.Descriptor(
  name='ItemIifo',
  full_name='protoFile.shop.getMallItemInfo.ItemIifo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.shop.getMallItemInfo.ItemIifo.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='name', full_name='protoFile.shop.getMallItemInfo.ItemIifo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='description', full_name='protoFile.shop.getMallItemInfo.ItemIifo.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='icon', full_name='protoFile.shop.getMallItemInfo.ItemIifo.icon', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='qualityLevel', full_name='protoFile.shop.getMallItemInfo.ItemIifo.qualityLevel', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='levelRequire', full_name='protoFile.shop.getMallItemInfo.ItemIifo.levelRequire', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='minDamage', full_name='protoFile.shop.getMallItemInfo.ItemIifo.minDamage', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='maxDamage', full_name='protoFile.shop.getMallItemInfo.ItemIifo.maxDamage', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='defense', full_name='protoFile.shop.getMallItemInfo.ItemIifo.defense', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='professionRequire', full_name='protoFile.shop.getMallItemInfo.ItemIifo.professionRequire', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='strRequire', full_name='protoFile.shop.getMallItemInfo.ItemIifo.strRequire', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dexRequire', full_name='protoFile.shop.getMallItemInfo.ItemIifo.dexRequire', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='vitRequire', full_name='protoFile.shop.getMallItemInfo.ItemIifo.vitRequire', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='protoFile.shop.getMallItemInfo.ItemIifo.type', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='durability', full_name='protoFile.shop.getMallItemInfo.ItemIifo.durability', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bind', full_name='protoFile.shop.getMallItemInfo.ItemIifo.bind', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='aliveTime', full_name='protoFile.shop.getMallItemInfo.ItemIifo.aliveTime', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bodyType', full_name='protoFile.shop.getMallItemInfo.ItemIifo.bodyType', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='promotion', full_name='protoFile.shop.getMallItemInfo.ItemIifo.promotion', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='price', full_name='protoFile.shop.getMallItemInfo.ItemIifo.price', index=19,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='priceType', full_name='protoFile.shop.getMallItemInfo.ItemIifo.priceType', index=20,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='restrict', full_name='protoFile.shop.getMallItemInfo.ItemIifo.restrict', index=21,
      number=22, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='maxstack', full_name='protoFile.shop.getMallItemInfo.ItemIifo.maxstack', index=22,
      number=23, type=5, cpp_type=1, label=1,
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
  serialized_start=372,
  serialized_end=803,
)

_GETMALLITEMINFORESPONSE.fields_by_name['data'].message_type = _RESPONSEDATA
_RESPONSEDATA.fields_by_name['items'].message_type = _ITEMIIFO
DESCRIPTOR.message_types_by_name['getMallItemInfoRequest'] = _GETMALLITEMINFOREQUEST
DESCRIPTOR.message_types_by_name['getMallItemInfoResponse'] = _GETMALLITEMINFORESPONSE
DESCRIPTOR.message_types_by_name['ResponseData'] = _RESPONSEDATA
DESCRIPTOR.message_types_by_name['ItemIifo'] = _ITEMIIFO

class getMallItemInfoRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETMALLITEMINFOREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.shop.getMallItemInfo.getMallItemInfoRequest)

class getMallItemInfoResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETMALLITEMINFORESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.shop.getMallItemInfo.getMallItemInfoResponse)

class ResponseData(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESPONSEDATA
  
  # @@protoc_insertion_point(class_scope:protoFile.shop.getMallItemInfo.ResponseData)

class ItemIifo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ITEMIIFO
  
  # @@protoc_insertion_point(class_scope:protoFile.shop.getMallItemInfo.ItemIifo)

# @@protoc_insertion_point(module_scope)
