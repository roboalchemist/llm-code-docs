:github_url: hide



# Gradient

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A color transition.


## Description

This resource describes a color transition by defining a set of colored points and how to interpolate between them.

See also [Curve<class_Curve>] which supports more complex easing methods, but does not support colors.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------+----------------------------------------------+
> | :ref:`PackedColorArray<class_PackedColorArray>`           | :ref:`colors<class_Gradient_property_colors>`                                       | ``PackedColorArray(0, 0, 0, 1, 1, 1, 1, 1)`` |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------+----------------------------------------------+
> | :ref:`ColorSpace<enum_Gradient_ColorSpace>`               | :ref:`interpolation_color_space<class_Gradient_property_interpolation_color_space>` | ``0``                                        |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------+----------------------------------------------+
> | :ref:`InterpolationMode<enum_Gradient_InterpolationMode>` | :ref:`interpolation_mode<class_Gradient_property_interpolation_mode>`               | ``0``                                        |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------+----------------------------------------------+
> | :ref:`PackedFloat32Array<class_PackedFloat32Array>`       | :ref:`offsets<class_Gradient_property_offsets>`                                     | ``PackedFloat32Array(0, 1)``                 |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------+----------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------+--------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`add_point<class_Gradient_method_add_point>`\ (\ offset\: :ref:`float<class_float>`, color\: :ref:`Color<class_Color>`\ ) |
> +---------------------------+--------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Color<class_Color>` | :ref:`get_color<class_Gradient_method_get_color>`\ (\ point\: :ref:`int<class_int>`\ )                                         |
> +---------------------------+--------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`get_offset<class_Gradient_method_get_offset>`\ (\ point\: :ref:`int<class_int>`\ )                                       |
> +---------------------------+--------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`     | :ref:`get_point_count<class_Gradient_method_get_point_count>`\ (\ ) |const|                                                    |
> +---------------------------+--------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`remove_point<class_Gradient_method_remove_point>`\ (\ point\: :ref:`int<class_int>`\ )                                   |
> +---------------------------+--------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`reverse<class_Gradient_method_reverse>`\ (\ )                                                                            |
> +---------------------------+--------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Color<class_Color>` | :ref:`sample<class_Gradient_method_sample>`\ (\ offset\: :ref:`float<class_float>`\ )                                          |
> +---------------------------+--------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_color<class_Gradient_method_set_color>`\ (\ point\: :ref:`int<class_int>`, color\: :ref:`Color<class_Color>`\ )      |
> +---------------------------+--------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_offset<class_Gradient_method_set_offset>`\ (\ point\: :ref:`int<class_int>`, offset\: :ref:`float<class_float>`\ )   |
> +---------------------------+--------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **InterpolationMode**: [🔗<enum_Gradient_InterpolationMode>]



[InterpolationMode<enum_Gradient_InterpolationMode>] **GRADIENT_INTERPOLATE_LINEAR** = `0`

Linear interpolation.



[InterpolationMode<enum_Gradient_InterpolationMode>] **GRADIENT_INTERPOLATE_CONSTANT** = `1`

Constant interpolation, color changes abruptly at each point and stays uniform between. This might cause visible aliasing when used for a gradient texture in some cases.



[InterpolationMode<enum_Gradient_InterpolationMode>] **GRADIENT_INTERPOLATE_CUBIC** = `2`

Cubic interpolation.


----



enum **ColorSpace**: [🔗<enum_Gradient_ColorSpace>]



[ColorSpace<enum_Gradient_ColorSpace>] **GRADIENT_COLOR_SPACE_SRGB** = `0`

sRGB color space.



[ColorSpace<enum_Gradient_ColorSpace>] **GRADIENT_COLOR_SPACE_LINEAR_SRGB** = `1`

Linear sRGB color space.



[ColorSpace<enum_Gradient_ColorSpace>] **GRADIENT_COLOR_SPACE_OKLAB** = `2`

[Oklab ](https://bottosson.github.io/posts/oklab/)_ color space. This color space provides a smooth and uniform-looking transition between colors.


----


## Property Descriptions



[PackedColorArray<class_PackedColorArray>] **colors** = `PackedColorArray(0, 0, 0, 1, 1, 1, 1, 1)` [🔗<class_Gradient_property_colors>]


- |void| **set_colors**\ (\ value\: [PackedColorArray<class_PackedColorArray>]\ )
- [PackedColorArray<class_PackedColorArray>] **get_colors**\ (\ )

Gradient's colors as a [PackedColorArray<class_PackedColorArray>].

\ **Note:** Setting this property updates all colors at once. To update any color individually use [set_color()<class_Gradient_method_set_color>].

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedColorArray<class_PackedColorArray>] for more details.


----



[ColorSpace<enum_Gradient_ColorSpace>] **interpolation_color_space** = `0` [🔗<class_Gradient_property_interpolation_color_space>]


- |void| **set_interpolation_color_space**\ (\ value\: [ColorSpace<enum_Gradient_ColorSpace>]\ )
- [ColorSpace<enum_Gradient_ColorSpace>] **get_interpolation_color_space**\ (\ )

The color space used to interpolate between points of the gradient. It does not affect the returned colors, which will always use nonlinear sRGB encoding.

\ **Note:** This setting has no effect when [interpolation_mode<class_Gradient_property_interpolation_mode>] is set to [GRADIENT_INTERPOLATE_CONSTANT<class_Gradient_constant_GRADIENT_INTERPOLATE_CONSTANT>].


----



[InterpolationMode<enum_Gradient_InterpolationMode>] **interpolation_mode** = `0` [🔗<class_Gradient_property_interpolation_mode>]


- |void| **set_interpolation_mode**\ (\ value\: [InterpolationMode<enum_Gradient_InterpolationMode>]\ )
- [InterpolationMode<enum_Gradient_InterpolationMode>] **get_interpolation_mode**\ (\ )

The algorithm used to interpolate between points of the gradient.


----



[PackedFloat32Array<class_PackedFloat32Array>] **offsets** = `PackedFloat32Array(0, 1)` [🔗<class_Gradient_property_offsets>]


- |void| **set_offsets**\ (\ value\: [PackedFloat32Array<class_PackedFloat32Array>]\ )
- [PackedFloat32Array<class_PackedFloat32Array>] **get_offsets**\ (\ )

Gradient's offsets as a [PackedFloat32Array<class_PackedFloat32Array>].

\ **Note:** Setting this property updates all offsets at once. To update any offset individually use [set_offset()<class_Gradient_method_set_offset>].

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedFloat32Array<class_PackedFloat32Array>] for more details.


----


## Method Descriptions



|void| **add_point**\ (\ offset\: [float<class_float>], color\: [Color<class_Color>]\ ) [🔗<class_Gradient_method_add_point>]

Adds the specified color to the gradient, with the specified offset.


----



[Color<class_Color>] **get_color**\ (\ point\: [int<class_int>]\ ) [🔗<class_Gradient_method_get_color>]

Returns the color of the gradient color at index `point`.


----



[float<class_float>] **get_offset**\ (\ point\: [int<class_int>]\ ) [🔗<class_Gradient_method_get_offset>]

Returns the offset of the gradient color at index `point`.


----



[int<class_int>] **get_point_count**\ (\ ) |const| [🔗<class_Gradient_method_get_point_count>]

Returns the number of colors in the gradient.


----



|void| **remove_point**\ (\ point\: [int<class_int>]\ ) [🔗<class_Gradient_method_remove_point>]

Removes the color at index `point`.


----



|void| **reverse**\ (\ ) [🔗<class_Gradient_method_reverse>]

Reverses/mirrors the gradient.

\ **Note:** This method mirrors all points around the middle of the gradient, which may produce unexpected results when [interpolation_mode<class_Gradient_property_interpolation_mode>] is set to [GRADIENT_INTERPOLATE_CONSTANT<class_Gradient_constant_GRADIENT_INTERPOLATE_CONSTANT>].


----



[Color<class_Color>] **sample**\ (\ offset\: [float<class_float>]\ ) [🔗<class_Gradient_method_sample>]

Returns the interpolated color specified by `offset`. `offset` should be between `0.0` and `1.0` (inclusive). Using a value lower than `0.0` will return the same color as `0.0`, and using a value higher than `1.0` will return the same color as `1.0`. If your input value is not within this range, consider using [@GlobalScope.remap()<class_@GlobalScope_method_remap>] on the input value with output values set to `0.0` and `1.0`.


----



|void| **set_color**\ (\ point\: [int<class_int>], color\: [Color<class_Color>]\ ) [🔗<class_Gradient_method_set_color>]

Sets the color of the gradient color at index `point`.


----



|void| **set_offset**\ (\ point\: [int<class_int>], offset\: [float<class_float>]\ ) [🔗<class_Gradient_method_set_offset>]

Sets the offset for the gradient color at index `point`.

