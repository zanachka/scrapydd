# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='service.proto',
  package='unary',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rservice.proto\x12\x05unary\"\x12\n\x10HeartbeatRequest\"\x13\n\x11HeartbeatResponse\"\x0f\n\rGetJobRequest\"\x10\n\x0eGetJobResponse\"\x12\n\x10GetJobEggRequest\"\x13\n\x11GetJobEggResponse\"\x14\n\x12\x43ompleteJobRequest\"\x15\n\x13\x43ompleteJobResponse2\x86\x02\n\x0bNodeService\x12>\n\tHeartbeat\x12\x17.unary.HeartbeatRequest\x1a\x18.unary.HeartbeatResponse\x12\x35\n\x06GetJob\x12\x14.unary.GetJobRequest\x1a\x15.unary.GetJobResponse\x12:\n\x06GetEgg\x12\x17.unary.GetJobEggRequest\x1a\x17.unary.GetJobEggRequest\x12\x44\n\x0b\x43ompleteJob\x12\x19.unary.CompleteJobRequest\x1a\x1a.unary.CompleteJobResponseb\x06proto3'
)




_HEARTBEATREQUEST = _descriptor.Descriptor(
  name='HeartbeatRequest',
  full_name='unary.HeartbeatRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_end=42,
)


_HEARTBEATRESPONSE = _descriptor.Descriptor(
  name='HeartbeatResponse',
  full_name='unary.HeartbeatResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=44,
  serialized_end=63,
)


_GETJOBREQUEST = _descriptor.Descriptor(
  name='GetJobRequest',
  full_name='unary.GetJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=65,
  serialized_end=80,
)


_GETJOBRESPONSE = _descriptor.Descriptor(
  name='GetJobResponse',
  full_name='unary.GetJobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=82,
  serialized_end=98,
)


_GETJOBEGGREQUEST = _descriptor.Descriptor(
  name='GetJobEggRequest',
  full_name='unary.GetJobEggRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=100,
  serialized_end=118,
)


_GETJOBEGGRESPONSE = _descriptor.Descriptor(
  name='GetJobEggResponse',
  full_name='unary.GetJobEggResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=120,
  serialized_end=139,
)


_COMPLETEJOBREQUEST = _descriptor.Descriptor(
  name='CompleteJobRequest',
  full_name='unary.CompleteJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=141,
  serialized_end=161,
)


_COMPLETEJOBRESPONSE = _descriptor.Descriptor(
  name='CompleteJobResponse',
  full_name='unary.CompleteJobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=163,
  serialized_end=184,
)

DESCRIPTOR.message_types_by_name['HeartbeatRequest'] = _HEARTBEATREQUEST
DESCRIPTOR.message_types_by_name['HeartbeatResponse'] = _HEARTBEATRESPONSE
DESCRIPTOR.message_types_by_name['GetJobRequest'] = _GETJOBREQUEST
DESCRIPTOR.message_types_by_name['GetJobResponse'] = _GETJOBRESPONSE
DESCRIPTOR.message_types_by_name['GetJobEggRequest'] = _GETJOBEGGREQUEST
DESCRIPTOR.message_types_by_name['GetJobEggResponse'] = _GETJOBEGGRESPONSE
DESCRIPTOR.message_types_by_name['CompleteJobRequest'] = _COMPLETEJOBREQUEST
DESCRIPTOR.message_types_by_name['CompleteJobResponse'] = _COMPLETEJOBRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HeartbeatRequest = _reflection.GeneratedProtocolMessageType('HeartbeatRequest', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEATREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:unary.HeartbeatRequest)
  })
_sym_db.RegisterMessage(HeartbeatRequest)

HeartbeatResponse = _reflection.GeneratedProtocolMessageType('HeartbeatResponse', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEATRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:unary.HeartbeatResponse)
  })
_sym_db.RegisterMessage(HeartbeatResponse)

GetJobRequest = _reflection.GeneratedProtocolMessageType('GetJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETJOBREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:unary.GetJobRequest)
  })
_sym_db.RegisterMessage(GetJobRequest)

GetJobResponse = _reflection.GeneratedProtocolMessageType('GetJobResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETJOBRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:unary.GetJobResponse)
  })
_sym_db.RegisterMessage(GetJobResponse)

GetJobEggRequest = _reflection.GeneratedProtocolMessageType('GetJobEggRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETJOBEGGREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:unary.GetJobEggRequest)
  })
_sym_db.RegisterMessage(GetJobEggRequest)

GetJobEggResponse = _reflection.GeneratedProtocolMessageType('GetJobEggResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETJOBEGGRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:unary.GetJobEggResponse)
  })
_sym_db.RegisterMessage(GetJobEggResponse)

CompleteJobRequest = _reflection.GeneratedProtocolMessageType('CompleteJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _COMPLETEJOBREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:unary.CompleteJobRequest)
  })
_sym_db.RegisterMessage(CompleteJobRequest)

CompleteJobResponse = _reflection.GeneratedProtocolMessageType('CompleteJobResponse', (_message.Message,), {
  'DESCRIPTOR' : _COMPLETEJOBRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:unary.CompleteJobResponse)
  })
_sym_db.RegisterMessage(CompleteJobResponse)



_NODESERVICE = _descriptor.ServiceDescriptor(
  name='NodeService',
  full_name='unary.NodeService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=187,
  serialized_end=449,
  methods=[
  _descriptor.MethodDescriptor(
    name='Heartbeat',
    full_name='unary.NodeService.Heartbeat',
    index=0,
    containing_service=None,
    input_type=_HEARTBEATREQUEST,
    output_type=_HEARTBEATRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetJob',
    full_name='unary.NodeService.GetJob',
    index=1,
    containing_service=None,
    input_type=_GETJOBREQUEST,
    output_type=_GETJOBRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetEgg',
    full_name='unary.NodeService.GetEgg',
    index=2,
    containing_service=None,
    input_type=_GETJOBEGGREQUEST,
    output_type=_GETJOBEGGREQUEST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CompleteJob',
    full_name='unary.NodeService.CompleteJob',
    index=3,
    containing_service=None,
    input_type=_COMPLETEJOBREQUEST,
    output_type=_COMPLETEJOBRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_NODESERVICE)

DESCRIPTOR.services_by_name['NodeService'] = _NODESERVICE

# @@protoc_insertion_point(module_scope)
