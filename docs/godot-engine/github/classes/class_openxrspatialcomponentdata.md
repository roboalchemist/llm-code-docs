:github_url: hide



# OpenXRSpatialComponentData

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [OpenXRSpatialComponentAnchorList<class_OpenXRSpatialComponentAnchorList>], [OpenXRSpatialComponentBounded2DList<class_OpenXRSpatialComponentBounded2DList>], [OpenXRSpatialComponentBounded3DList<class_OpenXRSpatialComponentBounded3DList>], [OpenXRSpatialComponentMarkerList<class_OpenXRSpatialComponentMarkerList>], [OpenXRSpatialComponentMesh2DList<class_OpenXRSpatialComponentMesh2DList>], [OpenXRSpatialComponentMesh3DList<class_OpenXRSpatialComponentMesh3DList>], [OpenXRSpatialComponentParentList<class_OpenXRSpatialComponentParentList>], [OpenXRSpatialComponentPersistenceList<class_OpenXRSpatialComponentPersistenceList>], [OpenXRSpatialComponentPlaneAlignmentList<class_OpenXRSpatialComponentPlaneAlignmentList>], [OpenXRSpatialComponentPlaneSemanticLabelList<class_OpenXRSpatialComponentPlaneSemanticLabelList>], [OpenXRSpatialComponentPolygon2DList<class_OpenXRSpatialComponentPolygon2DList>], [OpenXRSpatialQueryResultData<class_OpenXRSpatialQueryResultData>]

Object for storing OpenXR spatial entity component data.


## Description

Object for storing OpenXR spatial entity component data.


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>` | :ref:`_get_component_type<class_OpenXRSpatialComponentData_private_method__get_component_type>`\ (\ ) |virtual| |const|                               |
> +-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>` | :ref:`_get_structure_data<class_OpenXRSpatialComponentData_private_method__get_structure_data>`\ (\ next\: :ref:`int<class_int>`\ ) |virtual| |const| |
> +-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                | :ref:`_set_capacity<class_OpenXRSpatialComponentData_private_method__set_capacity>`\ (\ capacity\: :ref:`int<class_int>`\ ) |virtual|                 |
> +-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                | :ref:`set_capacity<class_OpenXRSpatialComponentData_method_set_capacity>`\ (\ capacity\: :ref:`int<class_int>`\ )                                     |
> +-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[int<class_int>] **_get_component_type**\ (\ ) |virtual| |const| [🔗<class_OpenXRSpatialComponentData_private_method__get_component_type>]

Return the component type for the component we store data for.


----



[int<class_int>] **_get_structure_data**\ (\ next\: [int<class_int>]\ ) |virtual| |const| [🔗<class_OpenXRSpatialComponentData_private_method__get_structure_data>]

Return a pointer to the structure data that will be submitted along with the snapshot query. This pointer must remain valid as long as this object is instantiated.


----



|void| **_set_capacity**\ (\ capacity\: [int<class_int>]\ ) |virtual| [🔗<class_OpenXRSpatialComponentData_private_method__set_capacity>]

Set the expected capacity as provided by the spatial entities query system. Buffers should be initialized with the correct storage.


----



|void| **set_capacity**\ (\ capacity\: [int<class_int>]\ ) [🔗<class_OpenXRSpatialComponentData_method_set_capacity>]

Set the expected capacity as provided by the spatial entities query system. Buffers should be initialized with the correct storage.

