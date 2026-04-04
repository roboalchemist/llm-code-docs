:github_url: hide



# OpenXRMarkerTracker

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialEntityTracker<class_OpenXRSpatialEntityTracker>] **<** [XRPositionalTracker<class_XRPositionalTracker>] **<** [XRTracker<class_XRTracker>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Spatial entity tracker for our spatial entity marker tracking extension.


## Description

Spatial entity tracker for our OpenXR spatial entity marker tracking extension. These trackers identify entities in our real space detected by a visual marker such as a QRCode or Aruco code, and map their location to our virtual space.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------------------------+--------------------------------------------------------------------+-------------------+
> | :ref:`Vector2<class_Vector2>`                                       | :ref:`bounds_size<class_OpenXRMarkerTracker_property_bounds_size>` | ``Vector2(0, 0)`` |
> +---------------------------------------------------------------------+--------------------------------------------------------------------+-------------------+
> | :ref:`int<class_int>`                                               | :ref:`marker_id<class_OpenXRMarkerTracker_property_marker_id>`     | ``0``             |
> +---------------------------------------------------------------------+--------------------------------------------------------------------+-------------------+
> | :ref:`MarkerType<enum_OpenXRSpatialComponentMarkerList_MarkerType>` | :ref:`marker_type<class_OpenXRMarkerTracker_property_marker_type>` | ``0``             |
> +---------------------------------------------------------------------+--------------------------------------------------------------------+-------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>` | :ref:`get_marker_data<class_OpenXRMarkerTracker_method_get_marker_data>`\ (\ ) |const|                                      |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`set_marker_data<class_OpenXRMarkerTracker_method_set_marker_data>`\ (\ marker_data\: :ref:`Variant<class_Variant>`\ ) |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[Vector2<class_Vector2>] **bounds_size** = `Vector2(0, 0)` [🔗<class_OpenXRMarkerTracker_property_bounds_size>]


- |void| **set_bounds_size**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_bounds_size**\ (\ )

The bounds size for this marker.


----



[int<class_int>] **marker_id** = `0` [🔗<class_OpenXRMarkerTracker_property_marker_id>]


- |void| **set_marker_id**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_marker_id**\ (\ )

The marker ID for this marker, this is only returned for Aruco and April Tag markers. Call [get_marker_data()<class_OpenXRMarkerTracker_method_get_marker_data>] for QRCode markers.


----



[MarkerType<enum_OpenXRSpatialComponentMarkerList_MarkerType>] **marker_type** = `0` [🔗<class_OpenXRMarkerTracker_property_marker_type>]


- |void| **set_marker_type**\ (\ value\: [MarkerType<enum_OpenXRSpatialComponentMarkerList_MarkerType>]\ )
- [MarkerType<enum_OpenXRSpatialComponentMarkerList_MarkerType>] **get_marker_type**\ (\ )

The type of marker.


----


## Method Descriptions



[Variant<class_Variant>] **get_marker_data**\ (\ ) |const| [🔗<class_OpenXRMarkerTracker_method_get_marker_data>]

Returns the marker data for this marker. This can return a [String<class_String>] or [PackedByteArray<class_PackedByteArray>]. Only applicable to QR Code based markers.


----



|void| **set_marker_data**\ (\ marker_data\: [Variant<class_Variant>]\ ) [🔗<class_OpenXRMarkerTracker_method_set_marker_data>]

Sets the marker data for this marker.

\ **Note:** This should only be set by marker discovery logic.

