:github_url: hide



# FogMaterial

**Inherits:** [Material<class_Material>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A material that controls how volumetric fog is rendered, to be assigned to a [FogVolume<class_FogVolume>].


## Description

A [Material<class_Material>] resource that can be used by [FogVolume<class_FogVolume>]\ s to draw volumetric effects.

If you need more advanced effects, use a custom [../tutorials/shaders/shader_reference/fog_shader](fog shader .md).


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------+--------------------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>`         | :ref:`albedo<class_FogMaterial_property_albedo>`                   | ``Color(1, 1, 1, 1)`` |
> +-----------------------------------+--------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`         | :ref:`density<class_FogMaterial_property_density>`                 | ``1.0``               |
> +-----------------------------------+--------------------------------------------------------------------+-----------------------+
> | :ref:`Texture3D<class_Texture3D>` | :ref:`density_texture<class_FogMaterial_property_density_texture>` |                       |
> +-----------------------------------+--------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`         | :ref:`edge_fade<class_FogMaterial_property_edge_fade>`             | ``0.1``               |
> +-----------------------------------+--------------------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>`         | :ref:`emission<class_FogMaterial_property_emission>`               | ``Color(0, 0, 0, 1)`` |
> +-----------------------------------+--------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`         | :ref:`height_falloff<class_FogMaterial_property_height_falloff>`   | ``0.0``               |
> +-----------------------------------+--------------------------------------------------------------------+-----------------------+
>

----


## Property Descriptions



[Color<class_Color>] **albedo** = `Color(1, 1, 1, 1)` [🔗<class_FogMaterial_property_albedo>]


- |void| **set_albedo**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_albedo**\ (\ )

The single-scattering [Color<class_Color>] of the [FogVolume<class_FogVolume>]. Internally, [albedo<class_FogMaterial_property_albedo>] is converted into single-scattering, which is additively blended with other [FogVolume<class_FogVolume>]\ s and the [Environment.volumetric_fog_albedo<class_Environment_property_volumetric_fog_albedo>].


----



[float<class_float>] **density** = `1.0` [🔗<class_FogMaterial_property_density>]


- |void| **set_density**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_density**\ (\ )

The density of the [FogVolume<class_FogVolume>]. Denser objects are more opaque, but may suffer from under-sampling artifacts that look like stripes. Negative values can be used to subtract fog from other [FogVolume<class_FogVolume>]\ s or global volumetric fog.

\ **Note:** Due to limited precision, [density<class_FogMaterial_property_density>] values between `-0.001` and `0.001` (exclusive) act like `0.0`. This does not apply to [Environment.volumetric_fog_density<class_Environment_property_volumetric_fog_density>].


----



[Texture3D<class_Texture3D>] **density_texture** [🔗<class_FogMaterial_property_density_texture>]


- |void| **set_density_texture**\ (\ value\: [Texture3D<class_Texture3D>]\ )
- [Texture3D<class_Texture3D>] **get_density_texture**\ (\ )

The 3D texture that is used to scale the [density<class_FogMaterial_property_density>] of the [FogVolume<class_FogVolume>]. This can be used to vary fog density within the [FogVolume<class_FogVolume>] with any kind of static pattern. For animated effects, consider using a custom [../tutorials/shaders/shader_reference/fog_shader](fog shader .md).


----



[float<class_float>] **edge_fade** = `0.1` [🔗<class_FogMaterial_property_edge_fade>]


- |void| **set_edge_fade**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_edge_fade**\ (\ )

The hardness of the edges of the [FogVolume<class_FogVolume>]. A higher value will result in softer edges, while a lower value will result in harder edges.


----



[Color<class_Color>] **emission** = `Color(0, 0, 0, 1)` [🔗<class_FogMaterial_property_emission>]


- |void| **set_emission**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_emission**\ (\ )

The [Color<class_Color>] of the light emitted by the [FogVolume<class_FogVolume>]. Emitted light will not cast light or shadows on other objects, but can be useful for modulating the [Color<class_Color>] of the [FogVolume<class_FogVolume>] independently from light sources.


----



[float<class_float>] **height_falloff** = `0.0` [🔗<class_FogMaterial_property_height_falloff>]


- |void| **set_height_falloff**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_height_falloff**\ (\ )

The rate by which the height-based fog decreases in density as height increases in world space. A high falloff will result in a sharp transition, while a low falloff will result in a smoother transition. A value of `0.0` results in uniform-density fog. The height threshold is determined by the height of the associated [FogVolume<class_FogVolume>].

