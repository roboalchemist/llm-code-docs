:github_url: hide



# GradientTexture2D

**Inherits:** [Texture2D<class_Texture2D>] **<** [Texture<class_Texture>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A 2D texture that creates a pattern with colors obtained from a [Gradient<class_Gradient>].


## Description

A 2D texture that obtains colors from a [Gradient<class_Gradient>] to fill the texture data. This texture is able to transform a color transition into different patterns such as a linear or a radial gradient. The texture is filled by interpolating colors starting from [fill_from<class_GradientTexture2D_property_fill_from>] to [fill_to<class_GradientTexture2D_property_fill_to>] offsets by default, but the gradient fill can be repeated to cover the entire texture.

The gradient is sampled individually for each pixel so it does not necessarily represent an exact copy of the gradient (see [width<class_GradientTexture2D_property_width>] and [height<class_GradientTexture2D_property_height>]). See also [GradientTexture1D<class_GradientTexture1D>], [CurveTexture<class_CurveTexture>] and [CurveXYZTexture<class_CurveXYZTexture>].


## Properties

> **TABLE**
> :widths: auto
>
> +----------------------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`Fill<enum_GradientTexture2D_Fill>`     | :ref:`fill<class_GradientTexture2D_property_fill>`           | ``0``                                                                                  |
> +----------------------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`                | :ref:`fill_from<class_GradientTexture2D_property_fill_from>` | ``Vector2(0, 0)``                                                                      |
> +----------------------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`                | :ref:`fill_to<class_GradientTexture2D_property_fill_to>`     | ``Vector2(1, 0)``                                                                      |
> +----------------------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`Gradient<class_Gradient>`              | :ref:`gradient<class_GradientTexture2D_property_gradient>`   |                                                                                        |
> +----------------------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                        | :ref:`height<class_GradientTexture2D_property_height>`       | ``64``                                                                                 |
> +----------------------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`Repeat<enum_GradientTexture2D_Repeat>` | :ref:`repeat<class_GradientTexture2D_property_repeat>`       | ``0``                                                                                  |
> +----------------------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                      | resource_local_to_scene                                      | ``false`` (overrides :ref:`Resource<class_Resource_property_resource_local_to_scene>`) |
> +----------------------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                      | :ref:`use_hdr<class_GradientTexture2D_property_use_hdr>`     | ``false``                                                                              |
> +----------------------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                        | :ref:`width<class_GradientTexture2D_property_width>`         | ``64``                                                                                 |
> +----------------------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **Fill**: [🔗<enum_GradientTexture2D_Fill>]



[Fill<enum_GradientTexture2D_Fill>] **FILL_LINEAR** = `0`

The colors are linearly interpolated in a straight line.



[Fill<enum_GradientTexture2D_Fill>] **FILL_RADIAL** = `1`

The colors are linearly interpolated in a circular pattern.



[Fill<enum_GradientTexture2D_Fill>] **FILL_SQUARE** = `2`

The colors are linearly interpolated in a square pattern.


----



enum **Repeat**: [🔗<enum_GradientTexture2D_Repeat>]



[Repeat<enum_GradientTexture2D_Repeat>] **REPEAT_NONE** = `0`

The gradient fill is restricted to the range defined by [fill_from<class_GradientTexture2D_property_fill_from>] to [fill_to<class_GradientTexture2D_property_fill_to>] offsets.



[Repeat<enum_GradientTexture2D_Repeat>] **REPEAT** = `1`

The texture is filled starting from [fill_from<class_GradientTexture2D_property_fill_from>] to [fill_to<class_GradientTexture2D_property_fill_to>] offsets, repeating the same pattern in both directions.



[Repeat<enum_GradientTexture2D_Repeat>] **REPEAT_MIRROR** = `2`

The texture is filled starting from [fill_from<class_GradientTexture2D_property_fill_from>] to [fill_to<class_GradientTexture2D_property_fill_to>] offsets, mirroring the pattern in both directions.


----


## Property Descriptions



[Fill<enum_GradientTexture2D_Fill>] **fill** = `0` [🔗<class_GradientTexture2D_property_fill>]


- |void| **set_fill**\ (\ value\: [Fill<enum_GradientTexture2D_Fill>]\ )
- [Fill<enum_GradientTexture2D_Fill>] **get_fill**\ (\ )

The gradient's fill type.


----



[Vector2<class_Vector2>] **fill_from** = `Vector2(0, 0)` [🔗<class_GradientTexture2D_property_fill_from>]


- |void| **set_fill_from**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_fill_from**\ (\ )

The initial offset used to fill the texture specified in UV coordinates.


----



[Vector2<class_Vector2>] **fill_to** = `Vector2(1, 0)` [🔗<class_GradientTexture2D_property_fill_to>]


- |void| **set_fill_to**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_fill_to**\ (\ )

The final offset used to fill the texture specified in UV coordinates.


----



[Gradient<class_Gradient>] **gradient** [🔗<class_GradientTexture2D_property_gradient>]


- |void| **set_gradient**\ (\ value\: [Gradient<class_Gradient>]\ )
- [Gradient<class_Gradient>] **get_gradient**\ (\ )

The [Gradient<class_Gradient>] used to fill the texture.


----



[int<class_int>] **height** = `64` [🔗<class_GradientTexture2D_property_height>]


- |void| **set_height**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_height**\ (\ )

The number of vertical color samples that will be obtained from the [Gradient<class_Gradient>], which also represents the texture's height.


----



[Repeat<enum_GradientTexture2D_Repeat>] **repeat** = `0` [🔗<class_GradientTexture2D_property_repeat>]


- |void| **set_repeat**\ (\ value\: [Repeat<enum_GradientTexture2D_Repeat>]\ )
- [Repeat<enum_GradientTexture2D_Repeat>] **get_repeat**\ (\ )

The gradient's repeat type.


----



[bool<class_bool>] **use_hdr** = `false` [🔗<class_GradientTexture2D_property_use_hdr>]


- |void| **set_use_hdr**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_using_hdr**\ (\ )

If `true`, the generated texture will support high dynamic range ([Image.FORMAT_RGBAF<class_Image_constant_FORMAT_RGBAF>] format). This allows for glow effects to work if [Environment.glow_enabled<class_Environment_property_glow_enabled>] is `true`. If `false`, the generated texture will use low dynamic range; overbright colors will be clamped ([Image.FORMAT_RGBA8<class_Image_constant_FORMAT_RGBA8>] format).


----



[int<class_int>] **width** = `64` [🔗<class_GradientTexture2D_property_width>]


- |void| **set_width**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_width**\ (\ )

The number of horizontal color samples that will be obtained from the [Gradient<class_Gradient>], which also represents the texture's width.

