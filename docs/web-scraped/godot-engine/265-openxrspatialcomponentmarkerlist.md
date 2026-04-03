# OpenXRSpatialComponentMarkerList

# OpenXRSpatialComponentMarkerList
Experimental:This class may be changed or removed in future versions.
Inherits:OpenXRSpatialComponentData<RefCounted<Object
Object for storing the queries marker result data.

## Description
Object for storing the queries marker result data when callingOpenXRSpatialEntityExtension.query_snapshot().

## Methods

| Variant | get_marker_data(snapshot:RID, index:int)const |
|---|---|
| int | get_marker_id(index:int)const |
| MarkerType | get_marker_type(index:int)const |

Variant
get_marker_data(snapshot:RID, index:int)const
get_marker_id(index:int)const
MarkerType
get_marker_type(index:int)const

## Enumerations
enumMarkerType:🔗
MarkerTypeMARKER_TYPE_UNKNOWN=0
Unknown or unset marker type.
MarkerTypeMARKER_TYPE_QRCODE=1
Marker based on a QR code.
MarkerTypeMARKER_TYPE_MICRO_QRCODE=2
Marker based on a micro QR code.
MarkerTypeMARKER_TYPE_ARUCO=3
Marker based on an Aruco code.
MarkerTypeMARKER_TYPE_APRIL_TAG=4
Marker based on an April Tag.
MarkerTypeMARKER_TYPE_MAX=5
Maximum value for this enum.

## Method Descriptions
Variantget_marker_data(snapshot:RID, index:int)const🔗
Returns either aStringor aPackedByteArraybuffer with data for the marker at thisindex. Only applicable for QR code markers.
intget_marker_id(index:int)const🔗
Returns the marker ID for the marker at thisindex. Only applicable for Aruco or April Tag markers.
MarkerTypeget_marker_type(index:int)const🔗
Returns the marker type for the marker at thisindex.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.