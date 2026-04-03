:github_url: hide



# OpenXRSpatialCapabilityConfigurationAruco

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialCapabilityConfigurationBaseHeader<class_OpenXRSpatialCapabilityConfigurationBaseHeader>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Configuration header for Aruco markers.


## Description

Configuration header for Aruco markers. Pass this to [OpenXRSpatialEntityExtension.create_spatial_context()<class_OpenXRSpatialEntityExtension_method_create_spatial_context>] to create a spatial context that can detect Aruco markers.


## Properties

> **TABLE**
> :widths: auto
>
> +----------------------------------------------------------------------------+----------------------------------------------------------------------------------------+--------+
> | :ref:`ArucoDict<enum_OpenXRSpatialCapabilityConfigurationAruco_ArucoDict>` | :ref:`aruco_dict<class_OpenXRSpatialCapabilityConfigurationAruco_property_aruco_dict>` | ``16`` |
> +----------------------------------------------------------------------------+----------------------------------------------------------------------------------------+--------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedInt64Array<class_PackedInt64Array>` | :ref:`get_enabled_components<class_OpenXRSpatialCapabilityConfigurationAruco_method_get_enabled_components>`\ (\ ) |const| |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **ArucoDict**: [🔗<enum_OpenXRSpatialCapabilityConfigurationAruco_ArucoDict>]



[ArucoDict<enum_OpenXRSpatialCapabilityConfigurationAruco_ArucoDict>] **ARUCO_DICT_4X4_50** = `1`

4 by 4 pixel Aruco marker dictionary with 50 IDs.



[ArucoDict<enum_OpenXRSpatialCapabilityConfigurationAruco_ArucoDict>] **ARUCO_DICT_4X4_100** = `2`

4 by 4 pixel Aruco marker dictionary with 100 IDs.



[ArucoDict<enum_OpenXRSpatialCapabilityConfigurationAruco_ArucoDict>] **ARUCO_DICT_4X4_250** = `3`

4 by 4 pixel Aruco marker dictionary with 250 IDs.



[ArucoDict<enum_OpenXRSpatialCapabilityConfigurationAruco_ArucoDict>] **ARUCO_DICT_4X4_1000** = `4`

4 by 4 pixel Aruco marker dictionary with 1000 IDs.



[ArucoDict<enum_OpenXRSpatialCapabilityConfigurationAruco_ArucoDict>] **ARUCO_DICT_5X5_50** = `5`

5 by 5 pixel Aruco marker dictionary with 50 IDs.



[ArucoDict<enum_OpenXRSpatialCapabilityConfigurationAruco_ArucoDict>] **ARUCO_DICT_5X5_100** = `6`

5 by 5 pixel Aruco marker dictionary with 100 IDs.



[ArucoDict<enum_OpenXRSpatialCapabilityConfigurationAruco_ArucoDict>] **ARUCO_DICT_5X5_250** = `7`

5 by 5 pixel Aruco marker dictionary with 250 IDs.



[ArucoDict<enum_OpenXRSpatialCapabilityConfigurationAruco_ArucoDict>] **ARUCO_DICT_5X5_1000** = `8`

5 by 5 pixel Aruco marker dictionary with 1000 IDs.



[ArucoDict<enum_OpenXRSpatialCapabilityConfigurationAruco_ArucoDict>] **ARUCO_DICT_6X6_50** = `9`

6 by 6 pixel Aruco marker dictionary with 50 IDs.



[ArucoDict<enum_OpenXRSpatialCapabilityConfigurationAruco_ArucoDict>] **ARUCO_DICT_6X6_100** = `10`

6 by 6 pixel Aruco marker dictionary with 100 IDs.



[ArucoDict<enum_OpenXRSpatialCapabilityConfigurationAruco_ArucoDict>] **ARUCO_DICT_6X6_250** = `11`

6 by 6 pixel Aruco marker dictionary with 250 IDs.



[ArucoDict<enum_OpenXRSpatialCapabilityConfigurationAruco_ArucoDict>] **ARUCO_DICT_6X6_1000** = `12`

6 by 6 pixel Aruco marker dictionary with 1000 IDs.



[ArucoDict<enum_OpenXRSpatialCapabilityConfigurationAruco_ArucoDict>] **ARUCO_DICT_7X7_50** = `13`

7 by 7 pixel Aruco marker dictionary with 50 IDs.



[ArucoDict<enum_OpenXRSpatialCapabilityConfigurationAruco_ArucoDict>] **ARUCO_DICT_7X7_100** = `14`

7 by 7 pixel Aruco marker dictionary with 100 IDs.



[ArucoDict<enum_OpenXRSpatialCapabilityConfigurationAruco_ArucoDict>] **ARUCO_DICT_7X7_250** = `15`

7 by 7 pixel Aruco marker dictionary with 250 IDs.



[ArucoDict<enum_OpenXRSpatialCapabilityConfigurationAruco_ArucoDict>] **ARUCO_DICT_7X7_1000** = `16`

7 by 7 pixel Aruco marker dictionary with 1000 IDs.


----


## Property Descriptions



[ArucoDict<enum_OpenXRSpatialCapabilityConfigurationAruco_ArucoDict>] **aruco_dict** = `16` [🔗<class_OpenXRSpatialCapabilityConfigurationAruco_property_aruco_dict>]


- |void| **set_aruco_dict**\ (\ value\: [ArucoDict<enum_OpenXRSpatialCapabilityConfigurationAruco_ArucoDict>]\ )
- [ArucoDict<enum_OpenXRSpatialCapabilityConfigurationAruco_ArucoDict>] **get_aruco_dict**\ (\ )

Dictionary to use to decode Aruco markers.

\ **Note:** Must be set before using this configuration to create a spatial context.


----


## Method Descriptions



[PackedInt64Array<class_PackedInt64Array>] **get_enabled_components**\ (\ ) |const| [🔗<class_OpenXRSpatialCapabilityConfigurationAruco_method_get_enabled_components>]

Returns the components enabled by this configuration.

\ **Note:** Only valid after this configuration was used to create a spatial context.

