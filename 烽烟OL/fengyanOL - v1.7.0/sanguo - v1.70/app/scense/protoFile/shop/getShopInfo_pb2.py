# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import app.scense.protoFile.itemInfo_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/shop/getShopInfo.proto',
  package='protoFile.shop.getShopInfo',
  serialized_pb='\n protoFile/shop/getShopInfo.proto\x12\x1aprotoFile.shop.getShopInfo\x1a\x18protoFile/itemInfo.proto\"6\n\x12getShopInfoRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x14\n\x0cshopCategory\x18\x02 \x02(\x05\"j\n\x13getShopInfoResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x32\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32$.protoFile.shop.getShopInfo.ShopInfo\"{\n\x08ShopInfo\x12@\n\x0fpackageItemInfo\x18\x01 \x03(\x0b\x32\'.protoFile.shop.getShopInfo.PackageInfo\x12\x14\n\x0cshopCategory\x18\x02 \x01(\x05\x12\x17\n\x0frefreshShopTime\x18\x03 \x01(\x05\"G\n\x0bPackageInfo\x12&\n\x08itemInfo\x18\x01 \x01(\x0b\x32\x14.protoFile.ItemsInfo\x12\x10\n\x08position\x18\x02 \x01(\x05')




_GETSHOPINFOREQUEST = descriptor.Descriptor(
  name='getShopInfoRequest',
  full_name='protoFile.shop.getShopInfo.getShopInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.shop.getShopInfo.getShopInfoRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='shopCategory', full_name='protoFile.shop.getShopInfo.getShopInfoRequest.shopCategory', index=1,
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
  serialized_start=90,
  serialized_end=144,
)


_GETSHOPINFORESPONSE = descriptor.Descriptor(
  name='getShopInfoResponse',
  full_name='protoFile.shop.getShopInfo.getShopInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.shop.getShopInfo.getShopInfoResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.shop.getShopInfo.getShopInfoResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='protoFile.shop.getShopInfo.getShopInfoResponse.data', index=2,
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
  serialized_start=146,
  serialized_end=252,
)


_SHOPINFO = descriptor.Descriptor(
  name='ShopInfo',
  full_name='protoFile.shop.getShopInfo.ShopInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='packageItemInfo', full_name='protoFile.shop.getShopInfo.ShopInfo.packageItemInfo', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='shopCategory', full_name='protoFile.shop.getShopInfo.ShopInfo.shopCategory', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='refreshShopTime', full_name='protoFile.shop.getShopInfo.ShopInfo.refreshShopTime', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=254,
  serialized_end=377,
)


_PACKAGEINFO = descriptor.Descriptor(
  name='PackageInfo',
  full_name='protoFile.shop.getShopInfo.PackageInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='itemInfo', full_name='protoFile.shop.getShopInfo.PackageInfo.itemInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='position', full_name='protoFile.shop.getShopInfo.PackageInfo.position', index=1,
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
  serialized_start=379,
  serialized_end=450,
)

_GETSHOPINFORESPONSE.fields_by_name['data'].message_type = _SHOPINFO
_SHOPINFO.fields_by_name['packageItemInfo'].message_type = _PACKAGEINFO
_PACKAGEINFO.fields_by_name['itemInfo'].message_type = app.scense.protoFile.itemInfo_pb2._ITEMSINFO
DESCRIPTOR.message_types_by_name['getShopInfoRequest'] = _GETSHOPINFOREQUEST
DESCRIPTOR.message_types_by_name['getShopInfoResponse'] = _GETSHOPINFORESPONSE
DESCRIPTOR.message_types_by_name['ShopInfo'] = _SHOPINFO
DESCRIPTOR.message_types_by_name['PackageInfo'] = _PACKAGEINFO

class getShopInfoRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETSHOPINFOREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.shop.getShopInfo.getShopInfoRequest)

class getShopInfoResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETSHOPINFORESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.shop.getShopInfo.getShopInfoResponse)

class ShopInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SHOPINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.shop.getShopInfo.ShopInfo)

class PackageInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PACKAGEINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.shop.getShopInfo.PackageInfo)

# @@protoc_insertion_point(module_scope)
