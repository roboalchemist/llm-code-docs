:github_url: hide



# VisualInstance3D

**Inherits:** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [Decal<class_Decal>], [FogVolume<class_FogVolume>], [GeometryInstance3D<class_GeometryInstance3D>], [GPUParticlesAttractor3D<class_GPUParticlesAttractor3D>], [GPUParticlesCollision3D<class_GPUParticlesCollision3D>], [Light3D<class_Light3D>], [LightmapGI<class_LightmapGI>], [OccluderInstance3D<class_OccluderInstance3D>], [OpenXRVisibilityMask<class_OpenXRVisibilityMask>], [ReflectionProbe<class_ReflectionProbe>], [RootMotionView<class_RootMotionView>], [VisibleOnScreenNotifier3D<class_VisibleOnScreenNotifier3D>], [VoxelGI<class_VoxelGI>]

Parent of all visual 3D nodes.


## Description

The **VisualInstance3D** is used to connect a resource to a visual representation. All visual 3D nodes inherit from the **VisualInstance3D**. In general, you should not access the **VisualInstance3D** properties directly as they are accessed and managed by the nodes that inherit from **VisualInstance3D**. **VisualInstance3D** is the node representation of the [RenderingServer<class_RenderingServer>] instance.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+-----------------------------------------------------------------------------------------+---------+
> | :ref:`int<class_int>`     | :ref:`layers<class_VisualInstance3D_property_layers>`                                   | ``1``   |
> +---------------------------+-----------------------------------------------------------------------------------------+---------+
> | :ref:`float<class_float>` | :ref:`sorting_offset<class_VisualInstance3D_property_sorting_offset>`                   | ``0.0`` |
> +---------------------------+-----------------------------------------------------------------------------------------+---------+
> | :ref:`bool<class_bool>`   | :ref:`sorting_use_aabb_center<class_VisualInstance3D_property_sorting_use_aabb_center>` |         |
> +---------------------------+-----------------------------------------------------------------------------------------+---------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AABB<class_AABB>` | :ref:`_get_aabb<class_VisualInstance3D_private_method__get_aabb>`\ (\ ) |virtual| |const|                                                                    |
> +-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AABB<class_AABB>` | :ref:`get_aabb<class_VisualInstance3D_method_get_aabb>`\ (\ ) |const|                                                                                        |
> +-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`   | :ref:`get_base<class_VisualInstance3D_method_get_base>`\ (\ ) |const|                                                                                        |
> +-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`   | :ref:`get_instance<class_VisualInstance3D_method_get_instance>`\ (\ ) |const|                                                                                |
> +-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`get_layer_mask_value<class_VisualInstance3D_method_get_layer_mask_value>`\ (\ layer_number\: :ref:`int<class_int>`\ ) |const|                          |
> +-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`set_base<class_VisualInstance3D_method_set_base>`\ (\ base\: :ref:`RID<class_RID>`\ )                                                                  |
> +-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`set_layer_mask_value<class_VisualInstance3D_method_set_layer_mask_value>`\ (\ layer_number\: :ref:`int<class_int>`, value\: :ref:`bool<class_bool>`\ ) |
> +-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[int<class_int>] **layers** = `1` [🔗<class_VisualInstance3D_property_layers>]


- |void| **set_layer_mask**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_layer_mask**\ (\ )

The render layer(s) this **VisualInstance3D** is drawn on.

This object will only be visible for [Camera3D<class_Camera3D>]\ s whose cull mask includes any of the render layers this **VisualInstance3D** is set to.

For [Light3D<class_Light3D>]\ s, this can be used to control which **VisualInstance3D**\ s are affected by a specific light. For [GPUParticles3D<class_GPUParticles3D>], this can be used to control which particles are effected by a specific attractor. For [Decal<class_Decal>]\ s, this can be used to control which **VisualInstance3D**\ s are affected by a specific decal.

To adjust [layers<class_VisualInstance3D_property_layers>] more easily using a script, use [get_layer_mask_value()<class_VisualInstance3D_method_get_layer_mask_value>] and [set_layer_mask_value()<class_VisualInstance3D_method_set_layer_mask_value>].

\ **Note:** [VoxelGI<class_VoxelGI>], SDFGI and [LightmapGI<class_LightmapGI>] will always take all layers into account to determine what contributes to global illumination. If this is an issue, set [GeometryInstance3D.gi_mode<class_GeometryInstance3D_property_gi_mode>] to [GeometryInstance3D.GI_MODE_DISABLED<class_GeometryInstance3D_constant_GI_MODE_DISABLED>] for meshes and [Light3D.light_bake_mode<class_Light3D_property_light_bake_mode>] to [Light3D.BAKE_DISABLED<class_Light3D_constant_BAKE_DISABLED>] for lights to exclude them from global illumination.


----



[float<class_float>] **sorting_offset** = `0.0` [🔗<class_VisualInstance3D_property_sorting_offset>]


- |void| **set_sorting_offset**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_sorting_offset**\ (\ )

The amount by which the depth of this **VisualInstance3D** will be adjusted when sorting by depth. Uses the same units as the engine (which are typically meters). Adjusting it to a higher value will make the **VisualInstance3D** reliably draw on top of other **VisualInstance3D**\ s that are otherwise positioned at the same spot. To ensure it always draws on top of other objects around it (not positioned at the same spot), set the value to be greater than the distance between this **VisualInstance3D** and the other nearby **VisualInstance3D**\ s.


----



[bool<class_bool>] **sorting_use_aabb_center** [🔗<class_VisualInstance3D_property_sorting_use_aabb_center>]


- |void| **set_sorting_use_aabb_center**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_sorting_use_aabb_center**\ (\ )

If `true`, the object is sorted based on the [AABB<class_AABB>] center. The object will be sorted based on the global position otherwise.

The [AABB<class_AABB>] center based sorting is generally more accurate for 3D models. The position based sorting instead allows to better control the drawing order when working with [GPUParticles3D<class_GPUParticles3D>] and [CPUParticles3D<class_CPUParticles3D>].


----


## Method Descriptions



[AABB<class_AABB>] **_get_aabb**\ (\ ) |virtual| |const| [🔗<class_VisualInstance3D_private_method__get_aabb>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[AABB<class_AABB>] **get_aabb**\ (\ ) |const| [🔗<class_VisualInstance3D_method_get_aabb>]

Returns the [AABB<class_AABB>] (also known as the bounding box) for this **VisualInstance3D**.


----



[RID<class_RID>] **get_base**\ (\ ) |const| [🔗<class_VisualInstance3D_method_get_base>]

Returns the RID of the resource associated with this **VisualInstance3D**. For example, if the Node is a [MeshInstance3D<class_MeshInstance3D>], this will return the RID of the associated [Mesh<class_Mesh>].


----



[RID<class_RID>] **get_instance**\ (\ ) |const| [🔗<class_VisualInstance3D_method_get_instance>]

Returns the RID of this instance. This RID is the same as the RID returned by [RenderingServer.instance_create()<class_RenderingServer_method_instance_create>]. This RID is needed if you want to call [RenderingServer<class_RenderingServer>] functions directly on this **VisualInstance3D**.


----



[bool<class_bool>] **get_layer_mask_value**\ (\ layer_number\: [int<class_int>]\ ) |const| [🔗<class_VisualInstance3D_method_get_layer_mask_value>]

Returns whether or not the specified layer of the [layers<class_VisualInstance3D_property_layers>] is enabled, given a `layer_number` between 1 and 20.


----



|void| **set_base**\ (\ base\: [RID<class_RID>]\ ) [🔗<class_VisualInstance3D_method_set_base>]

Sets the resource that is instantiated by this **VisualInstance3D**, which changes how the engine handles the **VisualInstance3D** under the hood. Equivalent to [RenderingServer.instance_set_base()<class_RenderingServer_method_instance_set_base>].


----



|void| **set_layer_mask_value**\ (\ layer_number\: [int<class_int>], value\: [bool<class_bool>]\ ) [🔗<class_VisualInstance3D_method_set_layer_mask_value>]

Based on `value`, enables or disables the specified layer in the [layers<class_VisualInstance3D_property_layers>], given a `layer_number` between 1 and 20.

