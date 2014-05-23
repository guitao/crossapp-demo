# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/mail/mailList.proto',
  package='protoFile.mail.mailList',
  serialized_pb='\n\x1dprotoFile/mail/mailList.proto\x12\x17protoFile.mail.mailList\"\x1d\n\x0fmailListRequest\x12\n\n\x02id\x18\x01 \x02(\x05\"f\n\x10mailListResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x31\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32#.protoFile.mail.mailList.dataPacket\">\n\ndataPacket\x12\x30\n\x05mails\x18\x01 \x03(\x0b\x32!.protoFile.mail.mailList.MailInfo\"\xa0\x01\n\x08MailInfo\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\nsystemType\x18\x03 \x01(\x05\x12\x10\n\x08sendTime\x18\x04 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x05 \x01(\t\x12\x0c\n\x04type\x18\x06 \x01(\x05\x12\x11\n\treference\x18\x07 \x01(\t\x12\x10\n\x08isFriend\x18\x08 \x01(\x05\x12\x10\n\x08playerId\x18\t \x01(\x05')




_MAILLISTREQUEST = descriptor.Descriptor(
  name='mailListRequest',
  full_name='protoFile.mail.mailList.mailListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.mail.mailList.mailListRequest.id', index=0,
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
  serialized_start=58,
  serialized_end=87,
)


_MAILLISTRESPONSE = descriptor.Descriptor(
  name='mailListResponse',
  full_name='protoFile.mail.mailList.mailListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.mail.mailList.mailListResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.mail.mailList.mailListResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='protoFile.mail.mailList.mailListResponse.data', index=2,
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
  serialized_start=89,
  serialized_end=191,
)


_DATAPACKET = descriptor.Descriptor(
  name='dataPacket',
  full_name='protoFile.mail.mailList.dataPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='mails', full_name='protoFile.mail.mailList.dataPacket.mails', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=193,
  serialized_end=255,
)


_MAILINFO = descriptor.Descriptor(
  name='MailInfo',
  full_name='protoFile.mail.mailList.MailInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.mail.mailList.MailInfo.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='name', full_name='protoFile.mail.mailList.MailInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='systemType', full_name='protoFile.mail.mailList.MailInfo.systemType', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sendTime', full_name='protoFile.mail.mailList.MailInfo.sendTime', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='content', full_name='protoFile.mail.mailList.MailInfo.content', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='protoFile.mail.mailList.MailInfo.type', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='reference', full_name='protoFile.mail.mailList.MailInfo.reference', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='isFriend', full_name='protoFile.mail.mailList.MailInfo.isFriend', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='playerId', full_name='protoFile.mail.mailList.MailInfo.playerId', index=8,
      number=9, type=5, cpp_type=1, label=1,
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
  serialized_end=418,
)

_MAILLISTRESPONSE.fields_by_name['data'].message_type = _DATAPACKET
_DATAPACKET.fields_by_name['mails'].message_type = _MAILINFO
DESCRIPTOR.message_types_by_name['mailListRequest'] = _MAILLISTREQUEST
DESCRIPTOR.message_types_by_name['mailListResponse'] = _MAILLISTRESPONSE
DESCRIPTOR.message_types_by_name['dataPacket'] = _DATAPACKET
DESCRIPTOR.message_types_by_name['MailInfo'] = _MAILINFO

class mailListRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MAILLISTREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.mail.mailList.mailListRequest)

class mailListResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MAILLISTRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.mail.mailList.mailListResponse)

class dataPacket(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DATAPACKET
  
  # @@protoc_insertion_point(class_scope:protoFile.mail.mailList.dataPacket)

class MailInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MAILINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.mail.mailList.MailInfo)

# @@protoc_insertion_point(module_scope)
