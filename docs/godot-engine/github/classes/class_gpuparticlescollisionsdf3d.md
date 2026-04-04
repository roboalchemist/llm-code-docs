:github_url: hide



# GPUParticlesCollisionSDF3D

**Inherits:** [GPUParticlesCollision3D<class_GPUParticlesCollision3D>] **<** [VisualInstance3D<class_VisualInstance3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A baked signed distance field 3D particle collision shape affecting [GPUParticles3D<class_GPUParticles3D>] nodes.


## Description

A baked signed distance field 3D particle collision shape affecting [GPUParticles3D<class_GPUParticles3D>] nodes.

Signed distance fields (SDF) allow for efficiently representing approximate collision shapes for convex and concave objects of any shape. This is more flexible than [GPUParticlesCollisionHeightField3D<class_GPUParticlesCollisionHeightField3D>], but it requires a baking step.

\ **Baking:** The signed distance field texture can be baked by selecting the **GPUParticlesCollisionSDF3D** node in the editor, then clicking **Bake SDF** at the top of the 3D viewport. Any *visible* [MeshInstance3D<class_MeshInstance3D>]\ s within the [size<class_GPUParticlesCollisionSDF3D_property_size>] will be taken into account for baking, regardless of their [GeometryInstance3D.gi_mode<class_GeometryInstance3D_property_gi_mode>].

\ **Note:** Baking a **GPUParticlesCollisionSDF3D**'s [texture<class_GPUParticlesCollisionSDF3D_property_texture>] is only possible within the editor, as there is no bake method exposed for use in exported projects. However, it's still possible to load pre-baked [Texture3D<class_Texture3D>]\ s into its [texture<class_GPUParticlesCollisionSDF3D_property_texture>] property in an exported project.

\ **Note:** [ParticleProcessMaterial.collision_mode<class_ParticleProcessMaterial_property_collision_mode>] must be [ParticleProcessMaterial.COLLISION_RIGID<class_ParticleProcessMaterial_constant_COLLISION_RIGID>] or [ParticleProcessMaterial.COLLISION_HIDE_ON_CONTACT<class_ParticleProcessMaterial_constant_COLLISION_HIDE_ON_CONTACT>] on the [GPUParticles3D<class_GPUParticles3D>]'s process material for collision to work.

\ **Note:** Particle collision only affects [GPUParticles3D<class_GPUParticles3D>], not [CPUParticles3D<class_CPUParticles3D>].


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------------------+-------------------------------------------------------------------------+----------------------+
> | :ref:`int<class_int>`                                         | :ref:`bake_mask<class_GPUParticlesCollisionSDF3D_property_bake_mask>`   | ``4294967295``       |
> +---------------------------------------------------------------+-------------------------------------------------------------------------+----------------------+
> | :ref:`Resolution<enum_GPUParticlesCollisionSDF3D_Resolution>` | :ref:`resolution<class_GPUParticlesCollisionSDF3D_property_resolution>` | ``2``                |
> +---------------------------------------------------------------+-------------------------------------------------------------------------+----------------------+
> | :ref:`Vector3<class_Vector3>`                                 | :ref:`size<class_GPUParticlesCollisionSDF3D_property_size>`             | ``Vector3(2, 2, 2)`` |
> +---------------------------------------------------------------+-------------------------------------------------------------------------+----------------------+
> | :ref:`Texture3D<class_Texture3D>`                             | :ref:`texture<class_GPUParticlesCollisionSDF3D_property_texture>`       |                      |
> +---------------------------------------------------------------+-------------------------------------------------------------------------+----------------------+
> | :ref:`float<class_float>`                                     | :ref:`thickness<class_GPUParticlesCollisionSDF3D_property_thickness>`   | ``1.0``              |
> +---------------------------------------------------------------+-------------------------------------------------------------------------+----------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`get_bake_mask_value<class_GPUParticlesCollisionSDF3D_method_get_bake_mask_value>`\ (\ layer_number\: :ref:`int<class_int>`\ ) |const|                          |
> +-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`set_bake_mask_value<class_GPUParticlesCollisionSDF3D_method_set_bake_mask_value>`\ (\ layer_number\: :ref:`int<class_int>`, value\: :ref:`bool<class_bool>`\ ) |
> +-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **Resolution**: [🔗<enum_GPUParticlesCollisionSDF3D_Resolution>]



[Resolution<enum_GPUParticlesCollisionSDF3D_Resolution>] **RESOLUTION_16** = `0`

Bake a 16×16×16 signed distance field. This is the fastest option, but also the least precise.



[Resolution<enum_GPUParticlesCollisionSDF3D_Resolution>] **RESOLUTION_32** = `1`

Bake a 32×32×32 signed distance field.



[Resolution<enum_GPUParticlesCollisionSDF3D_Resolution>] **RESOLUTION_64** = `2`

Bake a 64×64×64 signed distance field.



[Resolution<enum_GPUParticlesCollisionSDF3D_Resolution>] **RESOLUTION_128** = `3`

Bake a 128×128×128 signed distance field.



[Resolution<enum_GPUParticlesCollisionSDF3D_Resolution>] **RESOLUTION_256** = `4`

Bake a 256×256×256 signed distance field.



[Resolution<enum_GPUParticlesCollisionSDF3D_Resolution>] **RESOLUTION_512** = `5`

Bake a 512×512×512 signed distance field. This is the slowest option, but also the most precise.



[Resolution<enum_GPUParticlesCollisionSDF3D_Resolution>] **RESOLUTION_MAX** = `6`

Represents the size of the [Resolution<enum_GPUParticlesCollisionSDF3D_Resolution>] enum.


----


## Property Descriptions



[int<class_int>] **bake_mask** = `4294967295` [🔗<class_GPUParticlesCollisionSDF3D_property_bake_mask>]


- |void| **set_bake_mask**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_bake_mask**\ (\ )

The visual layers to account for when baking the particle collision SDF. Only [MeshInstance3D<class_MeshInstance3D>]\ s whose [VisualInstance3D.layers<class_VisualInstance3D_property_layers>] match with this [bake_mask<class_GPUParticlesCollisionSDF3D_property_bake_mask>] will be included in the generated particle collision SDF. By default, all objects are taken into account for the particle collision SDF baking.


----



[Resolution<enum_GPUParticlesCollisionSDF3D_Resolution>] **resolution** = `2` [🔗<class_GPUParticlesCollisionSDF3D_property_resolution>]


- |void| **set_resolution**\ (\ value\: [Resolution<enum_GPUParticlesCollisionSDF3D_Resolution>]\ )
- [Resolution<enum_GPUParticlesCollisionSDF3D_Resolution>] **get_resolution**\ (\ )

The bake resolution to use for the signed distance field [texture<class_GPUParticlesCollisionSDF3D_property_texture>]. The texture must be baked again for changes to the [resolution<class_GPUParticlesCollisionSDF3D_property_resolution>] property to be effective. Higher resolutions have a greater performance cost and take more time to bake. Higher resolutions also result in larger baked textures, leading to increased VRAM and storage space requirements. To improve performance and reduce bake times, use the lowest resolution possible for the object you're representing the collision of.


----



[Vector3<class_Vector3>] **size** = `Vector3(2, 2, 2)` [🔗<class_GPUParticlesCollisionSDF3D_property_size>]


- |void| **set_size**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_size**\ (\ )

The collision SDF's size in 3D units. To improve SDF quality, the [size<class_GPUParticlesCollisionSDF3D_property_size>] should be set as small as possible while covering the parts of the scene you need.


----



[Texture3D<class_Texture3D>] **texture** [🔗<class_GPUParticlesCollisionSDF3D_property_texture>]


- |void| **set_texture**\ (\ value\: [Texture3D<class_Texture3D>]\ )
- [Texture3D<class_Texture3D>] **get_texture**\ (\ )

The 3D texture representing the signed distance field.


----



[float<class_float>] **thickness** = `1.0` [🔗<class_GPUParticlesCollisionSDF3D_property_thickness>]


- |void| **set_thickness**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_thickness**\ (\ )

The collision shape's thickness. Unlike other particle colliders, **GPUParticlesCollisionSDF3D** is actually hollow on the inside. [thickness<class_GPUParticlesCollisionSDF3D_property_thickness>] can be increased to prevent particles from tunneling through the collision shape at high speeds, or when the **GPUParticlesCollisionSDF3D** is moved.


----


## Method Descriptions



[bool<class_bool>] **get_bake_mask_value**\ (\ layer_number\: [int<class_int>]\ ) |const| [🔗<class_GPUParticlesCollisionSDF3D_method_get_bake_mask_value>]

Returns whether or not the specified layer of the [bake_mask<class_GPUParticlesCollisionSDF3D_property_bake_mask>] is enabled, given a `layer_number` between 1 and 32.


----



|void| **set_bake_mask_value**\ (\ layer_number\: [int<class_int>], value\: [bool<class_bool>]\ ) [🔗<class_GPUParticlesCollisionSDF3D_method_set_bake_mask_value>]

Based on `value`, enables or disables the specified layer in the [bake_mask<class_GPUParticlesCollisionSDF3D_property_bake_mask>], given a `layer_number` between 1 and 32.

