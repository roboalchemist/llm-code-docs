:github_url: hide



# Slider

**Inherits:** [Range<class_Range>] **<** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [HSlider<class_HSlider>], [VSlider<class_VSlider>]

Abstract base class for sliders.


## Description

Abstract base class for sliders, used to adjust a value by moving a grabber along a horizontal or vertical axis. Sliders are [Range<class_Range>]-based controls.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------+-----------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                       | :ref:`editable<class_Slider_property_editable>`                 | ``true``                                                            |
> +-----------------------------------------------+-----------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`FocusMode<enum_Control_FocusMode>`      | focus_mode                                                      | ``2`` (overrides :ref:`Control<class_Control_property_focus_mode>`) |
> +-----------------------------------------------+-----------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                       | :ref:`scrollable<class_Slider_property_scrollable>`             | ``true``                                                            |
> +-----------------------------------------------+-----------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`float<class_float>`                     | step                                                            | ``1.0`` (overrides :ref:`Range<class_Range_property_step>`)         |
> +-----------------------------------------------+-----------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`int<class_int>`                         | :ref:`tick_count<class_Slider_property_tick_count>`             | ``0``                                                               |
> +-----------------------------------------------+-----------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                       | :ref:`ticks_on_borders<class_Slider_property_ticks_on_borders>` | ``false``                                                           |
> +-----------------------------------------------+-----------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`TickPosition<enum_Slider_TickPosition>` | :ref:`ticks_position<class_Slider_property_ticks_position>`     | ``0``                                                               |
> +-----------------------------------------------+-----------------------------------------------------------------+---------------------------------------------------------------------+
>

## Theme Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------+--------------------------------------------------------------------------------+-------+
> | :ref:`int<class_int>`             | :ref:`center_grabber<class_Slider_theme_constant_center_grabber>`              | ``0`` |
> +-----------------------------------+--------------------------------------------------------------------------------+-------+
> | :ref:`int<class_int>`             | :ref:`grabber_offset<class_Slider_theme_constant_grabber_offset>`              | ``0`` |
> +-----------------------------------+--------------------------------------------------------------------------------+-------+
> | :ref:`int<class_int>`             | :ref:`tick_offset<class_Slider_theme_constant_tick_offset>`                    | ``0`` |
> +-----------------------------------+--------------------------------------------------------------------------------+-------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`grabber<class_Slider_theme_icon_grabber>`                                |       |
> +-----------------------------------+--------------------------------------------------------------------------------+-------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`grabber_disabled<class_Slider_theme_icon_grabber_disabled>`              |       |
> +-----------------------------------+--------------------------------------------------------------------------------+-------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`grabber_highlight<class_Slider_theme_icon_grabber_highlight>`            |       |
> +-----------------------------------+--------------------------------------------------------------------------------+-------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`tick<class_Slider_theme_icon_tick>`                                      |       |
> +-----------------------------------+--------------------------------------------------------------------------------+-------+
> | :ref:`StyleBox<class_StyleBox>`   | :ref:`grabber_area<class_Slider_theme_style_grabber_area>`                     |       |
> +-----------------------------------+--------------------------------------------------------------------------------+-------+
> | :ref:`StyleBox<class_StyleBox>`   | :ref:`grabber_area_highlight<class_Slider_theme_style_grabber_area_highlight>` |       |
> +-----------------------------------+--------------------------------------------------------------------------------+-------+
> | :ref:`StyleBox<class_StyleBox>`   | :ref:`slider<class_Slider_theme_style_slider>`                                 |       |
> +-----------------------------------+--------------------------------------------------------------------------------+-------+
>

----


## Signals



**drag_ended**\ (\ value_changed\: [bool<class_bool>]\ ) [🔗<class_Slider_signal_drag_ended>]

Emitted when the grabber stops being dragged. If `value_changed` is `true`, [Range.value<class_Range_property_value>] is different from the value when the dragging was started.


----



**drag_started**\ (\ ) [🔗<class_Slider_signal_drag_started>]

Emitted when the grabber starts being dragged. This is emitted before the corresponding [Range.value_changed<class_Range_signal_value_changed>] signal.


----


## Enumerations



enum **TickPosition**: [🔗<enum_Slider_TickPosition>]



[TickPosition<enum_Slider_TickPosition>] **TICK_POSITION_BOTTOM_RIGHT** = `0`

Places the ticks at the bottom of the [HSlider<class_HSlider>], or right of the [VSlider<class_VSlider>].



[TickPosition<enum_Slider_TickPosition>] **TICK_POSITION_TOP_LEFT** = `1`

Places the ticks at the top of the [HSlider<class_HSlider>], or left of the [VSlider<class_VSlider>].



[TickPosition<enum_Slider_TickPosition>] **TICK_POSITION_BOTH** = `2`

Places the ticks at the both sides of the slider.



[TickPosition<enum_Slider_TickPosition>] **TICK_POSITION_CENTER** = `3`

Places the ticks at the center of the slider.


----


## Property Descriptions



[bool<class_bool>] **editable** = `true` [🔗<class_Slider_property_editable>]


- |void| **set_editable**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_editable**\ (\ )

If `true`, the slider can be interacted with. If `false`, the value can be changed only by code.


----



[bool<class_bool>] **scrollable** = `true` [🔗<class_Slider_property_scrollable>]


- |void| **set_scrollable**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_scrollable**\ (\ )

If `true`, the value can be changed using the mouse wheel.


----



[int<class_int>] **tick_count** = `0` [🔗<class_Slider_property_tick_count>]


- |void| **set_ticks**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_ticks**\ (\ )

Number of ticks displayed on the slider, including border ticks. Ticks are uniformly-distributed value markers.


----



[bool<class_bool>] **ticks_on_borders** = `false` [🔗<class_Slider_property_ticks_on_borders>]


- |void| **set_ticks_on_borders**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_ticks_on_borders**\ (\ )

If `true`, the slider will display ticks for minimum and maximum values.


----



[TickPosition<enum_Slider_TickPosition>] **ticks_position** = `0` [🔗<class_Slider_property_ticks_position>]


- |void| **set_ticks_position**\ (\ value\: [TickPosition<enum_Slider_TickPosition>]\ )
- [TickPosition<enum_Slider_TickPosition>] **get_ticks_position**\ (\ )

Sets the position of the ticks. See [TickPosition<enum_Slider_TickPosition>] for details.


----


## Theme Property Descriptions



[int<class_int>] **center_grabber** = `0` [🔗<class_Slider_theme_constant_center_grabber>]

Boolean constant. If `1`, the grabber texture size will be ignored and it will fit within slider's bounds based only on its center position.


----



[int<class_int>] **grabber_offset** = `0` [🔗<class_Slider_theme_constant_grabber_offset>]

Vertical or horizontal offset of the grabber.


----



[int<class_int>] **tick_offset** = `0` [🔗<class_Slider_theme_constant_tick_offset>]

Vertical or horizontal offset of the ticks. The offset is reversed for top or left ticks.


----



[Texture2D<class_Texture2D>] **grabber** [🔗<class_Slider_theme_icon_grabber>]

The texture for the grabber (the draggable element).


----



[Texture2D<class_Texture2D>] **grabber_disabled** [🔗<class_Slider_theme_icon_grabber_disabled>]

The texture for the grabber when it's disabled.


----



[Texture2D<class_Texture2D>] **grabber_highlight** [🔗<class_Slider_theme_icon_grabber_highlight>]

The texture for the grabber when it's focused.


----



[Texture2D<class_Texture2D>] **tick** [🔗<class_Slider_theme_icon_tick>]

The texture for the ticks, visible when [tick_count<class_Slider_property_tick_count>] is greater than 0.


----



[StyleBox<class_StyleBox>] **grabber_area** [🔗<class_Slider_theme_style_grabber_area>]

The background of the area to the left or bottom of the grabber.


----



[StyleBox<class_StyleBox>] **grabber_area_highlight** [🔗<class_Slider_theme_style_grabber_area_highlight>]

The background of the area to the left or bottom of the grabber that displays when it's being hovered or focused.


----



[StyleBox<class_StyleBox>] **slider** [🔗<class_Slider_theme_style_slider>]

The background for the whole slider. Affects the height or width of the [grabber_area<class_Slider_theme_style_grabber_area>].

