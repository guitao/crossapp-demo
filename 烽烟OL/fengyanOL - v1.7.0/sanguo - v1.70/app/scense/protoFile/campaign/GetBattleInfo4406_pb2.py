# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/campaign/GetBattleInfo4406.proto',
  package='protoFile.campaign.GetBattleInfo4406',
  serialized_pb='\n*protoFile/campaign/GetBattleInfo4406.proto\x12$protoFile.campaign.GetBattleInfo4406\"\"\n\x14GetBattleInfoRequest\x12\n\n\x02id\x18\x01 \x02(\x05\"\x88\x01\n\x15GetBattleInfoResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\x08\x12N\n\x0fgroupBattleInfo\x18\x03 \x01(\x0b\x32\x35.protoFile.campaign.GetBattleInfo4406.GroupBattleInfo\"\xda\x02\n\x0fGroupBattleInfo\x12\x12\n\nroundCount\x18\x01 \x01(\x05\x12\x12\n\nremainTime\x18\x02 \x01(\x05\x12\x12\n\njishaCount\x18\x03 \x01(\x05\x12\x12\n\nobtainCoin\x18\x04 \x01(\x05\x12\x11\n\tfailCount\x18\x05 \x01(\x05\x12\x10\n\x08obtainSw\x18\x06 \x01(\x05\x12H\n\x0e\x62\x61ttleInfoList\x18\x07 \x03(\x0b\x32\x30.protoFile.campaign.GetBattleInfo4406.BattleInfo\x12\x43\n\ngroup1Info\x18\x08 \x01(\x0b\x32/.protoFile.campaign.GetBattleInfo4406.GroupInfo\x12\x43\n\ngroup2Info\x18\t \x01(\x0b\x32/.protoFile.campaign.GetBattleInfo4406.GroupInfo\"g\n\nBattleInfo\x12\x0f\n\x07roleId1\x18\x01 \x01(\x05\x12\x11\n\troleName1\x18\x02 \x01(\t\x12\x0f\n\x07roleId2\x18\x03 \x01(\x05\x12\x11\n\troleName2\x18\x04 \x01(\t\x12\x11\n\tsucObCoin\x18\x05 \x01(\x05\"\x88\x01\n\tGroupInfo\x12\x11\n\tgroupName\x18\x01 \x01(\t\x12\x12\n\ngroupCount\x18\x02 \x01(\x05\x12\x0c\n\x04icon\x18\x03 \x01(\x05\x12\x46\n\x0bgroupMember\x18\x04 \x03(\x0b\x32\x31.protoFile.campaign.GetBattleInfo4406.GroupMember\"3\n\x0bGroupMember\x12\x10\n\x08memberId\x18\x01 \x01(\x05\x12\x12\n\nmemberName\x18\x02 \x01(\t')




_GETBATTLEINFOREQUEST = descriptor.Descriptor(
  name='GetBattleInfoRequest',
  full_name='protoFile.campaign.GetBattleInfo4406.GetBattleInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.campaign.GetBattleInfo4406.GetBattleInfoRequest.id', index=0,
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
  serialized_start=84,
  serialized_end=118,
)


_GETBATTLEINFORESPONSE = descriptor.Descriptor(
  name='GetBattleInfoResponse',
  full_name='protoFile.campaign.GetBattleInfo4406.GetBattleInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.campaign.GetBattleInfo4406.GetBattleInfoResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.campaign.GetBattleInfo4406.GetBattleInfoResponse.result', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='groupBattleInfo', full_name='protoFile.campaign.GetBattleInfo4406.GetBattleInfoResponse.groupBattleInfo', index=2,
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
  serialized_start=121,
  serialized_end=257,
)


_GROUPBATTLEINFO = descriptor.Descriptor(
  name='GroupBattleInfo',
  full_name='protoFile.campaign.GetBattleInfo4406.GroupBattleInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='roundCount', full_name='protoFile.campaign.GetBattleInfo4406.GroupBattleInfo.roundCount', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='remainTime', full_name='protoFile.campaign.GetBattleInfo4406.GroupBattleInfo.remainTime', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='jishaCount', full_name='protoFile.campaign.GetBattleInfo4406.GroupBattleInfo.jishaCount', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='obtainCoin', full_name='protoFile.campaign.GetBattleInfo4406.GroupBattleInfo.obtainCoin', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='failCount', full_name='protoFile.campaign.GetBattleInfo4406.GroupBattleInfo.failCount', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='obtainSw', full_name='protoFile.campaign.GetBattleInfo4406.GroupBattleInfo.obtainSw', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='battleInfoList', full_name='protoFile.campaign.GetBattleInfo4406.GroupBattleInfo.battleInfoList', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='group1Info', full_name='protoFile.campaign.GetBattleInfo4406.GroupBattleInfo.group1Info', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='group2Info', full_name='protoFile.campaign.GetBattleInfo4406.GroupBattleInfo.group2Info', index=8,
      number=9, type=11, cpp_type=10, label=1,
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
  serialized_start=260,
  serialized_end=606,
)


_BATTLEINFO = descriptor.Descriptor(
  name='BattleInfo',
  full_name='protoFile.campaign.GetBattleInfo4406.BattleInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='roleId1', full_name='protoFile.campaign.GetBattleInfo4406.BattleInfo.roleId1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='roleName1', full_name='protoFile.campaign.GetBattleInfo4406.BattleInfo.roleName1', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='roleId2', full_name='protoFile.campaign.GetBattleInfo4406.BattleInfo.roleId2', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='roleName2', full_name='protoFile.campaign.GetBattleInfo4406.BattleInfo.roleName2', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sucObCoin', full_name='protoFile.campaign.GetBattleInfo4406.BattleInfo.sucObCoin', index=4,
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
  serialized_start=608,
  serialized_end=711,
)


_GROUPINFO = descriptor.Descriptor(
  name='GroupInfo',
  full_name='protoFile.campaign.GetBattleInfo4406.GroupInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='groupName', full_name='protoFile.campaign.GetBattleInfo4406.GroupInfo.groupName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='groupCount', full_name='protoFile.campaign.GetBattleInfo4406.GroupInfo.groupCount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='icon', full_name='protoFile.campaign.GetBattleInfo4406.GroupInfo.icon', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='groupMember', full_name='protoFile.campaign.GetBattleInfo4406.GroupInfo.groupMember', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=714,
  serialized_end=850,
)


_GROUPMEMBER = descriptor.Descriptor(
  name='GroupMember',
  full_name='protoFile.campaign.GetBattleInfo4406.GroupMember',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='memberId', full_name='protoFile.campaign.GetBattleInfo4406.GroupMember.memberId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='memberName', full_name='protoFile.campaign.GetBattleInfo4406.GroupMember.memberName', index=1,
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
  serialized_start=852,
  serialized_end=903,
)

_GETBATTLEINFORESPONSE.fields_by_name['groupBattleInfo'].message_type = _GROUPBATTLEINFO
_GROUPBATTLEINFO.fields_by_name['battleInfoList'].message_type = _BATTLEINFO
_GROUPBATTLEINFO.fields_by_name['group1Info'].message_type = _GROUPINFO
_GROUPBATTLEINFO.fields_by_name['group2Info'].message_type = _GROUPINFO
_GROUPINFO.fields_by_name['groupMember'].message_type = _GROUPMEMBER
DESCRIPTOR.message_types_by_name['GetBattleInfoRequest'] = _GETBATTLEINFOREQUEST
DESCRIPTOR.message_types_by_name['GetBattleInfoResponse'] = _GETBATTLEINFORESPONSE
DESCRIPTOR.message_types_by_name['GroupBattleInfo'] = _GROUPBATTLEINFO
DESCRIPTOR.message_types_by_name['BattleInfo'] = _BATTLEINFO
DESCRIPTOR.message_types_by_name['GroupInfo'] = _GROUPINFO
DESCRIPTOR.message_types_by_name['GroupMember'] = _GROUPMEMBER

class GetBattleInfoRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETBATTLEINFOREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.campaign.GetBattleInfo4406.GetBattleInfoRequest)

class GetBattleInfoResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETBATTLEINFORESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.campaign.GetBattleInfo4406.GetBattleInfoResponse)

class GroupBattleInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GROUPBATTLEINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.campaign.GetBattleInfo4406.GroupBattleInfo)

class BattleInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BATTLEINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.campaign.GetBattleInfo4406.BattleInfo)

class GroupInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GROUPINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.campaign.GetBattleInfo4406.GroupInfo)

class GroupMember(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GROUPMEMBER
  
  # @@protoc_insertion_point(class_scope:protoFile.campaign.GetBattleInfo4406.GroupMember)

# @@protoc_insertion_point(module_scope)
