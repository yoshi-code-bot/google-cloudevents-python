# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/events/cloud/iot/v1/data.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/events/cloud/iot/v1/data.proto\x12\x1agoogle.events.cloud.iot.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\"\xe5\x06\n\x06\x44\x65vice\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06num_id\x18\x03 \x01(\x04\x12\x41\n\x0b\x63redentials\x18\x0c \x03(\x0b\x32,.google.events.cloud.iot.v1.DeviceCredential\x12\x37\n\x13last_heartbeat_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0flast_event_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0flast_state_time\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x38\n\x14last_config_ack_time\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x39\n\x15last_config_send_time\x18\x12 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07\x62locked\x18\x13 \x01(\x08\x12\x33\n\x0flast_error_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\x11last_error_status\x18\x0b \x01(\x0b\x32\x12.google.rpc.Status\x12\x38\n\x06\x63onfig\x18\r \x01(\x0b\x32(.google.events.cloud.iot.v1.DeviceConfig\x12\x36\n\x05state\x18\x10 \x01(\x0b\x32\'.google.events.cloud.iot.v1.DeviceState\x12\x37\n\tlog_level\x18\x15 \x01(\x0e\x32$.google.events.cloud.iot.v1.LogLevel\x12\x42\n\x08metadata\x18\x11 \x03(\x0b\x32\x30.google.events.cloud.iot.v1.Device.MetadataEntry\x12\x41\n\x0egateway_config\x18\x18 \x01(\x0b\x32).google.events.cloud.iot.v1.GatewayConfig\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xfc\x01\n\rGatewayConfig\x12=\n\x0cgateway_type\x18\x01 \x01(\x0e\x32\'.google.events.cloud.iot.v1.GatewayType\x12J\n\x13gateway_auth_method\x18\x02 \x01(\x0e\x32-.google.events.cloud.iot.v1.GatewayAuthMethod\x12 \n\x18last_accessed_gateway_id\x18\x03 \x01(\t\x12>\n\x1alast_accessed_gateway_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xd3\x03\n\x0e\x44\x65viceRegistry\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12W\n\x1a\x65vent_notification_configs\x18\n \x03(\x0b\x32\x33.google.events.cloud.iot.v1.EventNotificationConfig\x12V\n\x19state_notification_config\x18\x07 \x01(\x0b\x32\x33.google.events.cloud.iot.v1.StateNotificationConfig\x12;\n\x0bmqtt_config\x18\x04 \x01(\x0b\x32&.google.events.cloud.iot.v1.MqttConfig\x12;\n\x0bhttp_config\x18\t \x01(\x0b\x32&.google.events.cloud.iot.v1.HttpConfig\x12\x37\n\tlog_level\x18\x0b \x01(\x0e\x32$.google.events.cloud.iot.v1.LogLevel\x12\x43\n\x0b\x63redentials\x18\x08 \x03(\x0b\x32..google.events.cloud.iot.v1.RegistryCredential\"O\n\nMqttConfig\x12\x41\n\x12mqtt_enabled_state\x18\x01 \x01(\x0e\x32%.google.events.cloud.iot.v1.MqttState\"O\n\nHttpConfig\x12\x41\n\x12http_enabled_state\x18\x01 \x01(\x0e\x32%.google.events.cloud.iot.v1.HttpState\"O\n\x17\x45ventNotificationConfig\x12\x19\n\x11subfolder_matches\x18\x02 \x01(\t\x12\x19\n\x11pubsub_topic_name\x18\x01 \x01(\t\"4\n\x17StateNotificationConfig\x12\x19\n\x11pubsub_topic_name\x18\x01 \x01(\t\"v\n\x12RegistryCredential\x12R\n\x16public_key_certificate\x18\x01 \x01(\x0b\x32\x30.google.events.cloud.iot.v1.PublicKeyCertificateH\x00\x42\x0c\n\ncredential\"\xd0\x01\n\x16X509CertificateDetails\x12\x0e\n\x06issuer\x18\x01 \x01(\t\x12\x0f\n\x07subject\x18\x02 \x01(\t\x12.\n\nstart_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x65xpiry_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1b\n\x13signature_algorithm\x18\x05 \x01(\t\x12\x17\n\x0fpublic_key_type\x18\x06 \x01(\t\"\xbd\x01\n\x14PublicKeyCertificate\x12\x46\n\x06\x66ormat\x18\x01 \x01(\x0e\x32\x36.google.events.cloud.iot.v1.PublicKeyCertificateFormat\x12\x13\n\x0b\x63\x65rtificate\x18\x02 \x01(\t\x12H\n\x0cx509_details\x18\x03 \x01(\x0b\x32\x32.google.events.cloud.iot.v1.X509CertificateDetails\"\x9c\x01\n\x10\x44\x65viceCredential\x12\x45\n\npublic_key\x18\x02 \x01(\x0b\x32/.google.events.cloud.iot.v1.PublicKeyCredentialH\x00\x12\x33\n\x0f\x65xpiration_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x0c\n\ncredential\"_\n\x13PublicKeyCredential\x12;\n\x06\x66ormat\x18\x01 \x01(\x0e\x32+.google.events.cloud.iot.v1.PublicKeyFormat\x12\x0b\n\x03key\x18\x02 \x01(\t\"\xa0\x01\n\x0c\x44\x65viceConfig\x12\x0f\n\x07version\x18\x01 \x01(\x03\x12\x35\n\x11\x63loud_update_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0f\x64\x65vice_ack_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0b\x62inary_data\x18\x04 \x01(\x0c\"S\n\x0b\x44\x65viceState\x12/\n\x0bupdate_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0b\x62inary_data\x18\x02 \x01(\x0c\"W\n\x0f\x44\x65viceEventData\x12\x38\n\x07payload\x18\x01 \x01(\x0b\x32\".google.events.cloud.iot.v1.DeviceH\x00\x88\x01\x01\x42\n\n\x08_payload\"a\n\x11RegistryEventData\x12@\n\x07payload\x18\x01 \x01(\x0b\x32*.google.events.cloud.iot.v1.DeviceRegistryH\x00\x88\x01\x01\x42\n\n\x08_payload*L\n\tMqttState\x12\x1a\n\x16MQTT_STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cMQTT_ENABLED\x10\x01\x12\x11\n\rMQTT_DISABLED\x10\x02*L\n\tHttpState\x12\x1a\n\x16HTTP_STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cHTTP_ENABLED\x10\x01\x12\x11\n\rHTTP_DISABLED\x10\x02*O\n\x08LogLevel\x12\x19\n\x15LOG_LEVEL_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\n\x12\t\n\x05\x45RROR\x10\x14\x12\x08\n\x04INFO\x10\x1e\x12\t\n\x05\x44\x45\x42UG\x10(*I\n\x0bGatewayType\x12\x1c\n\x18GATEWAY_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07GATEWAY\x10\x01\x12\x0f\n\x0bNON_GATEWAY\x10\x02*\x91\x01\n\x11GatewayAuthMethod\x12#\n\x1fGATEWAY_AUTH_METHOD_UNSPECIFIED\x10\x00\x12\x14\n\x10\x41SSOCIATION_ONLY\x10\x01\x12\x1a\n\x16\x44\x45VICE_AUTH_TOKEN_ONLY\x10\x02\x12%\n!ASSOCIATION_AND_DEVICE_AUTH_TOKEN\x10\x03*e\n\x1aPublicKeyCertificateFormat\x12-\n)UNSPECIFIED_PUBLIC_KEY_CERTIFICATE_FORMAT\x10\x00\x12\x18\n\x14X509_CERTIFICATE_PEM\x10\x01*v\n\x0fPublicKeyFormat\x12!\n\x1dUNSPECIFIED_PUBLIC_KEY_FORMAT\x10\x00\x12\x0b\n\x07RSA_PEM\x10\x03\x12\x10\n\x0cRSA_X509_PEM\x10\x01\x12\r\n\tES256_PEM\x10\x02\x12\x12\n\x0e\x45S256_X509_PEM\x10\x04\x42&\xaa\x02#Google.Events.Protobuf.Cloud.Iot.V1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.events.cloud.iot.v1.data_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002#Google.Events.Protobuf.Cloud.Iot.V1'
  _DEVICE_METADATAENTRY._options = None
  _DEVICE_METADATAENTRY._serialized_options = b'8\001'
  _MQTTSTATE._serialized_start=3236
  _MQTTSTATE._serialized_end=3312
  _HTTPSTATE._serialized_start=3314
  _HTTPSTATE._serialized_end=3390
  _LOGLEVEL._serialized_start=3392
  _LOGLEVEL._serialized_end=3471
  _GATEWAYTYPE._serialized_start=3473
  _GATEWAYTYPE._serialized_end=3546
  _GATEWAYAUTHMETHOD._serialized_start=3549
  _GATEWAYAUTHMETHOD._serialized_end=3694
  _PUBLICKEYCERTIFICATEFORMAT._serialized_start=3696
  _PUBLICKEYCERTIFICATEFORMAT._serialized_end=3797
  _PUBLICKEYFORMAT._serialized_start=3799
  _PUBLICKEYFORMAT._serialized_end=3917
  _DEVICE._serialized_start=128
  _DEVICE._serialized_end=997
  _DEVICE_METADATAENTRY._serialized_start=950
  _DEVICE_METADATAENTRY._serialized_end=997
  _GATEWAYCONFIG._serialized_start=1000
  _GATEWAYCONFIG._serialized_end=1252
  _DEVICEREGISTRY._serialized_start=1255
  _DEVICEREGISTRY._serialized_end=1722
  _MQTTCONFIG._serialized_start=1724
  _MQTTCONFIG._serialized_end=1803
  _HTTPCONFIG._serialized_start=1805
  _HTTPCONFIG._serialized_end=1884
  _EVENTNOTIFICATIONCONFIG._serialized_start=1886
  _EVENTNOTIFICATIONCONFIG._serialized_end=1965
  _STATENOTIFICATIONCONFIG._serialized_start=1967
  _STATENOTIFICATIONCONFIG._serialized_end=2019
  _REGISTRYCREDENTIAL._serialized_start=2021
  _REGISTRYCREDENTIAL._serialized_end=2139
  _X509CERTIFICATEDETAILS._serialized_start=2142
  _X509CERTIFICATEDETAILS._serialized_end=2350
  _PUBLICKEYCERTIFICATE._serialized_start=2353
  _PUBLICKEYCERTIFICATE._serialized_end=2542
  _DEVICECREDENTIAL._serialized_start=2545
  _DEVICECREDENTIAL._serialized_end=2701
  _PUBLICKEYCREDENTIAL._serialized_start=2703
  _PUBLICKEYCREDENTIAL._serialized_end=2798
  _DEVICECONFIG._serialized_start=2801
  _DEVICECONFIG._serialized_end=2961
  _DEVICESTATE._serialized_start=2963
  _DEVICESTATE._serialized_end=3046
  _DEVICEEVENTDATA._serialized_start=3048
  _DEVICEEVENTDATA._serialized_end=3135
  _REGISTRYEVENTDATA._serialized_start=3137
  _REGISTRYEVENTDATA._serialized_end=3234
# @@protoc_insertion_point(module_scope)