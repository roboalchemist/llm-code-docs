:github_url: hide



# OpenXRSpatialComponentPlaneSemanticLabelList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData<class_OpenXRSpatialComponentData>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Object for storing the queries plane semantic label result data.


## Description

Object for storing the queries plane semantic label result data when calling [OpenXRSpatialEntityExtension.query_snapshot()<class_OpenXRSpatialEntityExtension_method_query_snapshot>].


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PlaneSemanticLabel<enum_OpenXRSpatialComponentPlaneSemanticLabelList_PlaneSemanticLabel>` | :ref:`get_plane_semantic_label<class_OpenXRSpatialComponentPlaneSemanticLabelList_method_get_plane_semantic_label>`\ (\ index\: :ref:`int<class_int>`\ ) |const| |
> +-------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **PlaneSemanticLabel**: [🔗<enum_OpenXRSpatialComponentPlaneSemanticLabelList_PlaneSemanticLabel>]



[PlaneSemanticLabel<enum_OpenXRSpatialComponentPlaneSemanticLabelList_PlaneSemanticLabel>] **PLANE_SEMANTIC_LABEL_UNCATEGORIZED** = `1`

Uncategorized plane.



[PlaneSemanticLabel<enum_OpenXRSpatialComponentPlaneSemanticLabelList_PlaneSemanticLabel>] **PLANE_SEMANTIC_LABEL_FLOOR** = `2`

Plane represents a floor.



[PlaneSemanticLabel<enum_OpenXRSpatialComponentPlaneSemanticLabelList_PlaneSemanticLabel>] **PLANE_SEMANTIC_LABEL_WALL** = `3`

Plane represents a wall.



[PlaneSemanticLabel<enum_OpenXRSpatialComponentPlaneSemanticLabelList_PlaneSemanticLabel>] **PLANE_SEMANTIC_LABEL_CEILING** = `4`

Plane represents a ceiling.



[PlaneSemanticLabel<enum_OpenXRSpatialComponentPlaneSemanticLabelList_PlaneSemanticLabel>] **PLANE_SEMANTIC_LABEL_TABLE** = `5`

Plane represents the surface of a table.


----


## Method Descriptions



[PlaneSemanticLabel<enum_OpenXRSpatialComponentPlaneSemanticLabelList_PlaneSemanticLabel>] **get_plane_semantic_label**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_OpenXRSpatialComponentPlaneSemanticLabelList_method_get_plane_semantic_label>]

Returns the plane semantic label for the parent entity at this `index`.

