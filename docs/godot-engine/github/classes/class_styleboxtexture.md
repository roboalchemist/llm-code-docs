:github_url: hide



# StyleBoxTexture

**Inherits:** [StyleBox<class_StyleBox>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A texture-based nine-patch [StyleBox<class_StyleBox>].


## Description

A texture-based nine-patch [StyleBox<class_StyleBox>], in a way similar to [NinePatchRect<class_NinePatchRect>]. This stylebox performs a 3×3 scaling of a texture, where only the center cell is fully stretched. This makes it possible to design bordered styles regardless of the stylebox's size.


## Properties

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`AxisStretchMode<enum_StyleBoxTexture_AxisStretchMode>` | :ref:`axis_stretch_horizontal<class_StyleBoxTexture_property_axis_stretch_horizontal>` | ``0``                 |
> +--------------------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`AxisStretchMode<enum_StyleBoxTexture_AxisStretchMode>` | :ref:`axis_stretch_vertical<class_StyleBoxTexture_property_axis_stretch_vertical>`     | ``0``                 |
> +--------------------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                                      | :ref:`draw_center<class_StyleBoxTexture_property_draw_center>`                         | ``true``              |
> +--------------------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                                    | :ref:`expand_margin_bottom<class_StyleBoxTexture_property_expand_margin_bottom>`       | ``0.0``               |
> +--------------------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                                    | :ref:`expand_margin_left<class_StyleBoxTexture_property_expand_margin_left>`           | ``0.0``               |
> +--------------------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                                    | :ref:`expand_margin_right<class_StyleBoxTexture_property_expand_margin_right>`         | ``0.0``               |
> +--------------------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                                    | :ref:`expand_margin_top<class_StyleBoxTexture_property_expand_margin_top>`             | ``0.0``               |
> +--------------------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>`                                    | :ref:`modulate_color<class_StyleBoxTexture_property_modulate_color>`                   | ``Color(1, 1, 1, 1)`` |
> +--------------------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Rect2<class_Rect2>`                                    | :ref:`region_rect<class_StyleBoxTexture_property_region_rect>`                         | ``Rect2(0, 0, 0, 0)`` |
> +--------------------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Texture2D<class_Texture2D>`                            | :ref:`texture<class_StyleBoxTexture_property_texture>`                                 |                       |
> +--------------------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                                    | :ref:`texture_margin_bottom<class_StyleBoxTexture_property_texture_margin_bottom>`     | ``0.0``               |
> +--------------------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                                    | :ref:`texture_margin_left<class_StyleBoxTexture_property_texture_margin_left>`         | ``0.0``               |
> +--------------------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                                    | :ref:`texture_margin_right<class_StyleBoxTexture_property_texture_margin_right>`       | ``0.0``               |
> +--------------------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                                    | :ref:`texture_margin_top<class_StyleBoxTexture_property_texture_margin_top>`           | ``0.0``               |
> +--------------------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`get_expand_margin<class_StyleBoxTexture_method_get_expand_margin>`\ (\ margin\: :ref:`Side<enum_@GlobalScope_Side>`\ ) |const|                             |
> +---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`get_texture_margin<class_StyleBoxTexture_method_get_texture_margin>`\ (\ margin\: :ref:`Side<enum_@GlobalScope_Side>`\ ) |const|                           |
> +---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_expand_margin<class_StyleBoxTexture_method_set_expand_margin>`\ (\ margin\: :ref:`Side<enum_@GlobalScope_Side>`, size\: :ref:`float<class_float>`\ )   |
> +---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_expand_margin_all<class_StyleBoxTexture_method_set_expand_margin_all>`\ (\ size\: :ref:`float<class_float>`\ )                                         |
> +---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_texture_margin<class_StyleBoxTexture_method_set_texture_margin>`\ (\ margin\: :ref:`Side<enum_@GlobalScope_Side>`, size\: :ref:`float<class_float>`\ ) |
> +---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_texture_margin_all<class_StyleBoxTexture_method_set_texture_margin_all>`\ (\ size\: :ref:`float<class_float>`\ )                                       |
> +---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **AxisStretchMode**: [🔗<enum_StyleBoxTexture_AxisStretchMode>]



[AxisStretchMode<enum_StyleBoxTexture_AxisStretchMode>] **AXIS_STRETCH_MODE_STRETCH** = `0`

Stretch the stylebox's texture. This results in visible distortion unless the texture size matches the stylebox's size perfectly.



[AxisStretchMode<enum_StyleBoxTexture_AxisStretchMode>] **AXIS_STRETCH_MODE_TILE** = `1`

Repeats the stylebox's texture to match the stylebox's size according to the nine-patch system.



[AxisStretchMode<enum_StyleBoxTexture_AxisStretchMode>] **AXIS_STRETCH_MODE_TILE_FIT** = `2`

Repeats the stylebox's texture to match the stylebox's size according to the nine-patch system. Unlike [AXIS_STRETCH_MODE_TILE<class_StyleBoxTexture_constant_AXIS_STRETCH_MODE_TILE>], the texture may be slightly stretched to make the nine-patch texture tile seamlessly.


----


## Property Descriptions



[AxisStretchMode<enum_StyleBoxTexture_AxisStretchMode>] **axis_stretch_horizontal** = `0` [🔗<class_StyleBoxTexture_property_axis_stretch_horizontal>]


- |void| **set_h_axis_stretch_mode**\ (\ value\: [AxisStretchMode<enum_StyleBoxTexture_AxisStretchMode>]\ )
- [AxisStretchMode<enum_StyleBoxTexture_AxisStretchMode>] **get_h_axis_stretch_mode**\ (\ )

Controls how the stylebox's texture will be stretched or tiled horizontally.


----



[AxisStretchMode<enum_StyleBoxTexture_AxisStretchMode>] **axis_stretch_vertical** = `0` [🔗<class_StyleBoxTexture_property_axis_stretch_vertical>]


- |void| **set_v_axis_stretch_mode**\ (\ value\: [AxisStretchMode<enum_StyleBoxTexture_AxisStretchMode>]\ )
- [AxisStretchMode<enum_StyleBoxTexture_AxisStretchMode>] **get_v_axis_stretch_mode**\ (\ )

Controls how the stylebox's texture will be stretched or tiled vertically.


----



[bool<class_bool>] **draw_center** = `true` [🔗<class_StyleBoxTexture_property_draw_center>]


- |void| **set_draw_center**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_draw_center_enabled**\ (\ )

If `true`, the nine-patch texture's center tile will be drawn.


----



[float<class_float>] **expand_margin_bottom** = `0.0` [🔗<class_StyleBoxTexture_property_expand_margin_bottom>]


- |void| **set_expand_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], size\: [float<class_float>]\ )
- [float<class_float>] **get_expand_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

Expands the bottom margin of this style box when drawing, causing it to be drawn larger than requested.


----



[float<class_float>] **expand_margin_left** = `0.0` [🔗<class_StyleBoxTexture_property_expand_margin_left>]


- |void| **set_expand_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], size\: [float<class_float>]\ )
- [float<class_float>] **get_expand_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

Expands the left margin of this style box when drawing, causing it to be drawn larger than requested.


----



[float<class_float>] **expand_margin_right** = `0.0` [🔗<class_StyleBoxTexture_property_expand_margin_right>]


- |void| **set_expand_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], size\: [float<class_float>]\ )
- [float<class_float>] **get_expand_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

Expands the right margin of this style box when drawing, causing it to be drawn larger than requested.


----



[float<class_float>] **expand_margin_top** = `0.0` [🔗<class_StyleBoxTexture_property_expand_margin_top>]


- |void| **set_expand_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], size\: [float<class_float>]\ )
- [float<class_float>] **get_expand_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

Expands the top margin of this style box when drawing, causing it to be drawn larger than requested.


----



[Color<class_Color>] **modulate_color** = `Color(1, 1, 1, 1)` [🔗<class_StyleBoxTexture_property_modulate_color>]


- |void| **set_modulate**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_modulate**\ (\ )

Modulates the color of the texture when this style box is drawn.


----



[Rect2<class_Rect2>] **region_rect** = `Rect2(0, 0, 0, 0)` [🔗<class_StyleBoxTexture_property_region_rect>]


- |void| **set_region_rect**\ (\ value\: [Rect2<class_Rect2>]\ )
- [Rect2<class_Rect2>] **get_region_rect**\ (\ )

The region to use from the [texture<class_StyleBoxTexture_property_texture>].

This is equivalent to first wrapping the [texture<class_StyleBoxTexture_property_texture>] in an [AtlasTexture<class_AtlasTexture>] with the same region.

If empty (`Rect2(0, 0, 0, 0)`), the whole [texture<class_StyleBoxTexture_property_texture>] is used.


----



[Texture2D<class_Texture2D>] **texture** [🔗<class_StyleBoxTexture_property_texture>]


- |void| **set_texture**\ (\ value\: [Texture2D<class_Texture2D>]\ )
- [Texture2D<class_Texture2D>] **get_texture**\ (\ )

The texture to use when drawing this style box.


----



[float<class_float>] **texture_margin_bottom** = `0.0` [🔗<class_StyleBoxTexture_property_texture_margin_bottom>]


- |void| **set_texture_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], size\: [float<class_float>]\ )
- [float<class_float>] **get_texture_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

Increases the bottom margin of the 3×3 texture box.

A higher value means more of the source texture is considered to be part of the bottom border of the 3×3 box.

This is also the value used as fallback for [StyleBox.content_margin_bottom<class_StyleBox_property_content_margin_bottom>] if it is negative.


----



[float<class_float>] **texture_margin_left** = `0.0` [🔗<class_StyleBoxTexture_property_texture_margin_left>]


- |void| **set_texture_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], size\: [float<class_float>]\ )
- [float<class_float>] **get_texture_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

Increases the left margin of the 3×3 texture box.

A higher value means more of the source texture is considered to be part of the left border of the 3×3 box.

This is also the value used as fallback for [StyleBox.content_margin_left<class_StyleBox_property_content_margin_left>] if it is negative.


----



[float<class_float>] **texture_margin_right** = `0.0` [🔗<class_StyleBoxTexture_property_texture_margin_right>]


- |void| **set_texture_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], size\: [float<class_float>]\ )
- [float<class_float>] **get_texture_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

Increases the right margin of the 3×3 texture box.

A higher value means more of the source texture is considered to be part of the right border of the 3×3 box.

This is also the value used as fallback for [StyleBox.content_margin_right<class_StyleBox_property_content_margin_right>] if it is negative.


----



[float<class_float>] **texture_margin_top** = `0.0` [🔗<class_StyleBoxTexture_property_texture_margin_top>]


- |void| **set_texture_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], size\: [float<class_float>]\ )
- [float<class_float>] **get_texture_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

Increases the top margin of the 3×3 texture box.

A higher value means more of the source texture is considered to be part of the top border of the 3×3 box.

This is also the value used as fallback for [StyleBox.content_margin_top<class_StyleBox_property_content_margin_top>] if it is negative.


----


## Method Descriptions



[float<class_float>] **get_expand_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const| [🔗<class_StyleBoxTexture_method_get_expand_margin>]

Returns the expand margin size of the specified [Side<enum_@GlobalScope_Side>].


----



[float<class_float>] **get_texture_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const| [🔗<class_StyleBoxTexture_method_get_texture_margin>]

Returns the margin size of the specified [Side<enum_@GlobalScope_Side>].


----



|void| **set_expand_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], size\: [float<class_float>]\ ) [🔗<class_StyleBoxTexture_method_set_expand_margin>]

Sets the expand margin to `size` pixels for the specified [Side<enum_@GlobalScope_Side>].


----



|void| **set_expand_margin_all**\ (\ size\: [float<class_float>]\ ) [🔗<class_StyleBoxTexture_method_set_expand_margin_all>]

Sets the expand margin to `size` pixels for all sides.


----



|void| **set_texture_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], size\: [float<class_float>]\ ) [🔗<class_StyleBoxTexture_method_set_texture_margin>]

Sets the margin to `size` pixels for the specified [Side<enum_@GlobalScope_Side>].


----



|void| **set_texture_margin_all**\ (\ size\: [float<class_float>]\ ) [🔗<class_StyleBoxTexture_method_set_texture_margin_all>]

Sets the margin to `size` pixels for all sides.

