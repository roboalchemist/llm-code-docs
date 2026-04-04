:github_url: hide



# OpenXRSpatialCapabilityConfigurationAnchor

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialCapabilityConfigurationBaseHeader<class_OpenXRSpatialCapabilityConfigurationBaseHeader>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Configuration header for spatial anchors.


## Description

Configuration header for spatial anchors. Pass this to [OpenXRSpatialEntityExtension.create_spatial_context()<class_OpenXRSpatialEntityExtension_method_create_spatial_context>] to create a spatial context with spatial anchor capabilities.


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedInt64Array<class_PackedInt64Array>` | :ref:`get_enabled_components<class_OpenXRSpatialCapabilityConfigurationAnchor_method_get_enabled_components>`\ (\ ) |const| |
> +-------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[PackedInt64Array<class_PackedInt64Array>] **get_enabled_components**\ (\ ) |const| [🔗<class_OpenXRSpatialCapabilityConfigurationAnchor_method_get_enabled_components>]

Returns the components enabled by this configuration.

\ **Note:** Only valid after this configuration was used to create a spatial context.

