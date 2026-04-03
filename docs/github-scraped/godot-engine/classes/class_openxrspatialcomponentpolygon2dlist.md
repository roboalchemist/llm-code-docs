:github_url: hide



# OpenXRSpatialComponentPolygon2DList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData<class_OpenXRSpatialComponentData>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Object for storing the queries polygon2d result data.


## Description

Object for storing the queries 2D polygon result data when calling [OpenXRSpatialEntityExtension.query_snapshot()<class_OpenXRSpatialEntityExtension_method_query_snapshot>].


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>`               | :ref:`get_transform<class_OpenXRSpatialComponentPolygon2DList_method_get_transform>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                 |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedVector2Array<class_PackedVector2Array>` | :ref:`get_vertices<class_OpenXRSpatialComponentPolygon2DList_method_get_vertices>`\ (\ snapshot\: :ref:`RID<class_RID>`, index\: :ref:`int<class_int>`\ ) |const| |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[Transform3D<class_Transform3D>] **get_transform**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_OpenXRSpatialComponentPolygon2DList_method_get_transform>]

Returns the transform for positioning our polygon for the entity at this `index`.


----



[PackedVector2Array<class_PackedVector2Array>] **get_vertices**\ (\ snapshot\: [RID<class_RID>], index\: [int<class_int>]\ ) |const| [🔗<class_OpenXRSpatialComponentPolygon2DList_method_get_vertices>]

Returns the polygon vertices for the entity at this `index`.

