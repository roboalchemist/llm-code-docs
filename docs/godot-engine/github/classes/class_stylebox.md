:github_url: hide



# StyleBox

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [StyleBoxEmpty<class_StyleBoxEmpty>], [StyleBoxFlat<class_StyleBoxFlat>], [StyleBoxLine<class_StyleBoxLine>], [StyleBoxTexture<class_StyleBoxTexture>]

Abstract base class for defining stylized boxes for UI elements.


## Description

**StyleBox** is an abstract base class for drawing stylized boxes for UI elements. It is used for panels, buttons, [LineEdit<class_LineEdit>] backgrounds, [Tree<class_Tree>] backgrounds, etc. and also for testing a transparency mask for pointer signals. If mask test fails on a **StyleBox** assigned as mask to a control, clicks and motion signals will go through it to the one below.

\ **Note:** For control nodes that have *Theme Properties*, the `focus` **StyleBox** is displayed over the `normal`, `hover` or `pressed` **StyleBox**. This makes the `focus` **StyleBox** more reusable across different nodes.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+-----------------------------------------------------------------------------+----------+
> | :ref:`float<class_float>` | :ref:`content_margin_bottom<class_StyleBox_property_content_margin_bottom>` | ``-1.0`` |
> +---------------------------+-----------------------------------------------------------------------------+----------+
> | :ref:`float<class_float>` | :ref:`content_margin_left<class_StyleBox_property_content_margin_left>`     | ``-1.0`` |
> +---------------------------+-----------------------------------------------------------------------------+----------+
> | :ref:`float<class_float>` | :ref:`content_margin_right<class_StyleBox_property_content_margin_right>`   | ``-1.0`` |
> +---------------------------+-----------------------------------------------------------------------------+----------+
> | :ref:`float<class_float>` | :ref:`content_margin_top<class_StyleBox_property_content_margin_top>`       | ``-1.0`` |
> +---------------------------+-----------------------------------------------------------------------------+----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`_draw<class_StyleBox_private_method__draw>`\ (\ to_canvas_item\: :ref:`RID<class_RID>`, rect\: :ref:`Rect2<class_Rect2>`\ ) |virtual| |required| |const| |
> +-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2<class_Rect2>`           | :ref:`_get_draw_rect<class_StyleBox_private_method__get_draw_rect>`\ (\ rect\: :ref:`Rect2<class_Rect2>`\ ) |virtual| |const|                                  |
> +-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`       | :ref:`_get_minimum_size<class_StyleBox_private_method__get_minimum_size>`\ (\ ) |virtual| |const|                                                              |
> +-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`_test_mask<class_StyleBox_private_method__test_mask>`\ (\ point\: :ref:`Vector2<class_Vector2>`, rect\: :ref:`Rect2<class_Rect2>`\ ) |virtual| |const|   |
> +-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`draw<class_StyleBox_method_draw>`\ (\ canvas_item\: :ref:`RID<class_RID>`, rect\: :ref:`Rect2<class_Rect2>`\ ) |const|                                   |
> +-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`           | :ref:`get_content_margin<class_StyleBox_method_get_content_margin>`\ (\ margin\: :ref:`Side<enum_@GlobalScope_Side>`\ ) |const|                                |
> +-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`CanvasItem<class_CanvasItem>` | :ref:`get_current_item_drawn<class_StyleBox_method_get_current_item_drawn>`\ (\ ) |const|                                                                      |
> +-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`           | :ref:`get_margin<class_StyleBox_method_get_margin>`\ (\ margin\: :ref:`Side<enum_@GlobalScope_Side>`\ ) |const|                                                |
> +-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`       | :ref:`get_minimum_size<class_StyleBox_method_get_minimum_size>`\ (\ ) |const|                                                                                  |
> +-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`       | :ref:`get_offset<class_StyleBox_method_get_offset>`\ (\ ) |const|                                                                                              |
> +-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`set_content_margin<class_StyleBox_method_set_content_margin>`\ (\ margin\: :ref:`Side<enum_@GlobalScope_Side>`, offset\: :ref:`float<class_float>`\ )    |
> +-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`set_content_margin_all<class_StyleBox_method_set_content_margin_all>`\ (\ offset\: :ref:`float<class_float>`\ )                                          |
> +-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`test_mask<class_StyleBox_method_test_mask>`\ (\ point\: :ref:`Vector2<class_Vector2>`, rect\: :ref:`Rect2<class_Rect2>`\ ) |const|                       |
> +-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[float<class_float>] **content_margin_bottom** = `-1.0` [🔗<class_StyleBox_property_content_margin_bottom>]


- |void| **set_content_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], offset\: [float<class_float>]\ )
- [float<class_float>] **get_content_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

The bottom margin for the contents of this style box. Increasing this value reduces the space available to the contents from the bottom.

If this value is negative, it is ignored and a child-specific margin is used instead. For example, for [StyleBoxFlat<class_StyleBoxFlat>], the border thickness (if any) is used instead.

It is up to the code using this style box to decide what these contents are: for example, a [Button<class_Button>] respects this content margin for the textual contents of the button.

\ [get_margin()<class_StyleBox_method_get_margin>] should be used to fetch this value as consumer instead of reading these properties directly. This is because it correctly respects negative values and the fallback mentioned above.


----



[float<class_float>] **content_margin_left** = `-1.0` [🔗<class_StyleBox_property_content_margin_left>]


- |void| **set_content_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], offset\: [float<class_float>]\ )
- [float<class_float>] **get_content_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

The left margin for the contents of this style box. Increasing this value reduces the space available to the contents from the left.

Refer to [content_margin_bottom<class_StyleBox_property_content_margin_bottom>] for extra considerations.


----



[float<class_float>] **content_margin_right** = `-1.0` [🔗<class_StyleBox_property_content_margin_right>]


- |void| **set_content_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], offset\: [float<class_float>]\ )
- [float<class_float>] **get_content_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

The right margin for the contents of this style box. Increasing this value reduces the space available to the contents from the right.

Refer to [content_margin_bottom<class_StyleBox_property_content_margin_bottom>] for extra considerations.


----



[float<class_float>] **content_margin_top** = `-1.0` [🔗<class_StyleBox_property_content_margin_top>]


- |void| **set_content_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], offset\: [float<class_float>]\ )
- [float<class_float>] **get_content_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const|

The top margin for the contents of this style box. Increasing this value reduces the space available to the contents from the top.

Refer to [content_margin_bottom<class_StyleBox_property_content_margin_bottom>] for extra considerations.


----


## Method Descriptions



|void| **_draw**\ (\ to_canvas_item\: [RID<class_RID>], rect\: [Rect2<class_Rect2>]\ ) |virtual| |required| |const| [🔗<class_StyleBox_private_method__draw>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Rect2<class_Rect2>] **_get_draw_rect**\ (\ rect\: [Rect2<class_Rect2>]\ ) |virtual| |const| [🔗<class_StyleBox_private_method__get_draw_rect>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Vector2<class_Vector2>] **_get_minimum_size**\ (\ ) |virtual| |const| [🔗<class_StyleBox_private_method__get_minimum_size>]

Virtual method to be implemented by the user. Returns a custom minimum size that the stylebox must respect when drawing. By default [get_minimum_size()<class_StyleBox_method_get_minimum_size>] only takes content margins into account. This method can be overridden to add another size restriction. A combination of the default behavior and the output of this method will be used, to account for both sizes.


----



[bool<class_bool>] **_test_mask**\ (\ point\: [Vector2<class_Vector2>], rect\: [Rect2<class_Rect2>]\ ) |virtual| |const| [🔗<class_StyleBox_private_method__test_mask>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **draw**\ (\ canvas_item\: [RID<class_RID>], rect\: [Rect2<class_Rect2>]\ ) |const| [🔗<class_StyleBox_method_draw>]

Draws this stylebox using a canvas item identified by the given [RID<class_RID>].

The [RID<class_RID>] value can either be the result of [CanvasItem.get_canvas_item()<class_CanvasItem_method_get_canvas_item>] called on an existing [CanvasItem<class_CanvasItem>]-derived node, or directly from creating a canvas item in the [RenderingServer<class_RenderingServer>] with [RenderingServer.canvas_item_create()<class_RenderingServer_method_canvas_item_create>].


----



[float<class_float>] **get_content_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const| [🔗<class_StyleBox_method_get_content_margin>]

Returns the default margin of the specified [Side<enum_@GlobalScope_Side>].


----



[CanvasItem<class_CanvasItem>] **get_current_item_drawn**\ (\ ) |const| [🔗<class_StyleBox_method_get_current_item_drawn>]

Returns the [CanvasItem<class_CanvasItem>] that handles its [CanvasItem.NOTIFICATION_DRAW<class_CanvasItem_constant_NOTIFICATION_DRAW>] or [CanvasItem._draw()<class_CanvasItem_private_method__draw>] callback at this moment.


----



[float<class_float>] **get_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>]\ ) |const| [🔗<class_StyleBox_method_get_margin>]

Returns the content margin offset for the specified [Side<enum_@GlobalScope_Side>].

Positive values reduce size inwards, unlike [Control<class_Control>]'s margin values.


----



[Vector2<class_Vector2>] **get_minimum_size**\ (\ ) |const| [🔗<class_StyleBox_method_get_minimum_size>]

Returns the minimum size that this stylebox can be shrunk to.


----



[Vector2<class_Vector2>] **get_offset**\ (\ ) |const| [🔗<class_StyleBox_method_get_offset>]

Returns the "offset" of a stylebox. This helper function returns a value equivalent to `Vector2(style.get_margin(MARGIN_LEFT), style.get_margin(MARGIN_TOP))`.


----



|void| **set_content_margin**\ (\ margin\: [Side<enum_@GlobalScope_Side>], offset\: [float<class_float>]\ ) [🔗<class_StyleBox_method_set_content_margin>]

Sets the default value of the specified [Side<enum_@GlobalScope_Side>] to `offset` pixels.


----



|void| **set_content_margin_all**\ (\ offset\: [float<class_float>]\ ) [🔗<class_StyleBox_method_set_content_margin_all>]

Sets the default margin to `offset` pixels for all sides.


----



[bool<class_bool>] **test_mask**\ (\ point\: [Vector2<class_Vector2>], rect\: [Rect2<class_Rect2>]\ ) |const| [🔗<class_StyleBox_method_test_mask>]

Test a position in a rectangle, return whether it passes the mask test.

