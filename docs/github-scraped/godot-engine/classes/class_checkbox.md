:github_url: hide



# CheckBox

**Inherits:** [Button<class_Button>] **<** [BaseButton<class_BaseButton>] **<** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A button that represents a binary choice.


## Description

**CheckBox** allows the user to choose one of only two possible options. It's similar to [CheckButton<class_CheckButton>] in functionality, but it has a different appearance. To follow established UX patterns, it's recommended to use **CheckBox** when toggling it has **no** immediate effect on something. For example, it could be used when toggling it will only do something once a confirmation button is pressed.

See also [BaseButton<class_BaseButton>] which contains common properties and methods associated with this node.

When [BaseButton.button_group<class_BaseButton_property_button_group>] specifies a [ButtonGroup<class_ButtonGroup>], **CheckBox** changes its appearance to that of a radio button and uses the various `radio_*` theme properties.


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
> +-----------------------------------+--------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>`         | :ref:`checkbox_checked_color<class_CheckBox_theme_color_checkbox_checked_color>`     | ``Color(1, 1, 1, 1)`` |
> +-----------------------------------+--------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>`         | :ref:`checkbox_unchecked_color<class_CheckBox_theme_color_checkbox_unchecked_color>` | ``Color(1, 1, 1, 1)`` |
> +-----------------------------------+--------------------------------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`             | :ref:`check_v_offset<class_CheckBox_theme_constant_check_v_offset>`                  | ``0``                 |
> +-----------------------------------+--------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`checked<class_CheckBox_theme_icon_checked>`                                    |                       |
> +-----------------------------------+--------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`checked_disabled<class_CheckBox_theme_icon_checked_disabled>`                  |                       |
> +-----------------------------------+--------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`radio_checked<class_CheckBox_theme_icon_radio_checked>`                        |                       |
> +-----------------------------------+--------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`radio_checked_disabled<class_CheckBox_theme_icon_radio_checked_disabled>`      |                       |
> +-----------------------------------+--------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`radio_unchecked<class_CheckBox_theme_icon_radio_unchecked>`                    |                       |
> +-----------------------------------+--------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`radio_unchecked_disabled<class_CheckBox_theme_icon_radio_unchecked_disabled>`  |                       |
> +-----------------------------------+--------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`unchecked<class_CheckBox_theme_icon_unchecked>`                                |                       |
> +-----------------------------------+--------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`unchecked_disabled<class_CheckBox_theme_icon_unchecked_disabled>`              |                       |
> +-----------------------------------+--------------------------------------------------------------------------------------+-----------------------+
>

----


## Theme Property Descriptions



[Color<class_Color>] **checkbox_checked_color** = `Color(1, 1, 1, 1)` [🔗<class_CheckBox_theme_color_checkbox_checked_color>]

The color of the checked icon when the checkbox is pressed.


----



[Color<class_Color>] **checkbox_unchecked_color** = `Color(1, 1, 1, 1)` [🔗<class_CheckBox_theme_color_checkbox_unchecked_color>]

The color of the unchecked icon when the checkbox is not pressed.


----



[int<class_int>] **check_v_offset** = `0` [🔗<class_CheckBox_theme_constant_check_v_offset>]

The vertical offset used when rendering the check icons (in pixels).


----



[Texture2D<class_Texture2D>] **checked** [🔗<class_CheckBox_theme_icon_checked>]

The check icon to display when the **CheckBox** is checked.


----



[Texture2D<class_Texture2D>] **checked_disabled** [🔗<class_CheckBox_theme_icon_checked_disabled>]

The check icon to display when the **CheckBox** is checked and is disabled.


----



[Texture2D<class_Texture2D>] **radio_checked** [🔗<class_CheckBox_theme_icon_radio_checked>]

The check icon to display when the **CheckBox** is configured as a radio button and is checked.


----



[Texture2D<class_Texture2D>] **radio_checked_disabled** [🔗<class_CheckBox_theme_icon_radio_checked_disabled>]

The check icon to display when the **CheckBox** is configured as a radio button, is disabled, and is unchecked.


----



[Texture2D<class_Texture2D>] **radio_unchecked** [🔗<class_CheckBox_theme_icon_radio_unchecked>]

The check icon to display when the **CheckBox** is configured as a radio button and is unchecked.


----



[Texture2D<class_Texture2D>] **radio_unchecked_disabled** [🔗<class_CheckBox_theme_icon_radio_unchecked_disabled>]

The check icon to display when the **CheckBox** is configured as a radio button, is disabled, and is unchecked.


----



[Texture2D<class_Texture2D>] **unchecked** [🔗<class_CheckBox_theme_icon_unchecked>]

The check icon to display when the **CheckBox** is unchecked.


----



[Texture2D<class_Texture2D>] **unchecked_disabled** [🔗<class_CheckBox_theme_icon_unchecked_disabled>]

The check icon to display when the **CheckBox** is unchecked and is disabled.

