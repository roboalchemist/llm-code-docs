:github_url: hide



# VScrollBar

**Inherits:** [ScrollBar<class_ScrollBar>] **<** [Range<class_Range>] **<** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A vertical scrollbar that goes from top (min) to bottom (max).


## Description

A vertical scrollbar, typically used to navigate through content that extends beyond the visible height of a control. It is a [Range<class_Range>]-based control and goes from top (min) to bottom (max). Note that this direction is the opposite of [VSlider<class_VSlider>]'s.


## Properties

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------+-----------------------+--------------------------------------------------------------------------------+
> | |bitfield|\[:ref:`SizeFlags<enum_Control_SizeFlags>`\] | size_flags_horizontal | ``0`` (overrides :ref:`Control<class_Control_property_size_flags_horizontal>`) |
> +--------------------------------------------------------+-----------------------+--------------------------------------------------------------------------------+
> | |bitfield|\[:ref:`SizeFlags<enum_Control_SizeFlags>`\] | size_flags_vertical   | ``1`` (overrides :ref:`Control<class_Control_property_size_flags_vertical>`)   |
> +--------------------------------------------------------+-----------------------+--------------------------------------------------------------------------------+
>

## Theme Properties

> **TABLE**
> :widths: auto
>
> +-----------------------+---------------------------------------------------------------------+-------+
> | :ref:`int<class_int>` | :ref:`padding_left<class_VScrollBar_theme_constant_padding_left>`   | ``0`` |
> +-----------------------+---------------------------------------------------------------------+-------+
> | :ref:`int<class_int>` | :ref:`padding_right<class_VScrollBar_theme_constant_padding_right>` | ``0`` |
> +-----------------------+---------------------------------------------------------------------+-------+
>

----


## Theme Property Descriptions



[int<class_int>] **padding_left** = `0` [🔗<class_VScrollBar_theme_constant_padding_left>]

Padding between the left of the [ScrollBar.scroll<class_ScrollBar_theme_style_scroll>] element and the [ScrollBar.grabber<class_ScrollBar_theme_style_grabber>].

\ **Note:** To apply vertical padding, modify the top/bottom content margins of [ScrollBar.scroll<class_ScrollBar_theme_style_scroll>] instead.


----



[int<class_int>] **padding_right** = `0` [🔗<class_VScrollBar_theme_constant_padding_right>]

Padding between the right of the [ScrollBar.scroll<class_ScrollBar_theme_style_scroll>] element and the [ScrollBar.grabber<class_ScrollBar_theme_style_grabber>].

\ **Note:** To apply vertical padding, modify the top/bottom content margins of [ScrollBar.scroll<class_ScrollBar_theme_style_scroll>] instead.

