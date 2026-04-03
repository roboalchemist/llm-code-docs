# OpenXRSpatialCapabilityConfigurationBaseHeader

# OpenXRSpatialCapabilityConfigurationBaseHeader
Experimental:This class may be changed or removed in future versions.
Inherits:RefCounted<Object
Inherited By:OpenXRSpatialCapabilityConfigurationAnchor,OpenXRSpatialCapabilityConfigurationAprilTag,OpenXRSpatialCapabilityConfigurationAruco,OpenXRSpatialCapabilityConfigurationMicroQrCode,OpenXRSpatialCapabilityConfigurationPlaneTracking,OpenXRSpatialCapabilityConfigurationQrCode
Wrapper base class for OpenXR Spatial Capability Configuration headers.

## Description
Wrapper base class for OpenXR Spatial Capability Configuration headers. This class needs to be implemented for each capability configuration structure usable within OpenXR's spatial entities system.

## Methods

| int | _get_configuration()virtual |
|---|---|
| bool | _has_valid_configuration()virtualconst |
| bool | has_valid_configuration()const |

_get_configuration()virtual
bool
_has_valid_configuration()virtualconst
bool
has_valid_configuration()const

## Method Descriptions
int_get_configuration()virtual🔗
Return a pointer (encoded as anint64_t) to a struct holding the spatial capability configuration data. The memory for this struct should remain accessible as long as this object remains instantiated.
bool_has_valid_configuration()virtualconst🔗
Returntrueif this object contains a valid configuration that can be retrieved when calling_get_configuration().
boolhas_valid_configuration()const🔗
Returnstrueif this object contains a valid configuration that can be used when callingOpenXRSpatialEntityExtension.create_spatial_context().

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.