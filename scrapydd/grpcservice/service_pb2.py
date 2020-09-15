# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: scrapydd/grpcservice/service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='scrapydd/grpcservice/service.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\"scrapydd/grpcservice/service.proto\"j\n\x04Node\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x03\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\x12\x0c\n\x04tags\x18\x04 \x03(\t\x12\x11\n\tis_online\x18\x06 \x01(\x08\x12\x11\n\tclient_ip\x18\x07 \x01(\t\"8\n\x0bNodeSession\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x03\x12\x0f\n\x07node_id\x18\x03 \x01(\x03\"+\n\x1bObtainNodeSessionJobRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\":\n\x0eNodeSessionJob\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0e\n\x06\x66igure\x18\x03 \x01(\t\"\'\n\x11GetNextJobRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\"D\n\x12GetNextJobResponse\x12\r\n\x05jobId\x18\x01 \x01(\t\x12\x0e\n\x06\x66igure\x18\x02 \x01(\t\x12\x0f\n\x07package\x18\x03 \x01(\x0c\"P\n\x12\x43ompleteJobRequest\x12\r\n\x05jobId\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x0c\n\x04logs\x18\x03 \x01(\x0c\x12\r\n\x05items\x18\x04 \x01(\x0c\"\x15\n\x13\x43ompleteJobResponse\">\n\x18\x43reateNodeSessionRequest\x12\"\n\x0cnode_session\x18\x02 \x01(\x0b\x32\x0c.NodeSession\":\n\x11\x43reateNodeRequest\x12\x13\n\x04node\x18\x02 \x01(\x0b\x32\x05.Node\x12\x10\n\x08node_key\x18\x03 \x01(\t\"D\n\x1bHeartbeatNodeSessionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x17\n\x0frunning_job_ids\x18\x02 \x03(\t\"O\n\x1cHeartbeatNodeSessionResponse\x12\x14\n\x0ckill_job_ids\x18\x01 \x03(\t\x12\x19\n\x11new_job_available\x18\x02 \x01(\x08\"+\n\x1bGetNodeSessionJobEggRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x19\n\tDataChunk\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x32\xc5\x03\n\x0bNodeService\x12\'\n\nCreateNode\x12\x12.CreateNodeRequest\x1a\x05.Node\x12<\n\x11\x43reateNodeSession\x12\x19.CreateNodeSessionRequest\x1a\x0c.NodeSession\x12S\n\x14HeartbeatNodeSession\x12\x1c.HeartbeatNodeSessionRequest\x1a\x1d.HeartbeatNodeSessionResponse\x12\x45\n\x14ObtainNodeSessionJob\x12\x1c.ObtainNodeSessionJobRequest\x1a\x0f.NodeSessionJob\x12\x42\n\x14GetNodeSessionJobEgg\x12\x1c.GetNodeSessionJobEggRequest\x1a\n.DataChunk0\x01\x12\x35\n\nGetNextJob\x12\x12.GetNextJobRequest\x1a\x13.GetNextJobResponse\x12\x38\n\x0b\x43ompleteJob\x12\x13.CompleteJobRequest\x1a\x14.CompleteJobResponseb\x06proto3')
)




_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Node.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='Node.id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='Node.display_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='Node.tags', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_online', full_name='Node.is_online', index=4,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_ip', full_name='Node.client_ip', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=144,
)


_NODESESSION = _descriptor.Descriptor(
  name='NodeSession',
  full_name='NodeSession',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='NodeSession.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='NodeSession.id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_id', full_name='NodeSession.node_id', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=146,
  serialized_end=202,
)


_OBTAINNODESESSIONJOBREQUEST = _descriptor.Descriptor(
  name='ObtainNodeSessionJobRequest',
  full_name='ObtainNodeSessionJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ObtainNodeSessionJobRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=204,
  serialized_end=247,
)


_NODESESSIONJOB = _descriptor.Descriptor(
  name='NodeSessionJob',
  full_name='NodeSessionJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='NodeSessionJob.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='NodeSessionJob.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='figure', full_name='NodeSessionJob.figure', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=249,
  serialized_end=307,
)


_GETNEXTJOBREQUEST = _descriptor.Descriptor(
  name='GetNextJobRequest',
  full_name='GetNextJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='GetNextJobRequest.session_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=309,
  serialized_end=348,
)


_GETNEXTJOBRESPONSE = _descriptor.Descriptor(
  name='GetNextJobResponse',
  full_name='GetNextJobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jobId', full_name='GetNextJobResponse.jobId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='figure', full_name='GetNextJobResponse.figure', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package', full_name='GetNextJobResponse.package', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=350,
  serialized_end=418,
)


_COMPLETEJOBREQUEST = _descriptor.Descriptor(
  name='CompleteJobRequest',
  full_name='CompleteJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jobId', full_name='CompleteJobRequest.jobId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='CompleteJobRequest.status', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logs', full_name='CompleteJobRequest.logs', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='items', full_name='CompleteJobRequest.items', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=420,
  serialized_end=500,
)


_COMPLETEJOBRESPONSE = _descriptor.Descriptor(
  name='CompleteJobResponse',
  full_name='CompleteJobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=502,
  serialized_end=523,
)


_CREATENODESESSIONREQUEST = _descriptor.Descriptor(
  name='CreateNodeSessionRequest',
  full_name='CreateNodeSessionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_session', full_name='CreateNodeSessionRequest.node_session', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=525,
  serialized_end=587,
)


_CREATENODEREQUEST = _descriptor.Descriptor(
  name='CreateNodeRequest',
  full_name='CreateNodeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='CreateNodeRequest.node', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_key', full_name='CreateNodeRequest.node_key', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=589,
  serialized_end=647,
)


_HEARTBEATNODESESSIONREQUEST = _descriptor.Descriptor(
  name='HeartbeatNodeSessionRequest',
  full_name='HeartbeatNodeSessionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='HeartbeatNodeSessionRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='running_job_ids', full_name='HeartbeatNodeSessionRequest.running_job_ids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=649,
  serialized_end=717,
)


_HEARTBEATNODESESSIONRESPONSE = _descriptor.Descriptor(
  name='HeartbeatNodeSessionResponse',
  full_name='HeartbeatNodeSessionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='kill_job_ids', full_name='HeartbeatNodeSessionResponse.kill_job_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_job_available', full_name='HeartbeatNodeSessionResponse.new_job_available', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=719,
  serialized_end=798,
)


_GETNODESESSIONJOBEGGREQUEST = _descriptor.Descriptor(
  name='GetNodeSessionJobEggRequest',
  full_name='GetNodeSessionJobEggRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='GetNodeSessionJobEggRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=800,
  serialized_end=843,
)


_DATACHUNK = _descriptor.Descriptor(
  name='DataChunk',
  full_name='DataChunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='DataChunk.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=845,
  serialized_end=870,
)

_CREATENODESESSIONREQUEST.fields_by_name['node_session'].message_type = _NODESESSION
_CREATENODEREQUEST.fields_by_name['node'].message_type = _NODE
DESCRIPTOR.message_types_by_name['Node'] = _NODE
DESCRIPTOR.message_types_by_name['NodeSession'] = _NODESESSION
DESCRIPTOR.message_types_by_name['ObtainNodeSessionJobRequest'] = _OBTAINNODESESSIONJOBREQUEST
DESCRIPTOR.message_types_by_name['NodeSessionJob'] = _NODESESSIONJOB
DESCRIPTOR.message_types_by_name['GetNextJobRequest'] = _GETNEXTJOBREQUEST
DESCRIPTOR.message_types_by_name['GetNextJobResponse'] = _GETNEXTJOBRESPONSE
DESCRIPTOR.message_types_by_name['CompleteJobRequest'] = _COMPLETEJOBREQUEST
DESCRIPTOR.message_types_by_name['CompleteJobResponse'] = _COMPLETEJOBRESPONSE
DESCRIPTOR.message_types_by_name['CreateNodeSessionRequest'] = _CREATENODESESSIONREQUEST
DESCRIPTOR.message_types_by_name['CreateNodeRequest'] = _CREATENODEREQUEST
DESCRIPTOR.message_types_by_name['HeartbeatNodeSessionRequest'] = _HEARTBEATNODESESSIONREQUEST
DESCRIPTOR.message_types_by_name['HeartbeatNodeSessionResponse'] = _HEARTBEATNODESESSIONRESPONSE
DESCRIPTOR.message_types_by_name['GetNodeSessionJobEggRequest'] = _GETNODESESSIONJOBEGGREQUEST
DESCRIPTOR.message_types_by_name['DataChunk'] = _DATACHUNK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), dict(
  DESCRIPTOR = _NODE,
  __module__ = 'scrapydd.grpcservice.service_pb2'
  # @@protoc_insertion_point(class_scope:Node)
  ))
_sym_db.RegisterMessage(Node)

NodeSession = _reflection.GeneratedProtocolMessageType('NodeSession', (_message.Message,), dict(
  DESCRIPTOR = _NODESESSION,
  __module__ = 'scrapydd.grpcservice.service_pb2'
  # @@protoc_insertion_point(class_scope:NodeSession)
  ))
_sym_db.RegisterMessage(NodeSession)

ObtainNodeSessionJobRequest = _reflection.GeneratedProtocolMessageType('ObtainNodeSessionJobRequest', (_message.Message,), dict(
  DESCRIPTOR = _OBTAINNODESESSIONJOBREQUEST,
  __module__ = 'scrapydd.grpcservice.service_pb2'
  # @@protoc_insertion_point(class_scope:ObtainNodeSessionJobRequest)
  ))
_sym_db.RegisterMessage(ObtainNodeSessionJobRequest)

NodeSessionJob = _reflection.GeneratedProtocolMessageType('NodeSessionJob', (_message.Message,), dict(
  DESCRIPTOR = _NODESESSIONJOB,
  __module__ = 'scrapydd.grpcservice.service_pb2'
  # @@protoc_insertion_point(class_scope:NodeSessionJob)
  ))
_sym_db.RegisterMessage(NodeSessionJob)

GetNextJobRequest = _reflection.GeneratedProtocolMessageType('GetNextJobRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETNEXTJOBREQUEST,
  __module__ = 'scrapydd.grpcservice.service_pb2'
  # @@protoc_insertion_point(class_scope:GetNextJobRequest)
  ))
_sym_db.RegisterMessage(GetNextJobRequest)

GetNextJobResponse = _reflection.GeneratedProtocolMessageType('GetNextJobResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETNEXTJOBRESPONSE,
  __module__ = 'scrapydd.grpcservice.service_pb2'
  # @@protoc_insertion_point(class_scope:GetNextJobResponse)
  ))
_sym_db.RegisterMessage(GetNextJobResponse)

CompleteJobRequest = _reflection.GeneratedProtocolMessageType('CompleteJobRequest', (_message.Message,), dict(
  DESCRIPTOR = _COMPLETEJOBREQUEST,
  __module__ = 'scrapydd.grpcservice.service_pb2'
  # @@protoc_insertion_point(class_scope:CompleteJobRequest)
  ))
_sym_db.RegisterMessage(CompleteJobRequest)

CompleteJobResponse = _reflection.GeneratedProtocolMessageType('CompleteJobResponse', (_message.Message,), dict(
  DESCRIPTOR = _COMPLETEJOBRESPONSE,
  __module__ = 'scrapydd.grpcservice.service_pb2'
  # @@protoc_insertion_point(class_scope:CompleteJobResponse)
  ))
_sym_db.RegisterMessage(CompleteJobResponse)

CreateNodeSessionRequest = _reflection.GeneratedProtocolMessageType('CreateNodeSessionRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATENODESESSIONREQUEST,
  __module__ = 'scrapydd.grpcservice.service_pb2'
  # @@protoc_insertion_point(class_scope:CreateNodeSessionRequest)
  ))
_sym_db.RegisterMessage(CreateNodeSessionRequest)

CreateNodeRequest = _reflection.GeneratedProtocolMessageType('CreateNodeRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATENODEREQUEST,
  __module__ = 'scrapydd.grpcservice.service_pb2'
  # @@protoc_insertion_point(class_scope:CreateNodeRequest)
  ))
_sym_db.RegisterMessage(CreateNodeRequest)

HeartbeatNodeSessionRequest = _reflection.GeneratedProtocolMessageType('HeartbeatNodeSessionRequest', (_message.Message,), dict(
  DESCRIPTOR = _HEARTBEATNODESESSIONREQUEST,
  __module__ = 'scrapydd.grpcservice.service_pb2'
  # @@protoc_insertion_point(class_scope:HeartbeatNodeSessionRequest)
  ))
_sym_db.RegisterMessage(HeartbeatNodeSessionRequest)

HeartbeatNodeSessionResponse = _reflection.GeneratedProtocolMessageType('HeartbeatNodeSessionResponse', (_message.Message,), dict(
  DESCRIPTOR = _HEARTBEATNODESESSIONRESPONSE,
  __module__ = 'scrapydd.grpcservice.service_pb2'
  # @@protoc_insertion_point(class_scope:HeartbeatNodeSessionResponse)
  ))
_sym_db.RegisterMessage(HeartbeatNodeSessionResponse)

GetNodeSessionJobEggRequest = _reflection.GeneratedProtocolMessageType('GetNodeSessionJobEggRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETNODESESSIONJOBEGGREQUEST,
  __module__ = 'scrapydd.grpcservice.service_pb2'
  # @@protoc_insertion_point(class_scope:GetNodeSessionJobEggRequest)
  ))
_sym_db.RegisterMessage(GetNodeSessionJobEggRequest)

DataChunk = _reflection.GeneratedProtocolMessageType('DataChunk', (_message.Message,), dict(
  DESCRIPTOR = _DATACHUNK,
  __module__ = 'scrapydd.grpcservice.service_pb2'
  # @@protoc_insertion_point(class_scope:DataChunk)
  ))
_sym_db.RegisterMessage(DataChunk)



_NODESERVICE = _descriptor.ServiceDescriptor(
  name='NodeService',
  full_name='NodeService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=873,
  serialized_end=1326,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateNode',
    full_name='NodeService.CreateNode',
    index=0,
    containing_service=None,
    input_type=_CREATENODEREQUEST,
    output_type=_NODE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateNodeSession',
    full_name='NodeService.CreateNodeSession',
    index=1,
    containing_service=None,
    input_type=_CREATENODESESSIONREQUEST,
    output_type=_NODESESSION,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='HeartbeatNodeSession',
    full_name='NodeService.HeartbeatNodeSession',
    index=2,
    containing_service=None,
    input_type=_HEARTBEATNODESESSIONREQUEST,
    output_type=_HEARTBEATNODESESSIONRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ObtainNodeSessionJob',
    full_name='NodeService.ObtainNodeSessionJob',
    index=3,
    containing_service=None,
    input_type=_OBTAINNODESESSIONJOBREQUEST,
    output_type=_NODESESSIONJOB,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetNodeSessionJobEgg',
    full_name='NodeService.GetNodeSessionJobEgg',
    index=4,
    containing_service=None,
    input_type=_GETNODESESSIONJOBEGGREQUEST,
    output_type=_DATACHUNK,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetNextJob',
    full_name='NodeService.GetNextJob',
    index=5,
    containing_service=None,
    input_type=_GETNEXTJOBREQUEST,
    output_type=_GETNEXTJOBRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CompleteJob',
    full_name='NodeService.CompleteJob',
    index=6,
    containing_service=None,
    input_type=_COMPLETEJOBREQUEST,
    output_type=_COMPLETEJOBRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_NODESERVICE)

DESCRIPTOR.services_by_name['NodeService'] = _NODESERVICE

# @@protoc_insertion_point(module_scope)
