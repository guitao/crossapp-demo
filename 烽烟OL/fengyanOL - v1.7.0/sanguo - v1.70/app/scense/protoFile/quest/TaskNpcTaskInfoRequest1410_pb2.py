# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import app.scense.protoFile.quest.TaskItemInfo_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/quest/TaskNpcTaskInfoRequest1410.proto',
  package='protoFile.quest.TaskNpcTaskInfoRequest1410',
  serialized_pb='\n0protoFile/quest/TaskNpcTaskInfoRequest1410.proto\x12*protoFile.quest.TaskNpcTaskInfoRequest1410\x1a\"protoFile/quest/TaskItemInfo.proto\"4\n\x16TaskNpcTaskInfoRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0e\n\x06npc_id\x18\x02 \x02(\x05\"\xa4\x01\n\x17TaskNpcTaskInfoResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0e\n\x06npc_id\x18\x02 \x02(\x05\x12\x0f\n\x07npc_img\x18\x03 \x02(\x05\x12\x10\n\x08npc_name\x18\x04 \x02(\t\x12\x10\n\x08npc_word\x18\x05 \x02(\t\x12\x34\n\rncp_task_item\x18\x06 \x03(\x0b\x32\x1d.protoFile.quest.TaskItemInfo')




_TASKNPCTASKINFOREQUEST = descriptor.Descriptor(
  name='TaskNpcTaskInfoRequest',
  full_name='protoFile.quest.TaskNpcTaskInfoRequest1410.TaskNpcTaskInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.quest.TaskNpcTaskInfoRequest1410.TaskNpcTaskInfoRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='npc_id', full_name='protoFile.quest.TaskNpcTaskInfoRequest1410.TaskNpcTaskInfoRequest.npc_id', index=1,
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
  serialized_start=132,
  serialized_end=184,
)


_TASKNPCTASKINFORESPONSE = descriptor.Descriptor(
  name='TaskNpcTaskInfoResponse',
  full_name='protoFile.quest.TaskNpcTaskInfoRequest1410.TaskNpcTaskInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.quest.TaskNpcTaskInfoRequest1410.TaskNpcTaskInfoResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='npc_id', full_name='protoFile.quest.TaskNpcTaskInfoRequest1410.TaskNpcTaskInfoResponse.npc_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='npc_img', full_name='protoFile.quest.TaskNpcTaskInfoRequest1410.TaskNpcTaskInfoResponse.npc_img', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='npc_name', full_name='protoFile.quest.TaskNpcTaskInfoRequest1410.TaskNpcTaskInfoResponse.npc_name', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='npc_word', full_name='protoFile.quest.TaskNpcTaskInfoRequest1410.TaskNpcTaskInfoResponse.npc_word', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ncp_task_item', full_name='protoFile.quest.TaskNpcTaskInfoRequest1410.TaskNpcTaskInfoResponse.ncp_task_item', index=5,
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
  serialized_start=187,
  serialized_end=351,
)

_TASKNPCTASKINFORESPONSE.fields_by_name['ncp_task_item'].message_type = app.scense.protoFile.quest.TaskItemInfo_pb2._TASKITEMINFO
DESCRIPTOR.message_types_by_name['TaskNpcTaskInfoRequest'] = _TASKNPCTASKINFOREQUEST
DESCRIPTOR.message_types_by_name['TaskNpcTaskInfoResponse'] = _TASKNPCTASKINFORESPONSE

class TaskNpcTaskInfoRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TASKNPCTASKINFOREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.quest.TaskNpcTaskInfoRequest1410.TaskNpcTaskInfoRequest)

class TaskNpcTaskInfoResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TASKNPCTASKINFORESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.quest.TaskNpcTaskInfoRequest1410.TaskNpcTaskInfoResponse)

# @@protoc_insertion_point(module_scope)
