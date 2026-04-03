:github_url: hide



# ScrollContainer

**Inherits:** [Container<class_Container>] **<** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [EditorInspector<class_EditorInspector>]

A container used to provide scrollbars to a child control when needed.


## Description

A container used to provide a child control with scrollbars when needed. Scrollbars will automatically be drawn at the right (for vertical) or bottom (for horizontal) and will enable dragging to move the viewable Control (and its children) within the ScrollContainer. Scrollbars will also automatically resize the grabber based on the [Control.custom_minimum_size<class_Control_property_custom_minimum_size>] of the Control relative to the ScrollContainer.


## Tutorials

- [../tutorials/ui/gui_containers](Using Containers .md)


## Properties

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                    | clip_contents                                                                                      | ``true`` (overrides :ref:`Control<class_Control_property_clip_contents>`) |
> +------------------------------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                    | :ref:`draw_focus_border<class_ScrollContainer_property_draw_focus_border>`                         | ``false``                                                                 |
> +------------------------------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                    | :ref:`follow_focus<class_ScrollContainer_property_follow_focus>`                                   | ``false``                                                                 |
> +------------------------------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
> | :ref:`ScrollMode<enum_ScrollContainer_ScrollMode>`         | :ref:`horizontal_scroll_mode<class_ScrollContainer_property_horizontal_scroll_mode>`               | ``1``                                                                     |
> +------------------------------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                      | :ref:`scroll_deadzone<class_ScrollContainer_property_scroll_deadzone>`                             | ``0``                                                                     |
> +------------------------------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
> | :ref:`ScrollHintMode<enum_ScrollContainer_ScrollHintMode>` | :ref:`scroll_hint_mode<class_ScrollContainer_property_scroll_hint_mode>`                           | ``0``                                                                     |
> +------------------------------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                      | :ref:`scroll_horizontal<class_ScrollContainer_property_scroll_horizontal>`                         | ``0``                                                                     |
> +------------------------------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                  | :ref:`scroll_horizontal_custom_step<class_ScrollContainer_property_scroll_horizontal_custom_step>` | ``-1.0``                                                                  |
> +------------------------------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                      | :ref:`scroll_vertical<class_ScrollContainer_property_scroll_vertical>`                             | ``0``                                                                     |
> +------------------------------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                  | :ref:`scroll_vertical_custom_step<class_ScrollContainer_property_scroll_vertical_custom_step>`     | ``-1.0``                                                                  |
> +------------------------------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                    | :ref:`tile_scroll_hint<class_ScrollContainer_property_tile_scroll_hint>`                           | ``false``                                                                 |
> +------------------------------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
> | :ref:`ScrollMode<enum_ScrollContainer_ScrollMode>`         | :ref:`vertical_scroll_mode<class_ScrollContainer_property_vertical_scroll_mode>`                   | ``1``                                                                     |
> +------------------------------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`ensure_control_visible<class_ScrollContainer_method_ensure_control_visible>`\ (\ control\: :ref:`Control<class_Control>`\ ) |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`HScrollBar<class_HScrollBar>` | :ref:`get_h_scroll_bar<class_ScrollContainer_method_get_h_scroll_bar>`\ (\ )                                                      |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`VScrollBar<class_VScrollBar>` | :ref:`get_v_scroll_bar<class_ScrollContainer_method_get_v_scroll_bar>`\ (\ )                                                      |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
>

## Theme Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------+-----------------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>`         | :ref:`scroll_hint_horizontal_color<class_ScrollContainer_theme_color_scroll_hint_horizontal_color>` | ``Color(0, 0, 0, 1)`` |
> +-----------------------------------+-----------------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>`         | :ref:`scroll_hint_vertical_color<class_ScrollContainer_theme_color_scroll_hint_vertical_color>`     | ``Color(0, 0, 0, 1)`` |
> +-----------------------------------+-----------------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`             | :ref:`scrollbar_h_separation<class_ScrollContainer_theme_constant_scrollbar_h_separation>`          | ``0``                 |
> +-----------------------------------+-----------------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`             | :ref:`scrollbar_v_separation<class_ScrollContainer_theme_constant_scrollbar_v_separation>`          | ``0``                 |
> +-----------------------------------+-----------------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`scroll_hint_horizontal<class_ScrollContainer_theme_icon_scroll_hint_horizontal>`              |                       |
> +-----------------------------------+-----------------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`scroll_hint_vertical<class_ScrollContainer_theme_icon_scroll_hint_vertical>`                  |                       |
> +-----------------------------------+-----------------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`StyleBox<class_StyleBox>`   | :ref:`focus<class_ScrollContainer_theme_style_focus>`                                               |                       |
> +-----------------------------------+-----------------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`StyleBox<class_StyleBox>`   | :ref:`panel<class_ScrollContainer_theme_style_panel>`                                               |                       |
> +-----------------------------------+-----------------------------------------------------------------------------------------------------+-----------------------+
>

----


## Signals



**scroll_ended**\ (\ ) [🔗<class_ScrollContainer_signal_scroll_ended>]

Emitted when scrolling stops when dragging the scrollable area *with a touch event*. This signal is *not* emitted when scrolling by dragging the scrollbar, scrolling with the mouse wheel or scrolling with keyboard/gamepad events.

\ **Note:** This signal is only emitted on Android or iOS, or on desktop/web platforms when [ProjectSettings.input_devices/pointing/emulate_touch_from_mouse<class_ProjectSettings_property_input_devices/pointing/emulate_touch_from_mouse>] is enabled.


----



**scroll_started**\ (\ ) [🔗<class_ScrollContainer_signal_scroll_started>]

Emitted when scrolling starts when dragging the scrollable area w\ *ith a touch event*. This signal is *not* emitted when scrolling by dragging the scrollbar, scrolling with the mouse wheel or scrolling with keyboard/gamepad events.

\ **Note:** This signal is only emitted on Android or iOS, or on desktop/web platforms when [ProjectSettings.input_devices/pointing/emulate_touch_from_mouse<class_ProjectSettings_property_input_devices/pointing/emulate_touch_from_mouse>] is enabled.


----


## Enumerations



enum **ScrollMode**: [🔗<enum_ScrollContainer_ScrollMode>]



[ScrollMode<enum_ScrollContainer_ScrollMode>] **SCROLL_MODE_DISABLED** = `0`

Scrolling disabled, scrollbar will be invisible.



[ScrollMode<enum_ScrollContainer_ScrollMode>] **SCROLL_MODE_AUTO** = `1`

Scrolling enabled, scrollbar will be visible only if necessary, i.e. container's content is bigger than the container.



[ScrollMode<enum_ScrollContainer_ScrollMode>] **SCROLL_MODE_SHOW_ALWAYS** = `2`

Scrolling enabled, scrollbar will be always visible.



[ScrollMode<enum_ScrollContainer_ScrollMode>] **SCROLL_MODE_SHOW_NEVER** = `3`

Scrolling enabled, scrollbar will be hidden.



[ScrollMode<enum_ScrollContainer_ScrollMode>] **SCROLL_MODE_RESERVE** = `4`

Combines [SCROLL_MODE_AUTO<class_ScrollContainer_constant_SCROLL_MODE_AUTO>] and [SCROLL_MODE_SHOW_ALWAYS<class_ScrollContainer_constant_SCROLL_MODE_SHOW_ALWAYS>]. The scrollbar is only visible if necessary, but the content size is adjusted as if it was always visible. It's useful for ensuring that content size stays the same regardless if the scrollbar is visible.


----



enum **ScrollHintMode**: [🔗<enum_ScrollContainer_ScrollHintMode>]



[ScrollHintMode<enum_ScrollContainer_ScrollHintMode>] **SCROLL_HINT_MODE_DISABLED** = `0`

Scroll hints will never be shown.



[ScrollHintMode<enum_ScrollContainer_ScrollHintMode>] **SCROLL_HINT_MODE_ALL** = `1`

Scroll hints will be shown at the top and bottom (if vertical), or left and right (if horizontal).



[ScrollHintMode<enum_ScrollContainer_ScrollHintMode>] **SCROLL_HINT_MODE_TOP_AND_LEFT** = `2`

Scroll hints will be shown at the top (if vertical), or the left (if horizontal).



[ScrollHintMode<enum_ScrollContainer_ScrollHintMode>] **SCROLL_HINT_MODE_BOTTOM_AND_RIGHT** = `3`

Scroll hints will be shown at the bottom (if horizontal), or the right (if horizontal).


----


## Property Descriptions



[bool<class_bool>] **draw_focus_border** = `false` [🔗<class_ScrollContainer_property_draw_focus_border>]


- |void| **set_draw_focus_border**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_draw_focus_border**\ (\ )

If `true`, [focus<class_ScrollContainer_theme_style_focus>] is drawn when the ScrollContainer or one of its descendant nodes is focused.


----



[bool<class_bool>] **follow_focus** = `false` [🔗<class_ScrollContainer_property_follow_focus>]


- |void| **set_follow_focus**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_following_focus**\ (\ )

If `true`, the ScrollContainer will automatically scroll to focused children (including indirect children) to make sure they are fully visible.


----



[ScrollMode<enum_ScrollContainer_ScrollMode>] **horizontal_scroll_mode** = `1` [🔗<class_ScrollContainer_property_horizontal_scroll_mode>]


- |void| **set_horizontal_scroll_mode**\ (\ value\: [ScrollMode<enum_ScrollContainer_ScrollMode>]\ )
- [ScrollMode<enum_ScrollContainer_ScrollMode>] **get_horizontal_scroll_mode**\ (\ )

Controls whether horizontal scrollbar can be used and when it should be visible.


----



[int<class_int>] **scroll_deadzone** = `0` [🔗<class_ScrollContainer_property_scroll_deadzone>]


- |void| **set_deadzone**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_deadzone**\ (\ )

Deadzone for touch scrolling. Lower deadzone makes the scrolling more sensitive.


----



[ScrollHintMode<enum_ScrollContainer_ScrollHintMode>] **scroll_hint_mode** = `0` [🔗<class_ScrollContainer_property_scroll_hint_mode>]


- |void| **set_scroll_hint_mode**\ (\ value\: [ScrollHintMode<enum_ScrollContainer_ScrollHintMode>]\ )
- [ScrollHintMode<enum_ScrollContainer_ScrollHintMode>] **get_scroll_hint_mode**\ (\ )

The way which scroll hints (indicators that show that the content can still be scrolled in a certain direction) will be shown.

\ **Note:** Hints won't be shown if the content can be scrolled both vertically and horizontally.


----



[int<class_int>] **scroll_horizontal** = `0` [🔗<class_ScrollContainer_property_scroll_horizontal>]


- |void| **set_h_scroll**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_h_scroll**\ (\ )

The current horizontal scroll value.

\ **Note:** If you are setting this value in the [Node._ready()<class_Node_private_method__ready>] function or earlier, it needs to be wrapped with [Object.set_deferred()<class_Object_method_set_deferred>], since scroll bar's [Range.max_value<class_Range_property_max_value>] is not initialized yet.

::

    func _ready():
        set_deferred("scroll_horizontal", 600)


----



[float<class_float>] **scroll_horizontal_custom_step** = `-1.0` [🔗<class_ScrollContainer_property_scroll_horizontal_custom_step>]


- |void| **set_horizontal_custom_step**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_horizontal_custom_step**\ (\ )

Overrides the [ScrollBar.custom_step<class_ScrollBar_property_custom_step>] used when clicking the internal scroll bar's horizontal increment and decrement buttons or when using arrow keys when the [ScrollBar<class_ScrollBar>] is focused.


----



[int<class_int>] **scroll_vertical** = `0` [🔗<class_ScrollContainer_property_scroll_vertical>]


- |void| **set_v_scroll**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_v_scroll**\ (\ )

The current vertical scroll value.

\ **Note:** Setting it early needs to be deferred, just like in [scroll_horizontal<class_ScrollContainer_property_scroll_horizontal>].

::

    func _ready():
        set_deferred("scroll_vertical", 600)


----



[float<class_float>] **scroll_vertical_custom_step** = `-1.0` [🔗<class_ScrollContainer_property_scroll_vertical_custom_step>]


- |void| **set_vertical_custom_step**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_vertical_custom_step**\ (\ )

Overrides the [ScrollBar.custom_step<class_ScrollBar_property_custom_step>] used when clicking the internal scroll bar's vertical increment and decrement buttons or when using arrow keys when the [ScrollBar<class_ScrollBar>] is focused.


----



[bool<class_bool>] **tile_scroll_hint** = `false` [🔗<class_ScrollContainer_property_tile_scroll_hint>]


- |void| **set_tile_scroll_hint**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_scroll_hint_tiled**\ (\ )

If `true`, the scroll hint texture will be tiled instead of stretched. See [scroll_hint_mode<class_ScrollContainer_property_scroll_hint_mode>].


----



[ScrollMode<enum_ScrollContainer_ScrollMode>] **vertical_scroll_mode** = `1` [🔗<class_ScrollContainer_property_vertical_scroll_mode>]


- |void| **set_vertical_scroll_mode**\ (\ value\: [ScrollMode<enum_ScrollContainer_ScrollMode>]\ )
- [ScrollMode<enum_ScrollContainer_ScrollMode>] **get_vertical_scroll_mode**\ (\ )

Controls whether vertical scrollbar can be used and when it should be visible.


----


## Method Descriptions



|void| **ensure_control_visible**\ (\ control\: [Control<class_Control>]\ ) [🔗<class_ScrollContainer_method_ensure_control_visible>]

Ensures the given `control` is visible (must be a direct or indirect child of the ScrollContainer). Used by [follow_focus<class_ScrollContainer_property_follow_focus>].

\ **Note:** This will not work on a node that was just added during the same frame. If you want to scroll to a newly added child, you must wait until the next frame using [SceneTree.process_frame<class_SceneTree_signal_process_frame>]:

::

    add_child(child_node)
    await get_tree().process_frame
    ensure_control_visible(child_node)


----



[HScrollBar<class_HScrollBar>] **get_h_scroll_bar**\ (\ ) [🔗<class_ScrollContainer_method_get_h_scroll_bar>]

Returns the horizontal scrollbar [HScrollBar<class_HScrollBar>] of this **ScrollContainer**.

\ **Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to disable or hide a scrollbar, you can use [horizontal_scroll_mode<class_ScrollContainer_property_horizontal_scroll_mode>].


----



[VScrollBar<class_VScrollBar>] **get_v_scroll_bar**\ (\ ) [🔗<class_ScrollContainer_method_get_v_scroll_bar>]

Returns the vertical scrollbar [VScrollBar<class_VScrollBar>] of this **ScrollContainer**.

\ **Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to disable or hide a scrollbar, you can use [vertical_scroll_mode<class_ScrollContainer_property_vertical_scroll_mode>].


----


## Theme Property Descriptions



[Color<class_Color>] **scroll_hint_horizontal_color** = `Color(0, 0, 0, 1)` [🔗<class_ScrollContainer_theme_color_scroll_hint_horizontal_color>]

[Color<class_Color>] used to modulate the [scroll_hint_horizontal<class_ScrollContainer_theme_icon_scroll_hint_horizontal>] texture.


----



[Color<class_Color>] **scroll_hint_vertical_color** = `Color(0, 0, 0, 1)` [🔗<class_ScrollContainer_theme_color_scroll_hint_vertical_color>]

[Color<class_Color>] used to modulate the [scroll_hint_vertical<class_ScrollContainer_theme_icon_scroll_hint_vertical>] texture.


----



[int<class_int>] **scrollbar_h_separation** = `0` [🔗<class_ScrollContainer_theme_constant_scrollbar_h_separation>]

The space between the ScrollContainer's vertical scroll bar and its content, in pixels. No space will be added when the content's minimum size is larger than the ScrollContainer's size.


----



[int<class_int>] **scrollbar_v_separation** = `0` [🔗<class_ScrollContainer_theme_constant_scrollbar_v_separation>]

The space between the ScrollContainer's horizontal scroll bar and its content, in pixels. No space will be added when the content's minimum size is larger than the ScrollContainer's size.


----



[Texture2D<class_Texture2D>] **scroll_hint_horizontal** [🔗<class_ScrollContainer_theme_icon_scroll_hint_horizontal>]

The indicator that will be shown when the content can still be scrolled horizontally. See [scroll_hint_mode<class_ScrollContainer_property_scroll_hint_mode>].


----



[Texture2D<class_Texture2D>] **scroll_hint_vertical** [🔗<class_ScrollContainer_theme_icon_scroll_hint_vertical>]

The indicator that will be shown when the content can still be scrolled vertically. See [scroll_hint_mode<class_ScrollContainer_property_scroll_hint_mode>].


----



[StyleBox<class_StyleBox>] **focus** [🔗<class_ScrollContainer_theme_style_focus>]

The focus border [StyleBox<class_StyleBox>] of the **ScrollContainer**. Only used if [draw_focus_border<class_ScrollContainer_property_draw_focus_border>] is `true`.


----



[StyleBox<class_StyleBox>] **panel** [🔗<class_ScrollContainer_theme_style_panel>]

The background [StyleBox<class_StyleBox>] of the **ScrollContainer**.

