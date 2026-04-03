:github_url: hide



# Occluder3D

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [ArrayOccluder3D<class_ArrayOccluder3D>], [BoxOccluder3D<class_BoxOccluder3D>], [PolygonOccluder3D<class_PolygonOccluder3D>], [QuadOccluder3D<class_QuadOccluder3D>], [SphereOccluder3D<class_SphereOccluder3D>]

Occluder shape resource for use with occlusion culling in [OccluderInstance3D<class_OccluderInstance3D>].


## Description

**Occluder3D** stores an occluder shape that can be used by the engine's occlusion culling system.

See [OccluderInstance3D<class_OccluderInstance3D>]'s documentation for instructions on setting up occlusion culling.


## Tutorials

- [../tutorials/3d/occlusion_culling](Occlusion culling .md)


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+-------------------------------------------------------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>`     | :ref:`get_indices<class_Occluder3D_method_get_indices>`\ (\ ) |const|   |
> +-----------------------------------------------------+-------------------------------------------------------------------------+
> | :ref:`PackedVector3Array<class_PackedVector3Array>` | :ref:`get_vertices<class_Occluder3D_method_get_vertices>`\ (\ ) |const| |
> +-----------------------------------------------------+-------------------------------------------------------------------------+
>

----


## Method Descriptions



[PackedInt32Array<class_PackedInt32Array>] **get_indices**\ (\ ) |const| [🔗<class_Occluder3D_method_get_indices>]

Returns the occluder shape's vertex indices.


----



[PackedVector3Array<class_PackedVector3Array>] **get_vertices**\ (\ ) |const| [🔗<class_Occluder3D_method_get_vertices>]

Returns the occluder shape's vertex positions.

