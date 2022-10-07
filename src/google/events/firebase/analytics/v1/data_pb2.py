# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/events/firebase/analytics/v1/data.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n.google/events/firebase/analytics/v1/data.proto\x12#google.events.firebase.analytics.v1"\xa2\x01\n\x10\x41nalyticsLogData\x12\x45\n\x08user_dim\x18\x01 \x01(\x0b\x32\x33.google.events.firebase.analytics.v1.UserDimensions\x12G\n\tevent_dim\x18\x02 \x03(\x0b\x32\x34.google.events.firebase.analytics.v1.EventDimensions"\xb5\x05\n\x0eUserDimensions\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12#\n\x1b\x66irst_open_timestamp_micros\x18\x02 \x01(\x03\x12`\n\x0fuser_properties\x18\x03 \x03(\x0b\x32G.google.events.firebase.analytics.v1.UserDimensions.UserPropertiesEntry\x12\x44\n\x0b\x64\x65vice_info\x18\x04 \x01(\x0b\x32/.google.events.firebase.analytics.v1.DeviceInfo\x12>\n\x08geo_info\x18\x05 \x01(\x0b\x32,.google.events.firebase.analytics.v1.GeoInfo\x12>\n\x08\x61pp_info\x18\x06 \x01(\x0b\x32,.google.events.firebase.analytics.v1.AppInfo\x12J\n\x0etraffic_source\x18\x07 \x01(\x0b\x32\x32.google.events.firebase.analytics.v1.TrafficSource\x12J\n\x0b\x62undle_info\x18\x08 \x01(\x0b\x32\x35.google.events.firebase.analytics.v1.ExportBundleInfo\x12>\n\x08ltv_info\x18\t \x01(\x0b\x32,.google.events.firebase.analytics.v1.LtvInfo\x1am\n\x13UserPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x45\n\x05value\x18\x02 \x01(\x0b\x32\x36.google.events.firebase.analytics.v1.UserPropertyValue:\x02\x38\x01"\x82\x01\n\x11UserPropertyValue\x12\x42\n\x05value\x18\x01 \x01(\x0b\x32\x33.google.events.firebase.analytics.v1.AnalyticsValue\x12\x1a\n\x12set_timestamp_usec\x18\x02 \x01(\x03\x12\r\n\x05index\x18\x03 \x01(\x05"{\n\x0e\x41nalyticsValue\x12\x16\n\x0cstring_value\x18\x01 \x01(\tH\x00\x12\x13\n\tint_value\x18\x02 \x01(\x03H\x00\x12\x15\n\x0b\x66loat_value\x18\x03 \x01(\x02H\x00\x12\x16\n\x0c\x64ouble_value\x18\x04 \x01(\x01H\x00\x42\r\n\x0bparam_value"\xc0\x02\n\nDeviceInfo\x12\x17\n\x0f\x64\x65vice_category\x18\x01 \x01(\t\x12\x19\n\x11mobile_brand_name\x18\x02 \x01(\t\x12\x19\n\x11mobile_model_name\x18\x03 \x01(\t\x12\x1d\n\x15mobile_marketing_name\x18\x04 \x01(\t\x12\x14\n\x0c\x64\x65vice_model\x18\x0c \x01(\t\x12\x18\n\x10platform_version\x18\x06 \x01(\t\x12\x11\n\tdevice_id\x18\x07 \x01(\t\x12\x1c\n\x14resettable_device_id\x18\x08 \x01(\t\x12\x1d\n\x15user_default_language\x18\t \x01(\t\x12\'\n\x1f\x64\x65vice_time_zone_offset_seconds\x18\n \x01(\x05\x12\x1b\n\x13limited_ad_tracking\x18\x0b \x01(\x08"p\n\x07\x41ppInfo\x12\x13\n\x0b\x61pp_version\x18\x01 \x01(\t\x12\x17\n\x0f\x61pp_instance_id\x18\x02 \x01(\t\x12\x11\n\tapp_store\x18\x03 \x01(\t\x12\x14\n\x0c\x61pp_platform\x18\x04 \x01(\t\x12\x0e\n\x06\x61pp_id\x18\x05 \x01(\t"K\n\x07GeoInfo\x12\x11\n\tcontinent\x18\x01 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x02 \x01(\t\x12\x0e\n\x06region\x18\x03 \x01(\t\x12\x0c\n\x04\x63ity\x18\x04 \x01(\t"k\n\rTrafficSource\x12\x1e\n\x16user_acquired_campaign\x18\x02 \x01(\t\x12\x1c\n\x14user_acquired_source\x18\x03 \x01(\t\x12\x1c\n\x14user_acquired_medium\x18\x04 \x01(\t"V\n\x10\x45xportBundleInfo\x12\x1a\n\x12\x62undle_sequence_id\x18\x01 \x01(\x05\x12&\n\x1eserver_timestamp_offset_micros\x18\x02 \x01(\x03",\n\x07LtvInfo\x12\x0f\n\x07revenue\x18\x01 \x01(\x01\x12\x10\n\x08\x63urrency\x18\x02 \x01(\t"\xb6\x02\n\x0f\x45ventDimensions\x12\x0c\n\x04\x64\x61te\x18\x06 \x01(\t\x12\x0c\n\x04name\x18\x01 \x01(\t\x12P\n\x06params\x18\x02 \x03(\x0b\x32@.google.events.firebase.analytics.v1.EventDimensions.ParamsEntry\x12\x18\n\x10timestamp_micros\x18\x04 \x01(\x03\x12!\n\x19previous_timestamp_micros\x18\x05 \x01(\x03\x12\x14\n\x0cvalue_in_usd\x18\x07 \x01(\x01\x1a\x62\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x42\n\x05value\x18\x02 \x01(\x0b\x32\x33.google.events.firebase.analytics.v1.AnalyticsValue:\x02\x38\x01\x42/\xaa\x02,Google.Events.Protobuf.Firebase.Analytics.V1b\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "google.events.firebase.analytics.v1.data_pb2", globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = (
        b"\252\002,Google.Events.Protobuf.Firebase.Analytics.V1"
    )
    _USERDIMENSIONS_USERPROPERTIESENTRY._options = None
    _USERDIMENSIONS_USERPROPERTIESENTRY._serialized_options = b"8\001"
    _EVENTDIMENSIONS_PARAMSENTRY._options = None
    _EVENTDIMENSIONS_PARAMSENTRY._serialized_options = b"8\001"
    _ANALYTICSLOGDATA._serialized_start = 88
    _ANALYTICSLOGDATA._serialized_end = 250
    _USERDIMENSIONS._serialized_start = 253
    _USERDIMENSIONS._serialized_end = 946
    _USERDIMENSIONS_USERPROPERTIESENTRY._serialized_start = 837
    _USERDIMENSIONS_USERPROPERTIESENTRY._serialized_end = 946
    _USERPROPERTYVALUE._serialized_start = 949
    _USERPROPERTYVALUE._serialized_end = 1079
    _ANALYTICSVALUE._serialized_start = 1081
    _ANALYTICSVALUE._serialized_end = 1204
    _DEVICEINFO._serialized_start = 1207
    _DEVICEINFO._serialized_end = 1527
    _APPINFO._serialized_start = 1529
    _APPINFO._serialized_end = 1641
    _GEOINFO._serialized_start = 1643
    _GEOINFO._serialized_end = 1718
    _TRAFFICSOURCE._serialized_start = 1720
    _TRAFFICSOURCE._serialized_end = 1827
    _EXPORTBUNDLEINFO._serialized_start = 1829
    _EXPORTBUNDLEINFO._serialized_end = 1915
    _LTVINFO._serialized_start = 1917
    _LTVINFO._serialized_end = 1961
    _EVENTDIMENSIONS._serialized_start = 1964
    _EVENTDIMENSIONS._serialized_end = 2274
    _EVENTDIMENSIONS_PARAMSENTRY._serialized_start = 2176
    _EVENTDIMENSIONS_PARAMSENTRY._serialized_end = 2274
# @@protoc_insertion_point(module_scope)
