:github_url: hide



# OpenXRSpatialComponentPlaneAlignmentList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData<class_OpenXRSpatialComponentData>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Object for storing the queries plane alignment result data.


## Description

Object for storing the queries plane alignment result data when calling [OpenXRSpatialEntityExtension.query_snapshot()<class_OpenXRSpatialEntityExtension_method_query_snapshot>].


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PlaneAlignment<enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment>` | :ref:`get_plane_alignment<class_OpenXRSpatialComponentPlaneAlignmentList_method_get_plane_alignment>`\ (\ index\: :ref:`int<class_int>`\ ) |const| |
> +-------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **PlaneAlignment**: [🔗<enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment>]



[PlaneAlignment<enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment>] **PLANE_ALIGNMENT_HORIZONTAL_UPWARD** = `0`

Plane is facing upward.



[PlaneAlignment<enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment>] **PLANE_ALIGNMENT_HORIZONTAL_DOWNWARD** = `1`

Plane is facing downwards.



[PlaneAlignment<enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment>] **PLANE_ALIGNMENT_VERTICAL** = `2`

Plane is vertically aligned.



[PlaneAlignment<enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment>] **PLANE_ALIGNMENT_ARBITRARY** = `3`

Plane has an arbitrary alignment.


----


## Method Descriptions



[PlaneAlignment<enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment>] **get_plane_alignment**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_OpenXRSpatialComponentPlaneAlignmentList_method_get_plane_alignment>]

Returns the plane alignment for the parent entity at this `index`.

