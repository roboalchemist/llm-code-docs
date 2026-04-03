:github_url: hide



# ScrollBar

**Inherits:** [Range<class_Range>] **<** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [HScrollBar<class_HScrollBar>], [VScrollBar<class_VScrollBar>]

Abstract base class for scrollbars.


## Description

Abstract base class for scrollbars, typically used to navigate through content that extends beyond the visible area of a control. Scrollbars are [Range<class_Range>]-based controls.


## Properties

> **TABLE**
> :widths: auto
>
> +------------------------------------------+----------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`float<class_float>`                | :ref:`custom_step<class_ScrollBar_property_custom_step>` | ``-1.0``                                                            |
> +------------------------------------------+----------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`FocusMode<enum_Control_FocusMode>` | focus_mode                                               | ``3`` (overrides :ref:`Control<class_Control_property_focus_mode>`) |
> +------------------------------------------+----------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`float<class_float>`                | step                                                     | ``0.0`` (overrides :ref:`Range<class_Range_property_step>`)         |
> +------------------------------------------+----------------------------------------------------------+---------------------------------------------------------------------+
>

## Theme Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------+----------------------------------------------------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`decrement<class_ScrollBar_theme_icon_decrement>`                     |
> +-----------------------------------+----------------------------------------------------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`decrement_highlight<class_ScrollBar_theme_icon_decrement_highlight>` |
> +-----------------------------------+----------------------------------------------------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`decrement_pressed<class_ScrollBar_theme_icon_decrement_pressed>`     |
> +-----------------------------------+----------------------------------------------------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`increment<class_ScrollBar_theme_icon_increment>`                     |
> +-----------------------------------+----------------------------------------------------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`increment_highlight<class_ScrollBar_theme_icon_increment_highlight>` |
> +-----------------------------------+----------------------------------------------------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`increment_pressed<class_ScrollBar_theme_icon_increment_pressed>`     |
> +-----------------------------------+----------------------------------------------------------------------------+
> | :ref:`StyleBox<class_StyleBox>`   | :ref:`grabber<class_ScrollBar_theme_style_grabber>`                        |
> +-----------------------------------+----------------------------------------------------------------------------+
> | :ref:`StyleBox<class_StyleBox>`   | :ref:`grabber_highlight<class_ScrollBar_theme_style_grabber_highlight>`    |
> +-----------------------------------+----------------------------------------------------------------------------+
> | :ref:`StyleBox<class_StyleBox>`   | :ref:`grabber_pressed<class_ScrollBar_theme_style_grabber_pressed>`        |
> +-----------------------------------+----------------------------------------------------------------------------+
> | :ref:`StyleBox<class_StyleBox>`   | :ref:`scroll<class_ScrollBar_theme_style_scroll>`                          |
> +-----------------------------------+----------------------------------------------------------------------------+
> | :ref:`StyleBox<class_StyleBox>`   | :ref:`scroll_focus<class_ScrollBar_theme_style_scroll_focus>`              |
> +-----------------------------------+----------------------------------------------------------------------------+
>

----


## Signals



**scrolling**\ (\ ) [🔗<class_ScrollBar_signal_scrolling>]

Emitted when the scrollbar is being scrolled.


----


## Property Descriptions



[float<class_float>] **custom_step** = `-1.0` [🔗<class_ScrollBar_property_custom_step>]


- |void| **set_custom_step**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_custom_step**\ (\ )

Overrides the step used when clicking increment and decrement buttons or when using arrow keys when the **ScrollBar** is focused.


----


## Theme Property Descriptions



[Texture2D<class_Texture2D>] **decrement** [🔗<class_ScrollBar_theme_icon_decrement>]

Icon used as a button to scroll the **ScrollBar** left/up. Supports custom step using the [custom_step<class_ScrollBar_property_custom_step>] property.


----



[Texture2D<class_Texture2D>] **decrement_highlight** [🔗<class_ScrollBar_theme_icon_decrement_highlight>]

Displayed when the mouse cursor hovers over the decrement button.


----



[Texture2D<class_Texture2D>] **decrement_pressed** [🔗<class_ScrollBar_theme_icon_decrement_pressed>]

Displayed when the decrement button is being pressed.


----



[Texture2D<class_Texture2D>] **increment** [🔗<class_ScrollBar_theme_icon_increment>]

Icon used as a button to scroll the **ScrollBar** right/down. Supports custom step using the [custom_step<class_ScrollBar_property_custom_step>] property.


----



[Texture2D<class_Texture2D>] **increment_highlight** [🔗<class_ScrollBar_theme_icon_increment_highlight>]

Displayed when the mouse cursor hovers over the increment button.


----



[Texture2D<class_Texture2D>] **increment_pressed** [🔗<class_ScrollBar_theme_icon_increment_pressed>]

Displayed when the increment button is being pressed.


----



[StyleBox<class_StyleBox>] **grabber** [🔗<class_ScrollBar_theme_style_grabber>]

Used as texture for the grabber, the draggable element representing current scroll.


----



[StyleBox<class_StyleBox>] **grabber_highlight** [🔗<class_ScrollBar_theme_style_grabber_highlight>]

Used when the mouse hovers over the grabber.


----



[StyleBox<class_StyleBox>] **grabber_pressed** [🔗<class_ScrollBar_theme_style_grabber_pressed>]

Used when the grabber is being dragged.


----



[StyleBox<class_StyleBox>] **scroll** [🔗<class_ScrollBar_theme_style_scroll>]

Used as background of this **ScrollBar**.


----



[StyleBox<class_StyleBox>] **scroll_focus** [🔗<class_ScrollBar_theme_style_scroll_focus>]

Used as background when the **ScrollBar** has the GUI focus.

