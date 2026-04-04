:github_url: hide

> **META**
	:keywords: batch



# MultiMesh

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Provides high-performance drawing of a mesh multiple times using GPU instancing.


## Description

MultiMesh provides low-level mesh instancing. Drawing thousands of [MeshInstance3D<class_MeshInstance3D>] nodes can be slow, since each object is submitted to the GPU then drawn individually.

MultiMesh is much faster as it can draw thousands of instances with a single draw call, resulting in less API overhead.

As a drawback, if the instances are too far away from each other, performance may be reduced as every single instance will always render (they are spatially indexed as one, for the whole object).

Since instances may have any behavior, the AABB used for visibility must be provided by the user.

\ **Note:** A MultiMesh is a single object, therefore the same maximum lights per object restriction applies. This means, that once the maximum lights are consumed by one or more instances, the rest of the MultiMesh instances will **not** receive any lighting.

\ **Note:** Blend Shapes will be ignored if used in a MultiMesh.


## Tutorials

- [../tutorials/3d/using_multi_mesh_instance](Using MultiMeshInstance .md)

- [../tutorials/performance/using_multimesh](Optimization using MultiMeshes .md)

- [../tutorials/performance/vertex_animation/animating_thousands_of_fish](Animating thousands of fish with MultiMeshInstance .md)


## Properties

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+----------------------------+
> | :ref:`PackedFloat32Array<class_PackedFloat32Array>`                            | :ref:`buffer<class_MultiMesh_property_buffer>`                                               | ``PackedFloat32Array()``   |
> +--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+----------------------------+
> | :ref:`PackedColorArray<class_PackedColorArray>`                                | :ref:`color_array<class_MultiMesh_property_color_array>`                                     |                            |
> +--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+----------------------------+
> | :ref:`AABB<class_AABB>`                                                        | :ref:`custom_aabb<class_MultiMesh_property_custom_aabb>`                                     | ``AABB(0, 0, 0, 0, 0, 0)`` |
> +--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+----------------------------+
> | :ref:`PackedColorArray<class_PackedColorArray>`                                | :ref:`custom_data_array<class_MultiMesh_property_custom_data_array>`                         |                            |
> +--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+----------------------------+
> | :ref:`int<class_int>`                                                          | :ref:`instance_count<class_MultiMesh_property_instance_count>`                               | ``0``                      |
> +--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+----------------------------+
> | :ref:`Mesh<class_Mesh>`                                                        | :ref:`mesh<class_MultiMesh_property_mesh>`                                                   |                            |
> +--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+----------------------------+
> | :ref:`PhysicsInterpolationQuality<enum_MultiMesh_PhysicsInterpolationQuality>` | :ref:`physics_interpolation_quality<class_MultiMesh_property_physics_interpolation_quality>` | ``0``                      |
> +--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+----------------------------+
> | :ref:`PackedVector2Array<class_PackedVector2Array>`                            | :ref:`transform_2d_array<class_MultiMesh_property_transform_2d_array>`                       |                            |
> +--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+----------------------------+
> | :ref:`PackedVector3Array<class_PackedVector3Array>`                            | :ref:`transform_array<class_MultiMesh_property_transform_array>`                             |                            |
> +--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+----------------------------+
> | :ref:`TransformFormat<enum_MultiMesh_TransformFormat>`                         | :ref:`transform_format<class_MultiMesh_property_transform_format>`                           | ``0``                      |
> +--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+----------------------------+
> | :ref:`bool<class_bool>`                                                        | :ref:`use_colors<class_MultiMesh_property_use_colors>`                                       | ``false``                  |
> +--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+----------------------------+
> | :ref:`bool<class_bool>`                                                        | :ref:`use_custom_data<class_MultiMesh_property_use_custom_data>`                             | ``false``                  |
> +--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+----------------------------+
> | :ref:`int<class_int>`                                                          | :ref:`visible_instance_count<class_MultiMesh_property_visible_instance_count>`               | ``-1``                     |
> +--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+----------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AABB<class_AABB>`               | :ref:`get_aabb<class_MultiMesh_method_get_aabb>`\ (\ ) |const|                                                                                                                                                             |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Color<class_Color>`             | :ref:`get_instance_color<class_MultiMesh_method_get_instance_color>`\ (\ instance\: :ref:`int<class_int>`\ ) |const|                                                                                                       |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Color<class_Color>`             | :ref:`get_instance_custom_data<class_MultiMesh_method_get_instance_custom_data>`\ (\ instance\: :ref:`int<class_int>`\ ) |const|                                                                                           |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>` | :ref:`get_instance_transform<class_MultiMesh_method_get_instance_transform>`\ (\ instance\: :ref:`int<class_int>`\ ) |const|                                                                                               |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform2D<class_Transform2D>` | :ref:`get_instance_transform_2d<class_MultiMesh_method_get_instance_transform_2d>`\ (\ instance\: :ref:`int<class_int>`\ ) |const|                                                                                         |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`reset_instance_physics_interpolation<class_MultiMesh_method_reset_instance_physics_interpolation>`\ (\ instance\: :ref:`int<class_int>`\ )                                                                           |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`reset_instances_physics_interpolation<class_MultiMesh_method_reset_instances_physics_interpolation>`\ (\ )                                                                                                           |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`set_buffer_interpolated<class_MultiMesh_method_set_buffer_interpolated>`\ (\ buffer_curr\: :ref:`PackedFloat32Array<class_PackedFloat32Array>`, buffer_prev\: :ref:`PackedFloat32Array<class_PackedFloat32Array>`\ ) |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`set_instance_color<class_MultiMesh_method_set_instance_color>`\ (\ instance\: :ref:`int<class_int>`, color\: :ref:`Color<class_Color>`\ )                                                                            |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`set_instance_custom_data<class_MultiMesh_method_set_instance_custom_data>`\ (\ instance\: :ref:`int<class_int>`, custom_data\: :ref:`Color<class_Color>`\ )                                                          |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`set_instance_transform<class_MultiMesh_method_set_instance_transform>`\ (\ instance\: :ref:`int<class_int>`, transform\: :ref:`Transform3D<class_Transform3D>`\ )                                                    |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`set_instance_transform_2d<class_MultiMesh_method_set_instance_transform_2d>`\ (\ instance\: :ref:`int<class_int>`, transform\: :ref:`Transform2D<class_Transform2D>`\ )                                              |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **TransformFormat**: [🔗<enum_MultiMesh_TransformFormat>]



[TransformFormat<enum_MultiMesh_TransformFormat>] **TRANSFORM_2D** = `0`

Use this when using 2D transforms.



[TransformFormat<enum_MultiMesh_TransformFormat>] **TRANSFORM_3D** = `1`

Use this when using 3D transforms.


----



enum **PhysicsInterpolationQuality**: [🔗<enum_MultiMesh_PhysicsInterpolationQuality>]



[PhysicsInterpolationQuality<enum_MultiMesh_PhysicsInterpolationQuality>] **INTERP_QUALITY_FAST** = `0`

Always interpolate using Basis lerping, which can produce warping artifacts in some situations.



[PhysicsInterpolationQuality<enum_MultiMesh_PhysicsInterpolationQuality>] **INTERP_QUALITY_HIGH** = `1`

Attempt to interpolate using Basis slerping (spherical linear interpolation) where possible, otherwise fall back to lerping.


----


## Property Descriptions



[PackedFloat32Array<class_PackedFloat32Array>] **buffer** = `PackedFloat32Array()` [🔗<class_MultiMesh_property_buffer>]


- |void| **set_buffer**\ (\ value\: [PackedFloat32Array<class_PackedFloat32Array>]\ )
- [PackedFloat32Array<class_PackedFloat32Array>] **get_buffer**\ (\ )

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedFloat32Array<class_PackedFloat32Array>] for more details.


----



[PackedColorArray<class_PackedColorArray>] **color_array** [🔗<class_MultiMesh_property_color_array>]

**Deprecated:** Accessing this property is very slow. Use [set_instance_color()<class_MultiMesh_method_set_instance_color>] and [get_instance_color()<class_MultiMesh_method_get_instance_color>] instead.

Array containing each [Color<class_Color>] used by all instances of this mesh.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedColorArray<class_PackedColorArray>] for more details.


----



[AABB<class_AABB>] **custom_aabb** = `AABB(0, 0, 0, 0, 0, 0)` [🔗<class_MultiMesh_property_custom_aabb>]


- |void| **set_custom_aabb**\ (\ value\: [AABB<class_AABB>]\ )
- [AABB<class_AABB>] **get_custom_aabb**\ (\ )

Custom AABB for this MultiMesh resource. Setting this manually prevents costly runtime AABB recalculations.


----



[PackedColorArray<class_PackedColorArray>] **custom_data_array** [🔗<class_MultiMesh_property_custom_data_array>]

**Deprecated:** Accessing this property is very slow. Use [set_instance_custom_data()<class_MultiMesh_method_set_instance_custom_data>] and [get_instance_custom_data()<class_MultiMesh_method_get_instance_custom_data>] instead.

Array containing each custom data value used by all instances of this mesh, as a [PackedColorArray<class_PackedColorArray>].

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedColorArray<class_PackedColorArray>] for more details.


----



[int<class_int>] **instance_count** = `0` [🔗<class_MultiMesh_property_instance_count>]


- |void| **set_instance_count**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_instance_count**\ (\ )

Number of instances that will get drawn. This clears and (re)sizes the buffers. Setting data format or flags afterwards will have no effect.

By default, all instances are drawn but you can limit this with [visible_instance_count<class_MultiMesh_property_visible_instance_count>].


----



[Mesh<class_Mesh>] **mesh** [🔗<class_MultiMesh_property_mesh>]


- |void| **set_mesh**\ (\ value\: [Mesh<class_Mesh>]\ )
- [Mesh<class_Mesh>] **get_mesh**\ (\ )

[Mesh<class_Mesh>] resource to be instanced.

The looks of the individual instances can be modified using [set_instance_color()<class_MultiMesh_method_set_instance_color>] and [set_instance_custom_data()<class_MultiMesh_method_set_instance_custom_data>].


----



[PhysicsInterpolationQuality<enum_MultiMesh_PhysicsInterpolationQuality>] **physics_interpolation_quality** = `0` [🔗<class_MultiMesh_property_physics_interpolation_quality>]


- |void| **set_physics_interpolation_quality**\ (\ value\: [PhysicsInterpolationQuality<enum_MultiMesh_PhysicsInterpolationQuality>]\ )
- [PhysicsInterpolationQuality<enum_MultiMesh_PhysicsInterpolationQuality>] **get_physics_interpolation_quality**\ (\ )

Choose whether to use an interpolation method that favors speed or quality.

When using low physics tick rates (typically below 20) or high rates of object rotation, you may get better results from the high quality setting.

\ **Note:** Fast quality does not equate to low quality. Except in the special cases mentioned above, the quality should be comparable to high quality.


----



[PackedVector2Array<class_PackedVector2Array>] **transform_2d_array** [🔗<class_MultiMesh_property_transform_2d_array>]

**Deprecated:** Accessing this property is very slow. Use [set_instance_transform_2d()<class_MultiMesh_method_set_instance_transform_2d>] and [get_instance_transform_2d()<class_MultiMesh_method_get_instance_transform_2d>] instead.

Array containing each [Transform2D<class_Transform2D>] value used by all instances of this mesh, as a [PackedVector2Array<class_PackedVector2Array>]. Each transform is divided into 3 [Vector2<class_Vector2>] values corresponding to the transforms' `x`, `y`, and `origin`.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array<class_PackedVector2Array>] for more details.


----



[PackedVector3Array<class_PackedVector3Array>] **transform_array** [🔗<class_MultiMesh_property_transform_array>]

**Deprecated:** Accessing this property is very slow. Use [set_instance_transform()<class_MultiMesh_method_set_instance_transform>] and [get_instance_transform()<class_MultiMesh_method_get_instance_transform>] instead.

Array containing each [Transform3D<class_Transform3D>] value used by all instances of this mesh, as a [PackedVector3Array<class_PackedVector3Array>]. Each transform is divided into 4 [Vector3<class_Vector3>] values corresponding to the transforms' `x`, `y`, `z`, and `origin`.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector3Array<class_PackedVector3Array>] for more details.


----



[TransformFormat<enum_MultiMesh_TransformFormat>] **transform_format** = `0` [🔗<class_MultiMesh_property_transform_format>]


- |void| **set_transform_format**\ (\ value\: [TransformFormat<enum_MultiMesh_TransformFormat>]\ )
- [TransformFormat<enum_MultiMesh_TransformFormat>] **get_transform_format**\ (\ )

Format of transform used to transform mesh, either 2D or 3D.


----



[bool<class_bool>] **use_colors** = `false` [🔗<class_MultiMesh_property_use_colors>]


- |void| **set_use_colors**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_using_colors**\ (\ )

If `true`, the **MultiMesh** will use color data (see [set_instance_color()<class_MultiMesh_method_set_instance_color>]). Can only be set when [instance_count<class_MultiMesh_property_instance_count>] is `0` or less. This means that you need to call this method before setting the instance count, or temporarily reset it to `0`.


----



[bool<class_bool>] **use_custom_data** = `false` [🔗<class_MultiMesh_property_use_custom_data>]


- |void| **set_use_custom_data**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_using_custom_data**\ (\ )

If `true`, the **MultiMesh** will use custom data (see [set_instance_custom_data()<class_MultiMesh_method_set_instance_custom_data>]). Can only be set when [instance_count<class_MultiMesh_property_instance_count>] is `0` or less. This means that you need to call this method before setting the instance count, or temporarily reset it to `0`.


----



[int<class_int>] **visible_instance_count** = `-1` [🔗<class_MultiMesh_property_visible_instance_count>]


- |void| **set_visible_instance_count**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_visible_instance_count**\ (\ )

Limits the number of instances drawn, -1 draws all instances. Changing this does not change the sizes of the buffers.


----


## Method Descriptions



[AABB<class_AABB>] **get_aabb**\ (\ ) |const| [🔗<class_MultiMesh_method_get_aabb>]

Returns the visibility axis-aligned bounding box in local space.


----



[Color<class_Color>] **get_instance_color**\ (\ instance\: [int<class_int>]\ ) |const| [🔗<class_MultiMesh_method_get_instance_color>]

Gets a specific instance's color multiplier.


----



[Color<class_Color>] **get_instance_custom_data**\ (\ instance\: [int<class_int>]\ ) |const| [🔗<class_MultiMesh_method_get_instance_custom_data>]

Returns the custom data that has been set for a specific instance.


----



[Transform3D<class_Transform3D>] **get_instance_transform**\ (\ instance\: [int<class_int>]\ ) |const| [🔗<class_MultiMesh_method_get_instance_transform>]

Returns the [Transform3D<class_Transform3D>] of a specific instance.


----



[Transform2D<class_Transform2D>] **get_instance_transform_2d**\ (\ instance\: [int<class_int>]\ ) |const| [🔗<class_MultiMesh_method_get_instance_transform_2d>]

Returns the [Transform2D<class_Transform2D>] of a specific instance.


----



|void| **reset_instance_physics_interpolation**\ (\ instance\: [int<class_int>]\ ) [🔗<class_MultiMesh_method_reset_instance_physics_interpolation>]

When using *physics interpolation*, this function allows you to prevent interpolation on an instance in the current physics tick.

This allows you to move instances instantaneously, and should usually be used when initially placing an instance such as a bullet to prevent graphical glitches.


----



|void| **reset_instances_physics_interpolation**\ (\ ) [🔗<class_MultiMesh_method_reset_instances_physics_interpolation>]

When using *physics interpolation*, this function allows you to prevent interpolation for all instances in the current physics tick.

This allows you to move all instances instantaneously, and should usually be used when initially placing instances to prevent graphical glitches.


----



|void| **set_buffer_interpolated**\ (\ buffer_curr\: [PackedFloat32Array<class_PackedFloat32Array>], buffer_prev\: [PackedFloat32Array<class_PackedFloat32Array>]\ ) [🔗<class_MultiMesh_method_set_buffer_interpolated>]

An alternative to setting the [buffer<class_MultiMesh_property_buffer>] property, which can be used with *physics interpolation*. This method takes two arrays, and can set the data for the current and previous tick in one go. The renderer will automatically interpolate the data at each frame.

This is useful for situations where the order of instances may change from physics tick to tick, such as particle systems.

When the order of instances is coherent, the simpler alternative of setting [buffer<class_MultiMesh_property_buffer>] can still be used with interpolation.


----



|void| **set_instance_color**\ (\ instance\: [int<class_int>], color\: [Color<class_Color>]\ ) [🔗<class_MultiMesh_method_set_instance_color>]

Sets the color of a specific instance by *multiplying* the mesh's existing vertex colors. This allows for different color tinting per instance.

\ **Note:** Each component is stored in 32 bits in the Forward+ and Mobile rendering methods, but is packed into 16 bits in the Compatibility rendering method.

For the color to take effect, ensure that [use_colors<class_MultiMesh_property_use_colors>] is `true` on the **MultiMesh** and [BaseMaterial3D.vertex_color_use_as_albedo<class_BaseMaterial3D_property_vertex_color_use_as_albedo>] is `true` on the material. If you intend to set an absolute color instead of tinting, make sure the material's albedo color is set to pure white (`Color(1, 1, 1)`).


----



|void| **set_instance_custom_data**\ (\ instance\: [int<class_int>], custom_data\: [Color<class_Color>]\ ) [🔗<class_MultiMesh_method_set_instance_custom_data>]

Sets custom data for a specific instance. `custom_data` is a [Color<class_Color>] type only to contain 4 floating-point numbers.

\ **Note:** Each number is stored in 32 bits in the Forward+ and Mobile rendering methods, but is packed into 16 bits in the Compatibility rendering method.

For the custom data to be used, ensure that [use_custom_data<class_MultiMesh_property_use_custom_data>] is `true`.

This custom instance data has to be manually accessed in your custom shader using `INSTANCE_CUSTOM`.


----



|void| **set_instance_transform**\ (\ instance\: [int<class_int>], transform\: [Transform3D<class_Transform3D>]\ ) [🔗<class_MultiMesh_method_set_instance_transform>]

Sets the [Transform3D<class_Transform3D>] for a specific instance.


----



|void| **set_instance_transform_2d**\ (\ instance\: [int<class_int>], transform\: [Transform2D<class_Transform2D>]\ ) [🔗<class_MultiMesh_method_set_instance_transform_2d>]

Sets the [Transform2D<class_Transform2D>] for a specific instance.

