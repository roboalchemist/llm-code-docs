:github_url: hide



# ArrayOccluder3D

**Inherits:** [Occluder3D<class_Occluder3D>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

3D polygon shape for use with occlusion culling in [OccluderInstance3D<class_OccluderInstance3D>].


## Description

**ArrayOccluder3D** stores an arbitrary 3D polygon shape that can be used by the engine's occlusion culling system. This is analogous to [ArrayMesh<class_ArrayMesh>], but for occluders.

See [OccluderInstance3D<class_OccluderInstance3D>]'s documentation for instructions on setting up occlusion culling.


## Tutorials

- [../tutorials/3d/occlusion_culling](Occlusion culling .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+----------------------------------------------------------+--------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>`     | :ref:`indices<class_ArrayOccluder3D_property_indices>`   | ``PackedInt32Array()``   |
> +-----------------------------------------------------+----------------------------------------------------------+--------------------------+
> | :ref:`PackedVector3Array<class_PackedVector3Array>` | :ref:`vertices<class_ArrayOccluder3D_property_vertices>` | ``PackedVector3Array()`` |
> +-----------------------------------------------------+----------------------------------------------------------+--------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`set_arrays<class_ArrayOccluder3D_method_set_arrays>`\ (\ vertices\: :ref:`PackedVector3Array<class_PackedVector3Array>`, indices\: :ref:`PackedInt32Array<class_PackedInt32Array>`\ ) |
> +--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[PackedInt32Array<class_PackedInt32Array>] **indices** = `PackedInt32Array()` [🔗<class_ArrayOccluder3D_property_indices>]


- |void| **set_indices**\ (\ value\: [PackedInt32Array<class_PackedInt32Array>]\ )
- [PackedInt32Array<class_PackedInt32Array>] **get_indices**\ (\ )

The occluder's index position. Indices determine which points from the [vertices<class_ArrayOccluder3D_property_vertices>] array should be drawn, and in which order.

\ **Note:** The occluder is always updated after setting this value. If creating occluders procedurally, consider using [set_arrays()<class_ArrayOccluder3D_method_set_arrays>] instead to avoid updating the occluder twice when it's created.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array<class_PackedInt32Array>] for more details.


----



[PackedVector3Array<class_PackedVector3Array>] **vertices** = `PackedVector3Array()` [🔗<class_ArrayOccluder3D_property_vertices>]


- |void| **set_vertices**\ (\ value\: [PackedVector3Array<class_PackedVector3Array>]\ )
- [PackedVector3Array<class_PackedVector3Array>] **get_vertices**\ (\ )

The occluder's vertex positions in local 3D coordinates.

\ **Note:** The occluder is always updated after setting this value. If creating occluders procedurally, consider using [set_arrays()<class_ArrayOccluder3D_method_set_arrays>] instead to avoid updating the occluder twice when it's created.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector3Array<class_PackedVector3Array>] for more details.


----


## Method Descriptions



|void| **set_arrays**\ (\ vertices\: [PackedVector3Array<class_PackedVector3Array>], indices\: [PackedInt32Array<class_PackedInt32Array>]\ ) [🔗<class_ArrayOccluder3D_method_set_arrays>]

Sets [indices<class_ArrayOccluder3D_property_indices>] and [vertices<class_ArrayOccluder3D_property_vertices>], while updating the final occluder only once after both values are set.

