:github_url: hide



# OpenXRSpatialCapabilityConfigurationBaseHeader

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [OpenXRSpatialCapabilityConfigurationAnchor<class_OpenXRSpatialCapabilityConfigurationAnchor>], [OpenXRSpatialCapabilityConfigurationAprilTag<class_OpenXRSpatialCapabilityConfigurationAprilTag>], [OpenXRSpatialCapabilityConfigurationAruco<class_OpenXRSpatialCapabilityConfigurationAruco>], [OpenXRSpatialCapabilityConfigurationMicroQrCode<class_OpenXRSpatialCapabilityConfigurationMicroQrCode>], [OpenXRSpatialCapabilityConfigurationPlaneTracking<class_OpenXRSpatialCapabilityConfigurationPlaneTracking>], [OpenXRSpatialCapabilityConfigurationQrCode<class_OpenXRSpatialCapabilityConfigurationQrCode>]

Wrapper base class for OpenXR Spatial Capability Configuration headers.


## Description

Wrapper base class for OpenXR Spatial Capability Configuration headers. This class needs to be implemented for each capability configuration structure usable within OpenXR's spatial entities system.


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`   | :ref:`_get_configuration<class_OpenXRSpatialCapabilityConfigurationBaseHeader_private_method__get_configuration>`\ (\ ) |virtual|                     |
> +-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`_has_valid_configuration<class_OpenXRSpatialCapabilityConfigurationBaseHeader_private_method__has_valid_configuration>`\ (\ ) |virtual| |const| |
> +-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`has_valid_configuration<class_OpenXRSpatialCapabilityConfigurationBaseHeader_method_has_valid_configuration>`\ (\ ) |const|                     |
> +-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[int<class_int>] **_get_configuration**\ (\ ) |virtual| [🔗<class_OpenXRSpatialCapabilityConfigurationBaseHeader_private_method__get_configuration>]

Return a pointer (encoded as an `int64_t`) to a struct holding the spatial capability configuration data. The memory for this struct should remain accessible as long as this object remains instantiated.


----



[bool<class_bool>] **_has_valid_configuration**\ (\ ) |virtual| |const| [🔗<class_OpenXRSpatialCapabilityConfigurationBaseHeader_private_method__has_valid_configuration>]

Return `true` if this object contains a valid configuration that can be retrieved when calling [_get_configuration()<class_OpenXRSpatialCapabilityConfigurationBaseHeader_private_method__get_configuration>].


----



[bool<class_bool>] **has_valid_configuration**\ (\ ) |const| [🔗<class_OpenXRSpatialCapabilityConfigurationBaseHeader_method_has_valid_configuration>]

Returns `true` if this object contains a valid configuration that can be used when calling [OpenXRSpatialEntityExtension.create_spatial_context()<class_OpenXRSpatialEntityExtension_method_create_spatial_context>].

