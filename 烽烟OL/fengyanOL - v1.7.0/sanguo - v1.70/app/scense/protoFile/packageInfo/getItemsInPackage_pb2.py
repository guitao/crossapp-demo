# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import app.scense.protoFile.itemInfo_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/packageInfo/getItemsInPackage.proto',
  package='protoFile.packageInfo.getItemsInPackage',
  serialized_pb='\n-protoFile/packageInfo/getItemsInPackage.proto\x12\'protoFile.packageInfo.getItemsInPackage\x1a\x18protoFile/itemInfo.proto\"M\n\x18getItemsInPackageRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x14\n\x0cpackCategory\x18\x02 \x02(\x05\x12\x0f\n\x07\x63urpage\x18\x03 \x02(\x05\"\x81\x01\n\x19getItemsInPackageResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x43\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x35.protoFile.packageInfo.getItemsInPackage.ResponseData\"\xbd\x01\n\x0cResponseData\x12\x14\n\x0cpackCategory\x18\x01 \x01(\x05\x12\x13\n\x0bpackageSize\x18\x02 \x01(\x05\x12\x0f\n\x07\x63urpage\x18\x03 \x01(\x05\x12\x0f\n\x07maxpage\x18\x04 \x01(\x05\x12\x11\n\ttotalsize\x18\x05 \x01(\x05\x12M\n\x0fpackageItemInfo\x18\x06 \x03(\x0b\x32\x34.protoFile.packageInfo.getItemsInPackage.PackageInfo\"G\n\x0bPackageInfo\x12&\n\x08itemInfo\x18\x01 \x01(\x0b\x32\x14.protoFile.ItemsInfo\x12\x10\n\x08position\x18\x02 \x01(\x05')




_GETITEMSINPACKAGEREQUEST = descriptor.Descriptor(
  name='getItemsInPackageRequest',
  full_name='protoFile.packageInfo.getItemsInPackage.getItemsInPackageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.packageInfo.getItemsInPackage.getItemsInPackageRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='packCategory', full_name='protoFile.packageInfo.getItemsInPackage.getItemsInPackageRequest.packCategory', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='curpage', full_name='protoFile.packageInfo.getItemsInPackage.getItemsInPackageRequest.curpage', index=2,
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
  serialized_start=116,
  serialized_end=193,
)


_GETITEMSINPACKAGERESPONSE = descriptor.Descriptor(
  name='getItemsInPackageResponse',
  full_name='protoFile.packageInfo.getItemsInPackage.getItemsInPackageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.packageInfo.getItemsInPackage.getItemsInPackageResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.packageInfo.getItemsInPackage.getItemsInPackageResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='protoFile.packageInfo.getItemsInPackage.getItemsInPackageResponse.data', index=2,
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
  serialized_start=196,
  serialized_end=325,
)


_RESPONSEDATA = descriptor.Descriptor(
  name='ResponseData',
  full_name='protoFile.packageInfo.getItemsInPackage.ResponseData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='packCategory', full_name='protoFile.packageInfo.getItemsInPackage.ResponseData.packCategory', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='packageSize', full_name='protoFile.packageInfo.getItemsInPackage.ResponseData.packageSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='curpage', full_name='protoFile.packageInfo.getItemsInPackage.ResponseData.curpage', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='maxpage', full_name='protoFile.packageInfo.getItemsInPackage.ResponseData.maxpage', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='totalsize', full_name='protoFile.packageInfo.getItemsInPackage.ResponseData.totalsize', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='packageItemInfo', full_name='protoFile.packageInfo.getItemsInPackage.ResponseData.packageItemInfo', index=5,
      number=6, type=11, cpp_type=10, label=3,
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
  serialized_start=328,
  serialized_end=517,
)


_PACKAGEINFO = descriptor.Descriptor(
  name='PackageInfo',
  full_name='protoFile.packageInfo.getItemsInPackage.PackageInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='itemInfo', full_name='protoFile.packageInfo.getItemsInPackage.PackageInfo.itemInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='position', full_name='protoFile.packageInfo.getItemsInPackage.PackageInfo.position', index=1,
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
  serialized_start=519,
  serialized_end=590,
)

_GETITEMSINPACKAGERESPONSE.fields_by_name['data'].message_type = _RESPONSEDATA
_RESPONSEDATA.fields_by_name['packageItemInfo'].message_type = _PACKAGEINFO
_PACKAGEINFO.fields_by_name['itemInfo'].message_type = app.scense.protoFile.itemInfo_pb2._ITEMSINFO
DESCRIPTOR.message_types_by_name['getItemsInPackageRequest'] = _GETITEMSINPACKAGEREQUEST
DESCRIPTOR.message_types_by_name['getItemsInPackageResponse'] = _GETITEMSINPACKAGERESPONSE
DESCRIPTOR.message_types_by_name['ResponseData'] = _RESPONSEDATA
DESCRIPTOR.message_types_by_name['PackageInfo'] = _PACKAGEINFO

class getItemsInPackageRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETITEMSINPACKAGEREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.packageInfo.getItemsInPackage.getItemsInPackageRequest)

class getItemsInPackageResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETITEMSINPACKAGERESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.packageInfo.getItemsInPackage.getItemsInPackageResponse)

class ResponseData(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESPONSEDATA
  
  # @@protoc_insertion_point(class_scope:protoFile.packageInfo.getItemsInPackage.ResponseData)

class PackageInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PACKAGEINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.packageInfo.getItemsInPackage.PackageInfo)

# @@protoc_insertion_point(module_scope)
