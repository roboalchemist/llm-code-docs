:github_url: hide



# NinePatchRect

**Inherits:** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A control that displays a texture by keeping its corners intact, but tiling its edges and center.


## Description

Also known as 9-slice panels, **NinePatchRect** produces clean panels of any size based on a small texture. To do so, it splits the texture in a 3×3 grid. When you scale the node, it tiles the texture's edges horizontally or vertically, tiles the center on both axes, and leaves the corners unchanged.


## Properties

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
> | :ref:`AxisStretchMode<enum_NinePatchRect_AxisStretchMode>` | :ref:`axis_stretch_horizontal<class_NinePatchRect_property_axis_stretch_horizontal>` | ``0``                                                                 |
> +------------------------------------------------------------+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
> | :ref:`AxisStretchMode<enum_NinePatchRect_AxisStretchMode>` | :ref:`axis_stretch_vertical<class_NinePatchRect_property_axis_stretch_vertical>`     | ``0``                                                                 |
> +------------------------------------------------------------+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                    | :ref:`draw_center<class_NinePatchRect_property_draw_center>`                         | ``true``                                                              |
> +------------------------------------------------------------+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
> | :ref:`MouseFilter<enum_Control_MouseFilter>`               | mouse_filter                                                                         | ``2`` (overrides :ref:`Control<class_Control_property_mouse_filter>`) |
> +------------------------------------------------------------+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
> | :ref:`int<class_int>`                                      | :ref:`patch_margin_bottom<class_NinePatchRect_property_patch_margin_bottom>`         | ``0``                                                                 |
> +------------------------------------------------------------+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
> | :ref:`int<class_int>`                                      | :ref:`patch_margin_left<class_NinePatchRect_property_patch_margin_left>`             | ``0``                                                                 |
> +------------------------------------------------------------+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
> | :ref:`int<class_int>`                                      | :ref:`patch_margin_right<class_NinePatchRect_property_patch_margin_right>`           | ``0``                                                                 |
> +------------------------------------------------------------+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
> | :ref:`int<class_int>`                                      | :ref:`patch_margin_top<class_NinePatchRect_property_patch_margin_top>`               | ``0``                                                                 |
> +------------------------------------------------------------+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
> | :ref:`Rect2<class_Rect2>`                                  | :ref:`region_rect<class_NinePatchRect_property_region_rect>`                         | ``Rect2(0, 0, 0, 0)``                                                 |
> +------------------------------------------------------------+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
> | :ref:`Texture2D<class_Texture2D>`                          | :ref:`texture<class_NinePatchRect_property_texture>`                                 |                                                                       |
> +------------------------------------------------------------+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>` | :ref:`get_patch_margin<class_NinePatchRect_method_get_patch_margin>`\ (\ margin\: :ref:`Side<enum_@GlobalScope_Side>`\ ) |const|                        |
> +-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                | :ref:`set_patch_margin<class_NinePatchRect_method_set_patch_margin>`\ (\ margin\: :ref:`Side<enum_@GlobalScope_Side>`, value\: :ref:`int<class_int>`\ ) |
> +-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**texture_changed**\ (\ ) [🔗<class_NinePatchRect_signal_texture_changed>]

Emitted when the node's texture changes.


----


## Enumerations



enum **AxisStretchMode**: [🔗<enum_NinePatchRect_AxisStretchMode>]



[AxisStretchMode<enum_NinePatchRect_AxisStretchMode>] **AXIS_STRETCH_MODE_STRETCH** = `0`

Stretches the center texture across the NinePatchRect. This may cause the texture to be distorted.



[AxisStretchMode<enum_NinePatchRect_AxisStretchMode>] **AXIS_STRETCH_MODE_TILE** = `1`

Repeats the center texture across the NinePatchRect. This won't cause any visible distortion. The texture must be seamless for this to work without displaying artifacts between edges.



[AxisStretchMode<enum_NinePatchRect_AxisStretchMode>] **AXIS_STRETCH_MODE_TILE_FIT** = `2`

Repeats the center texture across the NinePatchRect, but will also stretch the texture to make sure each tile is visible in full. This may cause the texture to be distorted, but less than [AXIS_STRETCH_MODE_STRETCH<class_NinePatchRect_constant_AXIS_STRETCH_MODE_STRETCH>]. The texture must be seamless for this to work without displaying artifacts between edges.


----


## Property Descriptions



[AxisStretchMode<enum_NinePatchRect_AxisStretchMode>] **axis_stretch_horizontal** = `0` [🔗<class_NinePatchRect_property_axis_stretch_horizontal>]


- |void| **set_h_axis_stretch_mode**\ (\ value\: [AxisStretchMode<enum_NinePatchRect_AxisStretchMode>]\ )
- [AxisStretchMode<enum_NinePatchRect_AxisStretchMode>] **get_h_axis_stretch_mode**\ (\ )

The stretch mode to use for horizontal stretching/tiling.


----



[AxisStretchMode<enum_NinePatchRect_AxisStretchMode>] **axis_stretch_vertical** = `0` [🔗<class_NinePatchRect_property_axis_stretch_vertical>]


- |void| **set_v_axis_stretch_mode**\ (\ value\: [AxisStretchMode<enum_NinePatchRect_AxisStretchMode>]\ )
- [AxisStretchMode<enum_NinePatchRect_AxisStretchMode>] **get_v_axis_stretch_mode**\ (\ )

The stretch mode to use for vertical stretching/tiling.


----



[bool<class_bool>] **draw_center** = `true` [🔗<class_NinePatchRect_property_draw_center>]


- |void| **set_draw_center**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_draw_center_enabled**\ (\ )

If `true`, draw the panel's center. Else, only draw the 9-slice's borders.


----



[int<class_int>] **patch_margin_bottom** = `0` [🔗<class_NinePatchRect_property_patch_margin_bottom>]


- |void| **set_patch_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], value\: [int<class_int>]\ )
- [int<class_int>] **get_patch_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

The height of the 9-slice's bottom row. A margin of 16 means the 9-slice's bottom corners and side will have a height of 16 pixels. You can set all 4 margin values individually to create panels with non-uniform borders.


----



[int<class_int>] **patch_margin_left** = `0` [🔗<class_NinePatchRect_property_patch_margin_left>]


- |void| **set_patch_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], value\: [int<class_int>]\ )
- [int<class_int>] **get_patch_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

The width of the 9-slice's left column. A margin of 16 means the 9-slice's left corners and side will have a width of 16 pixels. You can set all 4 margin values individually to create panels with non-uniform borders.


----



[int<class_int>] **patch_margin_right** = `0` [🔗<class_NinePatchRect_property_patch_margin_right>]


- |void| **set_patch_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], value\: [int<class_int>]\ )
- [int<class_int>] **get_patch_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

The width of the 9-slice's right column. A margin of 16 means the 9-slice's right corners and side will have a width of 16 pixels. You can set all 4 margin values individually to create panels with non-uniform borders.


----



[int<class_int>] **patch_margin_top** = `0` [🔗<class_NinePatchRect_property_patch_margin_top>]


- |void| **set_patch_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], value\: [int<class_int>]\ )
- [int<class_int>] **get_patch_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

The height of the 9-slice's top row. A margin of 16 means the 9-slice's top corners and side will have a height of 16 pixels. You can set all 4 margin values individually to create panels with non-uniform borders.


----



[Rect2<class_Rect2>] **region_rect** = `Rect2(0, 0, 0, 0)` [🔗<class_NinePatchRect_property_region_rect>]


- |void| **set_region_rect**\ (\ value\: [Rect2<class_Rect2>]\ )
- [Rect2<class_Rect2>] **get_region_rect**\ (\ )

Rectangular region of the texture to sample from. If you're working with an atlas, use this property to define the area the 9-slice should use. All other properties are relative to this one. If the rect is empty, NinePatchRect will use the whole texture.


----



[Texture2D<class_Texture2D>] **texture** [🔗<class_NinePatchRect_property_texture>]


- |void| **set_texture**\ (\ value\: [Texture2D<class_Texture2D>]\ )
- [Texture2D<class_Texture2D>] **get_texture**\ (\ )

The node's texture resource.


----


## Method Descriptions



[int<class_int>] **get_patch_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const| [🔗<class_NinePatchRect_method_get_patch_margin>]

Returns the size of the margin on the specified [Side<enum_@GlobalScope_Side>].


----



|void| **set_patch_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], value\: [int<class_int>]\ ) [🔗<class_NinePatchRect_method_set_patch_margin>]

Sets the size of the margin on the specified [Side<enum_@GlobalScope_Side>] to `value` pixels.

