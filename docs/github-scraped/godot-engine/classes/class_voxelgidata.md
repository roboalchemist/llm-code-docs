:github_url: hide



# VoxelGIData

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Contains baked voxel global illumination data for use in a [VoxelGI<class_VoxelGI>] node.


## Description

**VoxelGIData** contains baked voxel global illumination for use in a [VoxelGI<class_VoxelGI>] node. **VoxelGIData** also offers several properties to adjust the final appearance of the global illumination. These properties can be adjusted at run-time without having to bake the [VoxelGI<class_VoxelGI>] node again.

\ **Note:** To prevent text-based scene files (`.tscn`) from growing too much and becoming slow to load and save, always save **VoxelGIData** to an external binary resource file (`.res`) instead of embedding it within the scene. This can be done by clicking the dropdown arrow next to the **VoxelGIData** resource, choosing **Edit**, clicking the floppy disk icon at the top of the Inspector then choosing **Save As...**.


## Tutorials

- [Third Person Shooter (TPS) Demo ](https://godotengine.org/asset-library/asset/2710)_


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+--------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`bias<class_VoxelGIData_property_bias>`                       | ``1.5``   |
> +---------------------------+--------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`dynamic_range<class_VoxelGIData_property_dynamic_range>`     | ``2.0``   |
> +---------------------------+--------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`energy<class_VoxelGIData_property_energy>`                   | ``1.0``   |
> +---------------------------+--------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`interior<class_VoxelGIData_property_interior>`               | ``false`` |
> +---------------------------+--------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`normal_bias<class_VoxelGIData_property_normal_bias>`         | ``0.0``   |
> +---------------------------+--------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`propagation<class_VoxelGIData_property_propagation>`         | ``0.5``   |
> +---------------------------+--------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`use_two_bounces<class_VoxelGIData_property_use_two_bounces>` | ``true``  |
> +---------------------------+--------------------------------------------------------------------+-----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`allocate<class_VoxelGIData_method_allocate>`\ (\ to_cell_xform\: :ref:`Transform3D<class_Transform3D>`, aabb\: :ref:`AABB<class_AABB>`, octree_size\: :ref:`Vector3<class_Vector3>`, octree_cells\: :ref:`PackedByteArray<class_PackedByteArray>`, data_cells\: :ref:`PackedByteArray<class_PackedByteArray>`, distance_field\: :ref:`PackedByteArray<class_PackedByteArray>`, level_counts\: :ref:`PackedInt32Array<class_PackedInt32Array>`\ ) |
> +-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AABB<class_AABB>`                         | :ref:`get_bounds<class_VoxelGIData_method_get_bounds>`\ (\ ) |const|                                                                                                                                                                                                                                                                                                                                                                                   |
> +-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedByteArray<class_PackedByteArray>`   | :ref:`get_data_cells<class_VoxelGIData_method_get_data_cells>`\ (\ ) |const|                                                                                                                                                                                                                                                                                                                                                                           |
> +-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>` | :ref:`get_level_counts<class_VoxelGIData_method_get_level_counts>`\ (\ ) |const|                                                                                                                                                                                                                                                                                                                                                                       |
> +-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedByteArray<class_PackedByteArray>`   | :ref:`get_octree_cells<class_VoxelGIData_method_get_octree_cells>`\ (\ ) |const|                                                                                                                                                                                                                                                                                                                                                                       |
> +-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                   | :ref:`get_octree_size<class_VoxelGIData_method_get_octree_size>`\ (\ ) |const|                                                                                                                                                                                                                                                                                                                                                                         |
> +-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>`           | :ref:`get_to_cell_xform<class_VoxelGIData_method_get_to_cell_xform>`\ (\ ) |const|                                                                                                                                                                                                                                                                                                                                                                     |
> +-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[float<class_float>] **bias** = `1.5` [🔗<class_VoxelGIData_property_bias>]


- |void| **set_bias**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_bias**\ (\ )

The normal bias to use for indirect lighting and reflections. Higher values reduce self-reflections visible in non-rough materials, at the cost of more visible light leaking and flatter-looking indirect lighting. To prioritize hiding self-reflections over lighting quality, set [bias<class_VoxelGIData_property_bias>] to `0.0` and [normal_bias<class_VoxelGIData_property_normal_bias>] to a value between `1.0` and `2.0`.


----



[float<class_float>] **dynamic_range** = `2.0` [🔗<class_VoxelGIData_property_dynamic_range>]


- |void| **set_dynamic_range**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_dynamic_range**\ (\ )

The dynamic range to use (`1.0` represents a low dynamic range scene brightness). Higher values can be used to provide brighter indirect lighting, at the cost of more visible color banding in dark areas (both in indirect lighting and reflections). To avoid color banding, it's recommended to use the lowest value that does not result in visible light clipping.


----



[float<class_float>] **energy** = `1.0` [🔗<class_VoxelGIData_property_energy>]


- |void| **set_energy**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_energy**\ (\ )

The energy of the indirect lighting and reflections produced by the [VoxelGI<class_VoxelGI>] node. Higher values result in brighter indirect lighting. If indirect lighting looks too flat, try decreasing [propagation<class_VoxelGIData_property_propagation>] while increasing [energy<class_VoxelGIData_property_energy>] at the same time. See also [use_two_bounces<class_VoxelGIData_property_use_two_bounces>] which influences the indirect lighting's effective brightness.


----



[bool<class_bool>] **interior** = `false` [🔗<class_VoxelGIData_property_interior>]


- |void| **set_interior**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_interior**\ (\ )

If `true`, [Environment<class_Environment>] lighting is ignored by the [VoxelGI<class_VoxelGI>] node. If `false`, [Environment<class_Environment>] lighting is taken into account by the [VoxelGI<class_VoxelGI>] node. [Environment<class_Environment>] lighting updates in real-time, which means it can be changed without having to bake the [VoxelGI<class_VoxelGI>] node again.


----



[float<class_float>] **normal_bias** = `0.0` [🔗<class_VoxelGIData_property_normal_bias>]


- |void| **set_normal_bias**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_normal_bias**\ (\ )

The normal bias to use for indirect lighting and reflections. Higher values reduce self-reflections visible in non-rough materials, at the cost of more visible light leaking and flatter-looking indirect lighting. See also [bias<class_VoxelGIData_property_bias>]. To prioritize hiding self-reflections over lighting quality, set [bias<class_VoxelGIData_property_bias>] to `0.0` and [normal_bias<class_VoxelGIData_property_normal_bias>] to a value between `1.0` and `2.0`.


----



[float<class_float>] **propagation** = `0.5` [🔗<class_VoxelGIData_property_propagation>]


- |void| **set_propagation**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_propagation**\ (\ )

The multiplier to use when light bounces off a surface. Higher values result in brighter indirect lighting. If indirect lighting looks too flat, try decreasing [propagation<class_VoxelGIData_property_propagation>] while increasing [energy<class_VoxelGIData_property_energy>] at the same time. See also [use_two_bounces<class_VoxelGIData_property_use_two_bounces>] which influences the indirect lighting's effective brightness.


----



[bool<class_bool>] **use_two_bounces** = `true` [🔗<class_VoxelGIData_property_use_two_bounces>]


- |void| **set_use_two_bounces**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_using_two_bounces**\ (\ )

If `true`, performs two bounces of indirect lighting instead of one. This makes indirect lighting look more natural and brighter at a small performance cost. The second bounce is also visible in reflections. If the scene appears too bright after enabling [use_two_bounces<class_VoxelGIData_property_use_two_bounces>], adjust [propagation<class_VoxelGIData_property_propagation>] and [energy<class_VoxelGIData_property_energy>].


----


## Method Descriptions



|void| **allocate**\ (\ to_cell_xform\: [Transform3D<class_Transform3D>], aabb\: [AABB<class_AABB>], octree_size\: [Vector3<class_Vector3>], octree_cells\: [PackedByteArray<class_PackedByteArray>], data_cells\: [PackedByteArray<class_PackedByteArray>], distance_field\: [PackedByteArray<class_PackedByteArray>], level_counts\: [PackedInt32Array<class_PackedInt32Array>]\ ) [🔗<class_VoxelGIData_method_allocate>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[AABB<class_AABB>] **get_bounds**\ (\ ) |const| [🔗<class_VoxelGIData_method_get_bounds>]

Returns the bounds of the baked voxel data as an [AABB<class_AABB>], which should match [VoxelGI.size<class_VoxelGI_property_size>] after being baked (which only contains the size as a [Vector3<class_Vector3>]).

\ **Note:** If the size was modified without baking the VoxelGI data, then the value of [get_bounds()<class_VoxelGIData_method_get_bounds>] and [VoxelGI.size<class_VoxelGI_property_size>] will not match.


----



[PackedByteArray<class_PackedByteArray>] **get_data_cells**\ (\ ) |const| [🔗<class_VoxelGIData_method_get_data_cells>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[PackedInt32Array<class_PackedInt32Array>] **get_level_counts**\ (\ ) |const| [🔗<class_VoxelGIData_method_get_level_counts>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[PackedByteArray<class_PackedByteArray>] **get_octree_cells**\ (\ ) |const| [🔗<class_VoxelGIData_method_get_octree_cells>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Vector3<class_Vector3>] **get_octree_size**\ (\ ) |const| [🔗<class_VoxelGIData_method_get_octree_size>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Transform3D<class_Transform3D>] **get_to_cell_xform**\ (\ ) |const| [🔗<class_VoxelGIData_method_get_to_cell_xform>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!

