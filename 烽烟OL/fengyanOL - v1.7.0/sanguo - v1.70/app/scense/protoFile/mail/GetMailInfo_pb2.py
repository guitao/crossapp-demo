# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/mail/GetMailInfo.proto',
  package='protoFile.mail.GetMailInfo',
  serialized_pb='\n protoFile/mail/GetMailInfo.proto\x12\x1aprotoFile.mail.GetMailInfo\"0\n\x12getMailInfoRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0e\n\x06mailId\x18\x02 \x02(\x05\"l\n\x13getMailInfoResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x34\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32&.protoFile.mail.GetMailInfo.DataPacket\"D\n\nDataPacket\x12\x36\n\x08mailinfo\x18\x01 \x01(\x0b\x32$.protoFile.mail.GetMailInfo.MailInfo\"\x80\x01\n\x08MailInfo\x12\x16\n\x0emailIdResponse\x18\x01 \x01(\x05\x12\x10\n\x08mailFrom\x18\x02 \x01(\t\x12\x11\n\tmailTitle\x18\x03 \x01(\t\x12\x13\n\x0bmailContent\x18\x04 \x01(\t\x12\x10\n\x08mailType\x18\x05 \x01(\x05\x12\x10\n\x08mailDate\x18\x06 \x01(\t')




_GETMAILINFOREQUEST = descriptor.Descriptor(
  name='getMailInfoRequest',
  full_name='protoFile.mail.GetMailInfo.getMailInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.mail.GetMailInfo.getMailInfoRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='mailId', full_name='protoFile.mail.GetMailInfo.getMailInfoRequest.mailId', index=1,
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
  serialized_start=64,
  serialized_end=112,
)


_GETMAILINFORESPONSE = descriptor.Descriptor(
  name='getMailInfoResponse',
  full_name='protoFile.mail.GetMailInfo.getMailInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.mail.GetMailInfo.getMailInfoResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.mail.GetMailInfo.getMailInfoResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='protoFile.mail.GetMailInfo.getMailInfoResponse.data', index=2,
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
  serialized_start=114,
  serialized_end=222,
)


_DATAPACKET = descriptor.Descriptor(
  name='DataPacket',
  full_name='protoFile.mail.GetMailInfo.DataPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='mailinfo', full_name='protoFile.mail.GetMailInfo.DataPacket.mailinfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=224,
  serialized_end=292,
)


_MAILINFO = descriptor.Descriptor(
  name='MailInfo',
  full_name='protoFile.mail.GetMailInfo.MailInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='mailIdResponse', full_name='protoFile.mail.GetMailInfo.MailInfo.mailIdResponse', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='mailFrom', full_name='protoFile.mail.GetMailInfo.MailInfo.mailFrom', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='mailTitle', full_name='protoFile.mail.GetMailInfo.MailInfo.mailTitle', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='mailContent', full_name='protoFile.mail.GetMailInfo.MailInfo.mailContent', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='mailType', full_name='protoFile.mail.GetMailInfo.MailInfo.mailType', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='mailDate', full_name='protoFile.mail.GetMailInfo.MailInfo.mailDate', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=295,
  serialized_end=423,
)

_GETMAILINFORESPONSE.fields_by_name['data'].message_type = _DATAPACKET
_DATAPACKET.fields_by_name['mailinfo'].message_type = _MAILINFO
DESCRIPTOR.message_types_by_name['getMailInfoRequest'] = _GETMAILINFOREQUEST
DESCRIPTOR.message_types_by_name['getMailInfoResponse'] = _GETMAILINFORESPONSE
DESCRIPTOR.message_types_by_name['DataPacket'] = _DATAPACKET
DESCRIPTOR.message_types_by_name['MailInfo'] = _MAILINFO

class getMailInfoRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETMAILINFOREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.mail.GetMailInfo.getMailInfoRequest)

class getMailInfoResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETMAILINFORESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.mail.GetMailInfo.getMailInfoResponse)

class DataPacket(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DATAPACKET
  
  # @@protoc_insertion_point(class_scope:protoFile.mail.GetMailInfo.DataPacket)

class MailInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MAILINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.mail.GetMailInfo.MailInfo)

# @@protoc_insertion_point(module_scope)
