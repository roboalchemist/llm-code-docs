:github_url: hide



# CanvasItemMaterial

**Inherits:** [Material<class_Material>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A material for [CanvasItem<class_CanvasItem>]\ s.


## Description

**CanvasItemMaterial**\ s provide a means of modifying the textures associated with a CanvasItem. They specialize in describing blend and lighting behaviors for textures. Use a [ShaderMaterial<class_ShaderMaterial>] to more fully customize a material's interactions with a [CanvasItem<class_CanvasItem>].


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------+-----------+
> | :ref:`BlendMode<enum_CanvasItemMaterial_BlendMode>` | :ref:`blend_mode<class_CanvasItemMaterial_property_blend_mode>`                           | ``0``     |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------+-----------+
> | :ref:`LightMode<enum_CanvasItemMaterial_LightMode>` | :ref:`light_mode<class_CanvasItemMaterial_property_light_mode>`                           | ``0``     |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`                               | :ref:`particles_anim_h_frames<class_CanvasItemMaterial_property_particles_anim_h_frames>` |           |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                             | :ref:`particles_anim_loop<class_CanvasItemMaterial_property_particles_anim_loop>`         |           |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`                               | :ref:`particles_anim_v_frames<class_CanvasItemMaterial_property_particles_anim_v_frames>` |           |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                             | :ref:`particles_animation<class_CanvasItemMaterial_property_particles_animation>`         | ``false`` |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------+-----------+
>

----


## Enumerations



enum **BlendMode**: [🔗<enum_CanvasItemMaterial_BlendMode>]



[BlendMode<enum_CanvasItemMaterial_BlendMode>] **BLEND_MODE_MIX** = `0`

Mix blending mode. Colors are assumed to be independent of the alpha (opacity) value.



[BlendMode<enum_CanvasItemMaterial_BlendMode>] **BLEND_MODE_ADD** = `1`

Additive blending mode.



[BlendMode<enum_CanvasItemMaterial_BlendMode>] **BLEND_MODE_SUB** = `2`

Subtractive blending mode.



[BlendMode<enum_CanvasItemMaterial_BlendMode>] **BLEND_MODE_MUL** = `3`

Multiplicative blending mode.



[BlendMode<enum_CanvasItemMaterial_BlendMode>] **BLEND_MODE_PREMULT_ALPHA** = `4`

Mix blending mode. Colors are assumed to be premultiplied by the alpha (opacity) value.


----



enum **LightMode**: [🔗<enum_CanvasItemMaterial_LightMode>]



[LightMode<enum_CanvasItemMaterial_LightMode>] **LIGHT_MODE_NORMAL** = `0`

Render the material using both light and non-light sensitive material properties.



[LightMode<enum_CanvasItemMaterial_LightMode>] **LIGHT_MODE_UNSHADED** = `1`

Render the material as if there were no light.



[LightMode<enum_CanvasItemMaterial_LightMode>] **LIGHT_MODE_LIGHT_ONLY** = `2`

Render the material as if there were only light.


----


## Property Descriptions



[BlendMode<enum_CanvasItemMaterial_BlendMode>] **blend_mode** = `0` [🔗<class_CanvasItemMaterial_property_blend_mode>]


- |void| **set_blend_mode**\ (\ value\: [BlendMode<enum_CanvasItemMaterial_BlendMode>]\ )
- [BlendMode<enum_CanvasItemMaterial_BlendMode>] **get_blend_mode**\ (\ )

The manner in which a material's rendering is applied to underlying textures.


----



[LightMode<enum_CanvasItemMaterial_LightMode>] **light_mode** = `0` [🔗<class_CanvasItemMaterial_property_light_mode>]


- |void| **set_light_mode**\ (\ value\: [LightMode<enum_CanvasItemMaterial_LightMode>]\ )
- [LightMode<enum_CanvasItemMaterial_LightMode>] **get_light_mode**\ (\ )

The manner in which material reacts to lighting.


----



[int<class_int>] **particles_anim_h_frames** [🔗<class_CanvasItemMaterial_property_particles_anim_h_frames>]


- |void| **set_particles_anim_h_frames**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_particles_anim_h_frames**\ (\ )

The number of columns in the spritesheet assigned as [Texture2D<class_Texture2D>] for a [GPUParticles2D<class_GPUParticles2D>] or [CPUParticles2D<class_CPUParticles2D>].

\ **Note:** This property is only used and visible in the editor if [particles_animation<class_CanvasItemMaterial_property_particles_animation>] is `true`.


----



[bool<class_bool>] **particles_anim_loop** [🔗<class_CanvasItemMaterial_property_particles_anim_loop>]


- |void| **set_particles_anim_loop**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_particles_anim_loop**\ (\ )

If `true`, the particles animation will loop.

\ **Note:** This property is only used and visible in the editor if [particles_animation<class_CanvasItemMaterial_property_particles_animation>] is `true`.


----



[int<class_int>] **particles_anim_v_frames** [🔗<class_CanvasItemMaterial_property_particles_anim_v_frames>]


- |void| **set_particles_anim_v_frames**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_particles_anim_v_frames**\ (\ )

The number of rows in the spritesheet assigned as [Texture2D<class_Texture2D>] for a [GPUParticles2D<class_GPUParticles2D>] or [CPUParticles2D<class_CPUParticles2D>].

\ **Note:** This property is only used and visible in the editor if [particles_animation<class_CanvasItemMaterial_property_particles_animation>] is `true`.


----



[bool<class_bool>] **particles_animation** = `false` [🔗<class_CanvasItemMaterial_property_particles_animation>]


- |void| **set_particles_animation**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_particles_animation**\ (\ )

If `true`, enable spritesheet-based animation features when assigned to [GPUParticles2D<class_GPUParticles2D>] and [CPUParticles2D<class_CPUParticles2D>] nodes. The [ParticleProcessMaterial.anim_speed_max<class_ParticleProcessMaterial_property_anim_speed_max>] or [CPUParticles2D.anim_speed_max<class_CPUParticles2D_property_anim_speed_max>] should also be set to a positive value for the animation to play.

This property (and other `particles_anim_*` properties that depend on it) has no effect on other types of nodes.

