# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='GetJingJiInfo3700.proto',
  package='proto.jingji.jingji3700',
  serialized_pb='\n\x17GetJingJiInfo3700.proto\x12\x17proto.jingji.jingji3700\"\x1e\n\x10GetJingJiRequest\x12\n\n\x02id\x18\x01 \x02(\x05\"m\n\x11GetJingJiResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\x08\x12\x37\n\njingjiInfo\x18\x03 \x01(\x0b\x32#.proto.jingji.jingji3700.JingJiInfo\"\x98\x02\n\nJingJiInfo\x12\x10\n\x08rankInfo\x18\x01 \x01(\t\x12\r\n\x05jifen\x18\x02 \x01(\x05\x12\x0f\n\x07weiwang\x18\x03 \x01(\x05\x12\x0c\n\x04rank\x18\x04 \x01(\x05\x12\x11\n\tliansheng\x18\x05 \x01(\x05\x12\x0f\n\x07tzCount\x18\x06 \x01(\x05\x12\x32\n\x06\x64rList\x18\x07 \x03(\x0b\x32\".proto.jingji.jingji3700.DiRenInfo\x12;\n\x0e\x62\x61ttleInfoList\x18\x08 \x03(\x0b\x32#.proto.jingji.jingji3700.BattleInfo\x12\x10\n\x08\x61\x64\x64\x43ount\x18\t \x01(\x05\x12\x0f\n\x07reqCoin\x18\n \x01(\x05\x12\x12\n\nobtainTime\x18\x0b \x01(\x05\"Z\n\tDiRenInfo\x12\x0b\n\x03\x62Id\x18\x01 \x01(\x05\x12\r\n\x05\x62Name\x18\x02 \x01(\t\x12\x0e\n\x06\x62Level\x18\x03 \x01(\x05\x12\r\n\x05\x62Rank\x18\x04 \x01(\x05\x12\x12\n\nprofession\x18\x05 \x01(\x05\"\x1f\n\nBattleInfo\x12\x11\n\tbattleStr\x18\x01 \x01(\t')




_GETJINGJIREQUEST = descriptor.Descriptor(
  name='GetJingJiRequest',
  full_name='proto.jingji.jingji3700.GetJingJiRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='proto.jingji.jingji3700.GetJingJiRequest.id', index=0,
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
  serialized_start=52,
  serialized_end=82,
)


_GETJINGJIRESPONSE = descriptor.Descriptor(
  name='GetJingJiResponse',
  full_name='proto.jingji.jingji3700.GetJingJiResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='message', full_name='proto.jingji.jingji3700.GetJingJiResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='result', full_name='proto.jingji.jingji3700.GetJingJiResponse.result', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='jingjiInfo', full_name='proto.jingji.jingji3700.GetJingJiResponse.jingjiInfo', index=2,
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
  serialized_start=84,
  serialized_end=193,
)


_JINGJIINFO = descriptor.Descriptor(
  name='JingJiInfo',
  full_name='proto.jingji.jingji3700.JingJiInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='rankInfo', full_name='proto.jingji.jingji3700.JingJiInfo.rankInfo', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='jifen', full_name='proto.jingji.jingji3700.JingJiInfo.jifen', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='weiwang', full_name='proto.jingji.jingji3700.JingJiInfo.weiwang', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='rank', full_name='proto.jingji.jingji3700.JingJiInfo.rank', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='liansheng', full_name='proto.jingji.jingji3700.JingJiInfo.liansheng', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='tzCount', full_name='proto.jingji.jingji3700.JingJiInfo.tzCount', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='drList', full_name='proto.jingji.jingji3700.JingJiInfo.drList', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='battleInfoList', full_name='proto.jingji.jingji3700.JingJiInfo.battleInfoList', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='addCount', full_name='proto.jingji.jingji3700.JingJiInfo.addCount', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='reqCoin', full_name='proto.jingji.jingji3700.JingJiInfo.reqCoin', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='obtainTime', full_name='proto.jingji.jingji3700.JingJiInfo.obtainTime', index=10,
      number=11, type=5, cpp_type=1, label=1,
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
  serialized_start=196,
  serialized_end=476,
)


_DIRENINFO = descriptor.Descriptor(
  name='DiRenInfo',
  full_name='proto.jingji.jingji3700.DiRenInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='bId', full_name='proto.jingji.jingji3700.DiRenInfo.bId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bName', full_name='proto.jingji.jingji3700.DiRenInfo.bName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bLevel', full_name='proto.jingji.jingji3700.DiRenInfo.bLevel', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bRank', full_name='proto.jingji.jingji3700.DiRenInfo.bRank', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='profession', full_name='proto.jingji.jingji3700.DiRenInfo.profession', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=478,
  serialized_end=568,
)


_BATTLEINFO = descriptor.Descriptor(
  name='BattleInfo',
  full_name='proto.jingji.jingji3700.BattleInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='battleStr', full_name='proto.jingji.jingji3700.BattleInfo.battleStr', index=0,
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
  serialized_start=570,
  serialized_end=601,
)

_GETJINGJIRESPONSE.fields_by_name['jingjiInfo'].message_type = _JINGJIINFO
_JINGJIINFO.fields_by_name['drList'].message_type = _DIRENINFO
_JINGJIINFO.fields_by_name['battleInfoList'].message_type = _BATTLEINFO
DESCRIPTOR.message_types_by_name['GetJingJiRequest'] = _GETJINGJIREQUEST
DESCRIPTOR.message_types_by_name['GetJingJiResponse'] = _GETJINGJIRESPONSE
DESCRIPTOR.message_types_by_name['JingJiInfo'] = _JINGJIINFO
DESCRIPTOR.message_types_by_name['DiRenInfo'] = _DIRENINFO
DESCRIPTOR.message_types_by_name['BattleInfo'] = _BATTLEINFO

class GetJingJiRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETJINGJIREQUEST
  
  # @@protoc_insertion_point(class_scope:proto.jingji.jingji3700.GetJingJiRequest)

class GetJingJiResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETJINGJIRESPONSE
  
  # @@protoc_insertion_point(class_scope:proto.jingji.jingji3700.GetJingJiResponse)

class JingJiInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _JINGJIINFO
  
  # @@protoc_insertion_point(class_scope:proto.jingji.jingji3700.JingJiInfo)

class DiRenInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DIRENINFO
  
  # @@protoc_insertion_point(class_scope:proto.jingji.jingji3700.DiRenInfo)

class BattleInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BATTLEINFO
  
  # @@protoc_insertion_point(class_scope:proto.jingji.jingji3700.BattleInfo)

# @@protoc_insertion_point(module_scope)
