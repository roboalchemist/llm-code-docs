:github_url: hide



# CurveTexture

**Inherits:** [Texture2D<class_Texture2D>] **<** [Texture<class_Texture>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A 1D texture where pixel brightness corresponds to points on a curve.


## Description

A 1D texture where pixel brightness corresponds to points on a unit [Curve<class_Curve>] resource, either in grayscale or in red. This visual representation simplifies the task of saving curves as image files.

If you need to store up to 3 curves within a single texture, use [CurveXYZTexture<class_CurveXYZTexture>] instead. See also [GradientTexture1D<class_GradientTexture1D>] and [GradientTexture2D<class_GradientTexture2D>].


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------+---------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`Curve<class_Curve>`                         | :ref:`curve<class_CurveTexture_property_curve>`               |                                                                                        |
> +---------------------------------------------------+---------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | resource_local_to_scene                                       | ``false`` (overrides :ref:`Resource<class_Resource_property_resource_local_to_scene>`) |
> +---------------------------------------------------+---------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`TextureMode<enum_CurveTexture_TextureMode>` | :ref:`texture_mode<class_CurveTexture_property_texture_mode>` | ``0``                                                                                  |
> +---------------------------------------------------+---------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                             | :ref:`width<class_CurveTexture_property_width>`               | ``256``                                                                                |
> +---------------------------------------------------+---------------------------------------------------------------+----------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **TextureMode**: [🔗<enum_CurveTexture_TextureMode>]



[TextureMode<enum_CurveTexture_TextureMode>] **TEXTURE_MODE_RGB** = `0`

Store the curve equally across the red, green and blue channels. This uses more video memory, but is more compatible with shaders that only read the green and blue values.



[TextureMode<enum_CurveTexture_TextureMode>] **TEXTURE_MODE_RED** = `1`

Store the curve only in the red channel. This saves video memory, but some custom shaders may not be able to work with this.


----


## Property Descriptions



[Curve<class_Curve>] **curve** [🔗<class_CurveTexture_property_curve>]


- |void| **set_curve**\ (\ value\: [Curve<class_Curve>]\ )
- [Curve<class_Curve>] **get_curve**\ (\ )

The [Curve<class_Curve>] that is rendered onto the texture. Should be a unit [Curve<class_Curve>].


----



[TextureMode<enum_CurveTexture_TextureMode>] **texture_mode** = `0` [🔗<class_CurveTexture_property_texture_mode>]


- |void| **set_texture_mode**\ (\ value\: [TextureMode<enum_CurveTexture_TextureMode>]\ )
- [TextureMode<enum_CurveTexture_TextureMode>] **get_texture_mode**\ (\ )

The format the texture should be generated with. When passing a CurveTexture as an input to a [Shader<class_Shader>], this may need to be adjusted.


----



[int<class_int>] **width** = `256` [🔗<class_CurveTexture_property_width>]


- |void| **set_width**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_width**\ (\ )

The width of the texture (in pixels). Higher values make it possible to represent high-frequency data better (such as sudden direction changes), at the cost of increased generation time and memory usage.

