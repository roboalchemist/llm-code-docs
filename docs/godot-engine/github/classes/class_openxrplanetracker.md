:github_url: hide



# OpenXRPlaneTracker

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialEntityTracker<class_OpenXRSpatialEntityTracker>] **<** [XRPositionalTracker<class_XRPositionalTracker>] **<** [XRTracker<class_XRTracker>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Spatial entity tracker for our spatial entity plane tracking extension.


## Description

Spatial entity tracker for our OpenXR spatial entity plane tracking extension. These trackers identify entities in our real space such as walls, floors, tables, etc. and map their location to our virtual space.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------------------------------------+---------------------------------------------------------------------------+-------------------+
> | :ref:`Vector2<class_Vector2>`                                                       | :ref:`bounds_size<class_OpenXRPlaneTracker_property_bounds_size>`         | ``Vector2(0, 0)`` |
> +-------------------------------------------------------------------------------------+---------------------------------------------------------------------------+-------------------+
> | :ref:`PlaneAlignment<enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment>` | :ref:`plane_alignment<class_OpenXRPlaneTracker_property_plane_alignment>` | ``0``             |
> +-------------------------------------------------------------------------------------+---------------------------------------------------------------------------+-------------------+
> | :ref:`String<class_String>`                                                         | :ref:`plane_label<class_OpenXRPlaneTracker_property_plane_label>`         | ``""``            |
> +-------------------------------------------------------------------------------------+---------------------------------------------------------------------------+-------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`clear_mesh_data<class_OpenXRPlaneTracker_method_clear_mesh_data>`\ (\ )                                                                                                                                                                                             |
> +---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Mesh<class_Mesh>`               | :ref:`get_mesh<class_OpenXRPlaneTracker_method_get_mesh>`\ (\ )                                                                                                                                                                                                           |
> +---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>` | :ref:`get_mesh_offset<class_OpenXRPlaneTracker_method_get_mesh_offset>`\ (\ ) |const|                                                                                                                                                                                     |
> +---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Shape3D<class_Shape3D>`         | :ref:`get_shape<class_OpenXRPlaneTracker_method_get_shape>`\ (\ thickness\: :ref:`float<class_float>` = 0.01\ )                                                                                                                                                           |
> +---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`set_mesh_data<class_OpenXRPlaneTracker_method_set_mesh_data>`\ (\ origin\: :ref:`Transform3D<class_Transform3D>`, vertices\: :ref:`PackedVector2Array<class_PackedVector2Array>`, indices\: :ref:`PackedInt32Array<class_PackedInt32Array>` = PackedInt32Array()\ ) |
> +---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**mesh_changed**\ (\ ) [🔗<class_OpenXRPlaneTracker_signal_mesh_changed>]

Emitted when our mesh data has changed the mesh instance and collision needs to be updated.


----


## Property Descriptions



[Vector2<class_Vector2>] **bounds_size** = `Vector2(0, 0)` [🔗<class_OpenXRPlaneTracker_property_bounds_size>]


- |void| **set_bounds_size**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_bounds_size**\ (\ )

The bounding size of the plane. This is a 2D size.


----



[PlaneAlignment<enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment>] **plane_alignment** = `0` [🔗<class_OpenXRPlaneTracker_property_plane_alignment>]


- |void| **set_plane_alignment**\ (\ value\: [PlaneAlignment<enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment>]\ )
- [PlaneAlignment<enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment>] **get_plane_alignment**\ (\ )

The main alignment in space of this plane.


----



[String<class_String>] **plane_label** = `""` [🔗<class_OpenXRPlaneTracker_property_plane_label>]


- |void| **set_plane_label**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_plane_label**\ (\ )

The semantic label for this plane.


----


## Method Descriptions



|void| **clear_mesh_data**\ (\ ) [🔗<class_OpenXRPlaneTracker_method_clear_mesh_data>]

Clears the mesh data for this tracker. You should only call this if you are handling your own discovery logic.


----



[Mesh<class_Mesh>] **get_mesh**\ (\ ) [🔗<class_OpenXRPlaneTracker_method_get_mesh>]

Gets a mesh created from either the mesh data or from our bounding size for this plane.


----



[Transform3D<class_Transform3D>] **get_mesh_offset**\ (\ ) |const| [🔗<class_OpenXRPlaneTracker_method_get_mesh_offset>]

Gets the transform by which to offset the mesh and collision shape from our pose to display these correctly.


----



[Shape3D<class_Shape3D>] **get_shape**\ (\ thickness\: [float<class_float>] = 0.01\ ) [🔗<class_OpenXRPlaneTracker_method_get_shape>]

Gets a collision shape built either from the mesh data or from our bounding size for this plane.


----



|void| **set_mesh_data**\ (\ origin\: [Transform3D<class_Transform3D>], vertices\: [PackedVector2Array<class_PackedVector2Array>], indices\: [PackedInt32Array<class_PackedInt32Array>] = PackedInt32Array()\ ) [🔗<class_OpenXRPlaneTracker_method_set_mesh_data>]

Sets the mesh data for this plane. You should only call this if you are handling your own discovery logic.

