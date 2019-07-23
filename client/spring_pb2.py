# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spring.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='spring.proto',
  package='spring',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cspring.proto\x12\x06spring\"\x16\n\x05Regex\x12\r\n\x05regex\x18\x01 \x01(\t\"\x1a\n\x07Matches\x12\x0f\n\x07matches\x18\x01 \x03(\x0c\x32=\n\nSubscriber\x12/\n\tSubscribe\x12\r.spring.Regex\x1a\x0f.spring.Matches\"\x00\x30\x01\x62\x06proto3')
)




_REGEX = _descriptor.Descriptor(
  name='Regex',
  full_name='spring.Regex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='regex', full_name='spring.Regex.regex', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=46,
)


_MATCHES = _descriptor.Descriptor(
  name='Matches',
  full_name='spring.Matches',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='matches', full_name='spring.Matches.matches', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=74,
)

DESCRIPTOR.message_types_by_name['Regex'] = _REGEX
DESCRIPTOR.message_types_by_name['Matches'] = _MATCHES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Regex = _reflection.GeneratedProtocolMessageType('Regex', (_message.Message,), {
  'DESCRIPTOR' : _REGEX,
  '__module__' : 'spring_pb2'
  # @@protoc_insertion_point(class_scope:spring.Regex)
  })
_sym_db.RegisterMessage(Regex)

Matches = _reflection.GeneratedProtocolMessageType('Matches', (_message.Message,), {
  'DESCRIPTOR' : _MATCHES,
  '__module__' : 'spring_pb2'
  # @@protoc_insertion_point(class_scope:spring.Matches)
  })
_sym_db.RegisterMessage(Matches)



_SUBSCRIBER = _descriptor.ServiceDescriptor(
  name='Subscriber',
  full_name='spring.Subscriber',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=76,
  serialized_end=137,
  methods=[
  _descriptor.MethodDescriptor(
    name='Subscribe',
    full_name='spring.Subscriber.Subscribe',
    index=0,
    containing_service=None,
    input_type=_REGEX,
    output_type=_MATCHES,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SUBSCRIBER)

DESCRIPTOR.services_by_name['Subscriber'] = _SUBSCRIBER

# @@protoc_insertion_point(module_scope)
