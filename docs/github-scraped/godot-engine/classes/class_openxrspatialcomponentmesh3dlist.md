:github_url: hide



# OpenXRSpatialComponentMesh3DList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData<class_OpenXRSpatialComponentData>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Object for storing the queries mesh3d result data.


## Description

Object for storing the queries 3d mesh result data when calling [OpenXRSpatialEntityExtension.query_snapshot()<class_OpenXRSpatialEntityExtension_method_query_snapshot>].


## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Mesh<class_Mesh>`               | :ref:`get_mesh<class_OpenXRSpatialComponentMesh3DList_method_get_mesh>`\ (\ index\: :ref:`int<class_int>`\ ) |const|           |
> +---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>` | :ref:`get_transform<class_OpenXRSpatialComponentMesh3DList_method_get_transform>`\ (\ index\: :ref:`int<class_int>`\ ) |const| |
> +---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[Mesh<class_Mesh>] **get_mesh**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_OpenXRSpatialComponentMesh3DList_method_get_mesh>]

Returns the mesh for the entity at this `index`.


----



[Transform3D<class_Transform3D>] **get_transform**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_OpenXRSpatialComponentMesh3DList_method_get_transform>]

Returns the transform for positioning our mesh for the entity at this `index`.

