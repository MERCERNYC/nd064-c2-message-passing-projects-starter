# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: coordinates.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='coordinates.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x63oordinates.proto\"I\n\x12\x43oordinatesMessage\x12\x0e\n\x06userId\x18\x01 \x01(\x05\x12\x10\n\x08latitude\x18\x02 \x01(\x05\x12\x11\n\tlongitude\x18\x03 \x01(\x05\x32\x41\n\x0bItemService\x12\x32\n\x06\x43reate\x12\x13.CoordinatesMessage\x1a\x13.CoordinatesMessageb\x06proto3'
)




_COORDINATESMESSAGE = _descriptor.Descriptor(
  name='CoordinatesMessage',
  full_name='CoordinatesMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userId', full_name='CoordinatesMessage.userId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='CoordinatesMessage.latitude', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='CoordinatesMessage.longitude', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=21,
  serialized_end=94,
)

DESCRIPTOR.message_types_by_name['CoordinatesMessage'] = _COORDINATESMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CoordinatesMessage = _reflection.GeneratedProtocolMessageType('CoordinatesMessage', (_message.Message,), {
  'DESCRIPTOR' : _COORDINATESMESSAGE,
  '__module__' : 'coordinates_pb2'
  # @@protoc_insertion_point(class_scope:CoordinatesMessage)
  })
_sym_db.RegisterMessage(CoordinatesMessage)



_ITEMSERVICE = _descriptor.ServiceDescriptor(
  name='ItemService',
  full_name='ItemService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=96,
  serialized_end=161,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='ItemService.Create',
    index=0,
    containing_service=None,
    input_type=_COORDINATESMESSAGE,
    output_type=_COORDINATESMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ITEMSERVICE)

DESCRIPTOR.services_by_name['ItemService'] = _ITEMSERVICE

# @@protoc_insertion_point(module_scope)
