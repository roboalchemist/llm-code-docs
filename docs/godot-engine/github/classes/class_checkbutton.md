:github_url: hide

> **META**
	:keywords: switch, toggle



# CheckButton

**Inherits:** [Button<class_Button>] **<** [BaseButton<class_BaseButton>] **<** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A button that represents a binary choice.


## Description

**CheckButton** is a toggle button displayed as a check field. It's similar to [CheckBox<class_CheckBox>] in functionality, but it has a different appearance. To follow established UX patterns, it's recommended to use **CheckButton** when toggling it has an **immediate** effect on something. For example, it can be used when pressing it shows or hides advanced settings, without asking the user to confirm this action.

See also [BaseButton<class_BaseButton>] which contains common properties and methods associated with this node.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------------------+-------------+-------------------------------------------------------------------------------+
> | :ref:`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>` | alignment   | ``0`` (overrides :ref:`Button<class_Button_property_alignment>`)              |
> +-------------------------------------------------------------------+-------------+-------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                           | toggle_mode | ``true`` (overrides :ref:`BaseButton<class_BaseButton_property_toggle_mode>`) |
> +-------------------------------------------------------------------+-------------+-------------------------------------------------------------------------------+
>

## Theme Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------+----------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>`         | :ref:`button_checked_color<class_CheckButton_theme_color_button_checked_color>`              | ``Color(1, 1, 1, 1)`` |
> +-----------------------------------+----------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>`         | :ref:`button_unchecked_color<class_CheckButton_theme_color_button_unchecked_color>`          | ``Color(1, 1, 1, 1)`` |
> +-----------------------------------+----------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`             | :ref:`check_v_offset<class_CheckButton_theme_constant_check_v_offset>`                       | ``0``                 |
> +-----------------------------------+----------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`checked<class_CheckButton_theme_icon_checked>`                                         |                       |
> +-----------------------------------+----------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`checked_disabled<class_CheckButton_theme_icon_checked_disabled>`                       |                       |
> +-----------------------------------+----------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`checked_disabled_mirrored<class_CheckButton_theme_icon_checked_disabled_mirrored>`     |                       |
> +-----------------------------------+----------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`checked_mirrored<class_CheckButton_theme_icon_checked_mirrored>`                       |                       |
> +-----------------------------------+----------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`unchecked<class_CheckButton_theme_icon_unchecked>`                                     |                       |
> +-----------------------------------+----------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`unchecked_disabled<class_CheckButton_theme_icon_unchecked_disabled>`                   |                       |
> +-----------------------------------+----------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`unchecked_disabled_mirrored<class_CheckButton_theme_icon_unchecked_disabled_mirrored>` |                       |
> +-----------------------------------+----------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`unchecked_mirrored<class_CheckButton_theme_icon_unchecked_mirrored>`                   |                       |
> +-----------------------------------+----------------------------------------------------------------------------------------------+-----------------------+
>

----


## Theme Property Descriptions



[Color<class_Color>] **button_checked_color** = `Color(1, 1, 1, 1)` [🔗<class_CheckButton_theme_color_button_checked_color>]

The color of the checked icon when the checkbox is pressed.


----



[Color<class_Color>] **button_unchecked_color** = `Color(1, 1, 1, 1)` [🔗<class_CheckButton_theme_color_button_unchecked_color>]

The color of the unchecked icon when the checkbox is not pressed.


----



[int<class_int>] **check_v_offset** = `0` [🔗<class_CheckButton_theme_constant_check_v_offset>]

The vertical offset used when rendering the toggle icons (in pixels).


----



[Texture2D<class_Texture2D>] **checked** [🔗<class_CheckButton_theme_icon_checked>]

The icon to display when the **CheckButton** is checked (for left-to-right layouts).


----



[Texture2D<class_Texture2D>] **checked_disabled** [🔗<class_CheckButton_theme_icon_checked_disabled>]

The icon to display when the **CheckButton** is checked and disabled (for left-to-right layouts).


----



[Texture2D<class_Texture2D>] **checked_disabled_mirrored** [🔗<class_CheckButton_theme_icon_checked_disabled_mirrored>]

The icon to display when the **CheckButton** is checked and disabled (for right-to-left layouts).


----



[Texture2D<class_Texture2D>] **checked_mirrored** [🔗<class_CheckButton_theme_icon_checked_mirrored>]

The icon to display when the **CheckButton** is checked (for right-to-left layouts).


----



[Texture2D<class_Texture2D>] **unchecked** [🔗<class_CheckButton_theme_icon_unchecked>]

The icon to display when the **CheckButton** is unchecked (for left-to-right layouts).


----



[Texture2D<class_Texture2D>] **unchecked_disabled** [🔗<class_CheckButton_theme_icon_unchecked_disabled>]

The icon to display when the **CheckButton** is unchecked and disabled (for left-to-right layouts).


----



[Texture2D<class_Texture2D>] **unchecked_disabled_mirrored** [🔗<class_CheckButton_theme_icon_unchecked_disabled_mirrored>]

The icon to display when the **CheckButton** is unchecked and disabled (for right-to-left layouts).


----



[Texture2D<class_Texture2D>] **unchecked_mirrored** [🔗<class_CheckButton_theme_icon_unchecked_mirrored>]

The icon to display when the **CheckButton** is unchecked (for right-to-left layouts).

