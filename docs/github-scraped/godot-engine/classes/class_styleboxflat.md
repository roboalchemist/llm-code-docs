:github_url: hide



# StyleBoxFlat

**Inherits:** [StyleBox<class_StyleBox>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A customizable [StyleBox<class_StyleBox>] that doesn't use a texture.


## Description

By configuring various properties of this style box, you can achieve many common looks without the need of a texture. This includes optionally rounded borders, antialiasing, shadows, and skew.

Setting corner radius to high values is allowed. As soon as corners overlap, the stylebox will switch to a relative system:

> **CODE**
>
> height = 30
> corner_radius_top_left = 50
> corner_radius_bottom_left = 100
>
The relative system now would take the 1:2 ratio of the two left corners to calculate the actual corner width. Both corners added will **never** be more than the height. Result:

> **CODE**
>
> corner_radius_top_left: 10
> corner_radius_bottom_left: 20
>

## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------------+
> | :ref:`bool<class_bool>`       | :ref:`anti_aliasing<class_StyleBoxFlat_property_anti_aliasing>`                           | ``true``                    |
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------------+
> | :ref:`float<class_float>`     | :ref:`anti_aliasing_size<class_StyleBoxFlat_property_anti_aliasing_size>`                 | ``1.0``                     |
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------------+
> | :ref:`Color<class_Color>`     | :ref:`bg_color<class_StyleBoxFlat_property_bg_color>`                                     | ``Color(0.6, 0.6, 0.6, 1)`` |
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------------+
> | :ref:`bool<class_bool>`       | :ref:`border_blend<class_StyleBoxFlat_property_border_blend>`                             | ``false``                   |
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------------+
> | :ref:`Color<class_Color>`     | :ref:`border_color<class_StyleBoxFlat_property_border_color>`                             | ``Color(0.8, 0.8, 0.8, 1)`` |
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------------+
> | :ref:`int<class_int>`         | :ref:`border_width_bottom<class_StyleBoxFlat_property_border_width_bottom>`               | ``0``                       |
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------------+
> | :ref:`int<class_int>`         | :ref:`border_width_left<class_StyleBoxFlat_property_border_width_left>`                   | ``0``                       |
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------------+
> | :ref:`int<class_int>`         | :ref:`border_width_right<class_StyleBoxFlat_property_border_width_right>`                 | ``0``                       |
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------------+
> | :ref:`int<class_int>`         | :ref:`border_width_top<class_StyleBoxFlat_property_border_width_top>`                     | ``0``                       |
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------------+
> | :ref:`int<class_int>`         | :ref:`corner_detail<class_StyleBoxFlat_property_corner_detail>`                           | ``8``                       |
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------------+
> | :ref:`int<class_int>`         | :ref:`corner_radius_bottom_left<class_StyleBoxFlat_property_corner_radius_bottom_left>`   | ``0``                       |
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------------+
> | :ref:`int<class_int>`         | :ref:`corner_radius_bottom_right<class_StyleBoxFlat_property_corner_radius_bottom_right>` | ``0``                       |
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------------+
> | :ref:`int<class_int>`         | :ref:`corner_radius_top_left<class_StyleBoxFlat_property_corner_radius_top_left>`         | ``0``                       |
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------------+
> | :ref:`int<class_int>`         | :ref:`corner_radius_top_right<class_StyleBoxFlat_property_corner_radius_top_right>`       | ``0``                       |
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------------+
> | :ref:`bool<class_bool>`       | :ref:`draw_center<class_StyleBoxFlat_property_draw_center>`                               | ``true``                    |
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------------+
> | :ref:`float<class_float>`     | :ref:`expand_margin_bottom<class_StyleBoxFlat_property_expand_margin_bottom>`             | ``0.0``                     |
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------------+
> | :ref:`float<class_float>`     | :ref:`expand_margin_left<class_StyleBoxFlat_property_expand_margin_left>`                 | ``0.0``                     |
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------------+
> | :ref:`float<class_float>`     | :ref:`expand_margin_right<class_StyleBoxFlat_property_expand_margin_right>`               | ``0.0``                     |
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------------+
> | :ref:`float<class_float>`     | :ref:`expand_margin_top<class_StyleBoxFlat_property_expand_margin_top>`                   | ``0.0``                     |
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------------+
> | :ref:`Color<class_Color>`     | :ref:`shadow_color<class_StyleBoxFlat_property_shadow_color>`                             | ``Color(0, 0, 0, 0.6)``     |
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`shadow_offset<class_StyleBoxFlat_property_shadow_offset>`                           | ``Vector2(0, 0)``           |
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------------+
> | :ref:`int<class_int>`         | :ref:`shadow_size<class_StyleBoxFlat_property_shadow_size>`                               | ``0``                       |
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`skew<class_StyleBoxFlat_property_skew>`                                             | ``Vector2(0, 0)``           |
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`     | :ref:`get_border_width<class_StyleBoxFlat_method_get_border_width>`\ (\ margin\: :ref:`Side<enum_@GlobalScope_Side>`\ ) |const|                               |
> +---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`     | :ref:`get_border_width_min<class_StyleBoxFlat_method_get_border_width_min>`\ (\ ) |const|                                                                     |
> +---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`     | :ref:`get_corner_radius<class_StyleBoxFlat_method_get_corner_radius>`\ (\ corner\: :ref:`Corner<enum_@GlobalScope_Corner>`\ ) |const|                         |
> +---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`get_expand_margin<class_StyleBoxFlat_method_get_expand_margin>`\ (\ margin\: :ref:`Side<enum_@GlobalScope_Side>`\ ) |const|                             |
> +---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_border_width<class_StyleBoxFlat_method_set_border_width>`\ (\ margin\: :ref:`Side<enum_@GlobalScope_Side>`, width\: :ref:`int<class_int>`\ )        |
> +---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_border_width_all<class_StyleBoxFlat_method_set_border_width_all>`\ (\ width\: :ref:`int<class_int>`\ )                                              |
> +---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_corner_radius<class_StyleBoxFlat_method_set_corner_radius>`\ (\ corner\: :ref:`Corner<enum_@GlobalScope_Corner>`, radius\: :ref:`int<class_int>`\ ) |
> +---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_corner_radius_all<class_StyleBoxFlat_method_set_corner_radius_all>`\ (\ radius\: :ref:`int<class_int>`\ )                                           |
> +---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_expand_margin<class_StyleBoxFlat_method_set_expand_margin>`\ (\ margin\: :ref:`Side<enum_@GlobalScope_Side>`, size\: :ref:`float<class_float>`\ )   |
> +---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_expand_margin_all<class_StyleBoxFlat_method_set_expand_margin_all>`\ (\ size\: :ref:`float<class_float>`\ )                                         |
> +---------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[bool<class_bool>] **anti_aliasing** = `true` [🔗<class_StyleBoxFlat_property_anti_aliasing>]


- |void| **set_anti_aliased**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_anti_aliased**\ (\ )

Antialiasing draws a small ring around the edges, which fades to transparency. As a result, edges look much smoother. This is only noticeable when using rounded corners or [skew<class_StyleBoxFlat_property_skew>].

\ **Note:** When using beveled corners with 45-degree angles ([corner_detail<class_StyleBoxFlat_property_corner_detail>] = 1), it is recommended to set [anti_aliasing<class_StyleBoxFlat_property_anti_aliasing>] to `false` to ensure crisp visuals and avoid possible visual glitches.


----



[float<class_float>] **anti_aliasing_size** = `1.0` [🔗<class_StyleBoxFlat_property_anti_aliasing_size>]


- |void| **set_aa_size**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_aa_size**\ (\ )

This changes the size of the antialiasing effect. `1.0` is recommended for an optimal result at 100% scale, identical to how rounded rectangles are rendered in web browsers and most vector drawing software.

\ **Note:** Higher values may produce a blur effect but can also create undesired artifacts on small boxes with large-radius corners.


----



[Color<class_Color>] **bg_color** = `Color(0.6, 0.6, 0.6, 1)` [🔗<class_StyleBoxFlat_property_bg_color>]


- |void| **set_bg_color**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_bg_color**\ (\ )

The background color of the stylebox.


----



[bool<class_bool>] **border_blend** = `false` [🔗<class_StyleBoxFlat_property_border_blend>]


- |void| **set_border_blend**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_border_blend**\ (\ )

If `true`, the border will fade into the background color.


----



[Color<class_Color>] **border_color** = `Color(0.8, 0.8, 0.8, 1)` [🔗<class_StyleBoxFlat_property_border_color>]


- |void| **set_border_color**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_border_color**\ (\ )

Sets the color of the border.


----



[int<class_int>] **border_width_bottom** = `0` [🔗<class_StyleBoxFlat_property_border_width_bottom>]


- |void| **set_border_width**\ (\ margin\: [Side<enum_@GlobalScope_Side>], width\: [int<class_int>]\ )
- [int<class_int>] **get_border_width**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

Border width for the bottom border.


----



[int<class_int>] **border_width_left** = `0` [🔗<class_StyleBoxFlat_property_border_width_left>]


- |void| **set_border_width**\ (\ margin\: [Side<enum_@GlobalScope_Side>], width\: [int<class_int>]\ )
- [int<class_int>] **get_border_width**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

Border width for the left border.


----



[int<class_int>] **border_width_right** = `0` [🔗<class_StyleBoxFlat_property_border_width_right>]


- |void| **set_border_width**\ (\ margin\: [Side<enum_@GlobalScope_Side>], width\: [int<class_int>]\ )
- [int<class_int>] **get_border_width**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

Border width for the right border.


----



[int<class_int>] **border_width_top** = `0` [🔗<class_StyleBoxFlat_property_border_width_top>]


- |void| **set_border_width**\ (\ margin\: [Side<enum_@GlobalScope_Side>], width\: [int<class_int>]\ )
- [int<class_int>] **get_border_width**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

Border width for the top border.


----



[int<class_int>] **corner_detail** = `8` [🔗<class_StyleBoxFlat_property_corner_detail>]


- |void| **set_corner_detail**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_corner_detail**\ (\ )

This sets the number of vertices used for each corner. Higher values result in rounder corners but take more processing power to compute. When choosing a value, you should take the corner radius ([set_corner_radius_all()<class_StyleBoxFlat_method_set_corner_radius_all>]) into account.

For corner radii less than 10, `4` or `5` should be enough. For corner radii less than 30, values between `8` and `12` should be enough.

A corner detail of `1` will result in chamfered corners instead of rounded corners, which is useful for some artistic effects.


----



[int<class_int>] **corner_radius_bottom_left** = `0` [🔗<class_StyleBoxFlat_property_corner_radius_bottom_left>]


- |void| **set_corner_radius**\ (\ corner\: [Corner<enum_@GlobalScope_Corner>], radius\: [int<class_int>]\ )
- [int<class_int>] **get_corner_radius**\ (\ corner\: [Corner<enum_@GlobalScope_Corner>]\ ) |const|

The bottom-left corner's radius. If `0`, the corner is not rounded.


----



[int<class_int>] **corner_radius_bottom_right** = `0` [🔗<class_StyleBoxFlat_property_corner_radius_bottom_right>]


- |void| **set_corner_radius**\ (\ corner\: [Corner<enum_@GlobalScope_Corner>], radius\: [int<class_int>]\ )
- [int<class_int>] **get_corner_radius**\ (\ corner\: [Corner<enum_@GlobalScope_Corner>]\ ) |const|

The bottom-right corner's radius. If `0`, the corner is not rounded.


----



[int<class_int>] **corner_radius_top_left** = `0` [🔗<class_StyleBoxFlat_property_corner_radius_top_left>]


- |void| **set_corner_radius**\ (\ corner\: [Corner<enum_@GlobalScope_Corner>], radius\: [int<class_int>]\ )
- [int<class_int>] **get_corner_radius**\ (\ corner\: [Corner<enum_@GlobalScope_Corner>]\ ) |const|

The top-left corner's radius. If `0`, the corner is not rounded.


----



[int<class_int>] **corner_radius_top_right** = `0` [🔗<class_StyleBoxFlat_property_corner_radius_top_right>]


- |void| **set_corner_radius**\ (\ corner\: [Corner<enum_@GlobalScope_Corner>], radius\: [int<class_int>]\ )
- [int<class_int>] **get_corner_radius**\ (\ corner\: [Corner<enum_@GlobalScope_Corner>]\ ) |const|

The top-right corner's radius. If `0`, the corner is not rounded.


----



[bool<class_bool>] **draw_center** = `true` [🔗<class_StyleBoxFlat_property_draw_center>]


- |void| **set_draw_center**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_draw_center_enabled**\ (\ )

Toggles drawing of the inner part of the stylebox.


----



[float<class_float>] **expand_margin_bottom** = `0.0` [🔗<class_StyleBoxFlat_property_expand_margin_bottom>]


- |void| **set_expand_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], size\: [float<class_float>]\ )
- [float<class_float>] **get_expand_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

Expands the stylebox outside of the control rect on the bottom edge. Useful in combination with [border_width_bottom<class_StyleBoxFlat_property_border_width_bottom>] to draw a border outside the control rect.

\ **Note:** Unlike [StyleBox.content_margin_bottom<class_StyleBox_property_content_margin_bottom>], [expand_margin_bottom<class_StyleBoxFlat_property_expand_margin_bottom>] does *not* affect the size of the clickable area for [Control<class_Control>]\ s. This can negatively impact usability if used wrong, as the user may try to click an area of the StyleBox that cannot actually receive clicks.


----



[float<class_float>] **expand_margin_left** = `0.0` [🔗<class_StyleBoxFlat_property_expand_margin_left>]


- |void| **set_expand_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], size\: [float<class_float>]\ )
- [float<class_float>] **get_expand_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

Expands the stylebox outside of the control rect on the left edge. Useful in combination with [border_width_left<class_StyleBoxFlat_property_border_width_left>] to draw a border outside the control rect.

\ **Note:** Unlike [StyleBox.content_margin_left<class_StyleBox_property_content_margin_left>], [expand_margin_left<class_StyleBoxFlat_property_expand_margin_left>] does *not* affect the size of the clickable area for [Control<class_Control>]\ s. This can negatively impact usability if used wrong, as the user may try to click an area of the StyleBox that cannot actually receive clicks.


----



[float<class_float>] **expand_margin_right** = `0.0` [🔗<class_StyleBoxFlat_property_expand_margin_right>]


- |void| **set_expand_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], size\: [float<class_float>]\ )
- [float<class_float>] **get_expand_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

Expands the stylebox outside of the control rect on the right edge. Useful in combination with [border_width_right<class_StyleBoxFlat_property_border_width_right>] to draw a border outside the control rect.

\ **Note:** Unlike [StyleBox.content_margin_right<class_StyleBox_property_content_margin_right>], [expand_margin_right<class_StyleBoxFlat_property_expand_margin_right>] does *not* affect the size of the clickable area for [Control<class_Control>]\ s. This can negatively impact usability if used wrong, as the user may try to click an area of the StyleBox that cannot actually receive clicks.


----



[float<class_float>] **expand_margin_top** = `0.0` [🔗<class_StyleBoxFlat_property_expand_margin_top>]


- |void| **set_expand_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], size\: [float<class_float>]\ )
- [float<class_float>] **get_expand_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

Expands the stylebox outside of the control rect on the top edge. Useful in combination with [border_width_top<class_StyleBoxFlat_property_border_width_top>] to draw a border outside the control rect.

\ **Note:** Unlike [StyleBox.content_margin_top<class_StyleBox_property_content_margin_top>], [expand_margin_top<class_StyleBoxFlat_property_expand_margin_top>] does *not* affect the size of the clickable area for [Control<class_Control>]\ s. This can negatively impact usability if used wrong, as the user may try to click an area of the StyleBox that cannot actually receive clicks.


----



[Color<class_Color>] **shadow_color** = `Color(0, 0, 0, 0.6)` [🔗<class_StyleBoxFlat_property_shadow_color>]


- |void| **set_shadow_color**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_shadow_color**\ (\ )

The color of the shadow. This has no effect if [shadow_size<class_StyleBoxFlat_property_shadow_size>] is lower than 1.


----



[Vector2<class_Vector2>] **shadow_offset** = `Vector2(0, 0)` [🔗<class_StyleBoxFlat_property_shadow_offset>]


- |void| **set_shadow_offset**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_shadow_offset**\ (\ )

The shadow offset in pixels. Adjusts the position of the shadow relatively to the stylebox.


----



[int<class_int>] **shadow_size** = `0` [🔗<class_StyleBoxFlat_property_shadow_size>]


- |void| **set_shadow_size**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_shadow_size**\ (\ )

The shadow size in pixels.


----



[Vector2<class_Vector2>] **skew** = `Vector2(0, 0)` [🔗<class_StyleBoxFlat_property_skew>]


- |void| **set_skew**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_skew**\ (\ )

If set to a non-zero value on either axis, [skew<class_StyleBoxFlat_property_skew>] distorts the StyleBox horizontally and/or vertically. This can be used for "futuristic"-style UIs. Positive values skew the StyleBox towards the right (X axis) and upwards (Y axis), while negative values skew the StyleBox towards the left (X axis) and downwards (Y axis).

\ **Note:** To ensure text does not touch the StyleBox's edges, consider increasing the [StyleBox<class_StyleBox>]'s content margin (see [StyleBox.content_margin_bottom<class_StyleBox_property_content_margin_bottom>]). It is preferable to increase the content margin instead of the expand margin (see [expand_margin_bottom<class_StyleBoxFlat_property_expand_margin_bottom>]), as increasing the expand margin does not increase the size of the clickable area for [Control<class_Control>]\ s.


----


## Method Descriptions



[int<class_int>] **get_border_width**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const| [🔗<class_StyleBoxFlat_method_get_border_width>]

Returns the specified [Side<enum_@GlobalScope_Side>]'s border width.


----



[int<class_int>] **get_border_width_min**\ (\ ) |const| [🔗<class_StyleBoxFlat_method_get_border_width_min>]

Returns the smallest border width out of all four borders.


----



[int<class_int>] **get_corner_radius**\ (\ corner\: [Corner<enum_@GlobalScope_Corner>]\ ) |const| [🔗<class_StyleBoxFlat_method_get_corner_radius>]

Returns the given `corner`'s radius.


----



[float<class_float>] **get_expand_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const| [🔗<class_StyleBoxFlat_method_get_expand_margin>]

Returns the size of the specified [Side<enum_@GlobalScope_Side>]'s expand margin.


----



|void| **set_border_width**\ (\ margin\: [Side<enum_@GlobalScope_Side>], width\: [int<class_int>]\ ) [🔗<class_StyleBoxFlat_method_set_border_width>]

Sets the specified [Side<enum_@GlobalScope_Side>]'s border width to `width` pixels.


----



|void| **set_border_width_all**\ (\ width\: [int<class_int>]\ ) [🔗<class_StyleBoxFlat_method_set_border_width_all>]

Sets the border width to `width` pixels for all sides.


----



|void| **set_corner_radius**\ (\ corner\: [Corner<enum_@GlobalScope_Corner>], radius\: [int<class_int>]\ ) [🔗<class_StyleBoxFlat_method_set_corner_radius>]

Sets the corner radius to `radius` pixels for the given `corner`.


----



|void| **set_corner_radius_all**\ (\ radius\: [int<class_int>]\ ) [🔗<class_StyleBoxFlat_method_set_corner_radius_all>]

Sets the corner radius to `radius` pixels for all corners.


----



|void| **set_expand_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], size\: [float<class_float>]\ ) [🔗<class_StyleBoxFlat_method_set_expand_margin>]

Sets the expand margin to `size` pixels for the specified [Side<enum_@GlobalScope_Side>].


----



|void| **set_expand_margin_all**\ (\ size\: [float<class_float>]\ ) [🔗<class_StyleBoxFlat_method_set_expand_margin_all>]

Sets the expand margin to `size` pixels for all sides.

