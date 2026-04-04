:github_url: hide



# MenuBar

**Inherits:** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A horizontal menu bar that creates a menu for each [PopupMenu<class_PopupMenu>] child.


## Description

A horizontal menu bar that creates a menu for each [PopupMenu<class_PopupMenu>] child. New items are created by adding [PopupMenu<class_PopupMenu>]\ s to this node. Item title is determined by [Window.title<class_Window_property_title>], or node name if [Window.title<class_Window_property_title>] is empty. Item title can be overridden using [set_menu_title()<class_MenuBar_method_set_menu_title>].


## Properties

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------+----------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                          | :ref:`flat<class_MenuBar_property_flat>`                             | ``false``                                                           |
> +--------------------------------------------------+----------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`FocusMode<enum_Control_FocusMode>`         | focus_mode                                                           | ``3`` (overrides :ref:`Control<class_Control_property_focus_mode>`) |
> +--------------------------------------------------+----------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`String<class_String>`                      | :ref:`language<class_MenuBar_property_language>`                     | ``""``                                                              |
> +--------------------------------------------------+----------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                          | :ref:`prefer_global_menu<class_MenuBar_property_prefer_global_menu>` | ``true``                                                            |
> +--------------------------------------------------+----------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`int<class_int>`                            | :ref:`start_index<class_MenuBar_property_start_index>`               | ``-1``                                                              |
> +--------------------------------------------------+----------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                          | :ref:`switch_on_hover<class_MenuBar_property_switch_on_hover>`       | ``true``                                                            |
> +--------------------------------------------------+----------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`TextDirection<enum_Control_TextDirection>` | :ref:`text_direction<class_MenuBar_property_text_direction>`         | ``0``                                                               |
> +--------------------------------------------------+----------------------------------------------------------------------+---------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`             | :ref:`get_menu_count<class_MenuBar_method_get_menu_count>`\ (\ ) |const|                                                                  |
> +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PopupMenu<class_PopupMenu>` | :ref:`get_menu_popup<class_MenuBar_method_get_menu_popup>`\ (\ menu\: :ref:`int<class_int>`\ ) |const|                                    |
> +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`       | :ref:`get_menu_title<class_MenuBar_method_get_menu_title>`\ (\ menu\: :ref:`int<class_int>`\ ) |const|                                    |
> +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`       | :ref:`get_menu_tooltip<class_MenuBar_method_get_menu_tooltip>`\ (\ menu\: :ref:`int<class_int>`\ ) |const|                                |
> +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`           | :ref:`is_menu_disabled<class_MenuBar_method_is_menu_disabled>`\ (\ menu\: :ref:`int<class_int>`\ ) |const|                                |
> +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`           | :ref:`is_menu_hidden<class_MenuBar_method_is_menu_hidden>`\ (\ menu\: :ref:`int<class_int>`\ ) |const|                                    |
> +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`           | :ref:`is_native_menu<class_MenuBar_method_is_native_menu>`\ (\ ) |const|                                                                  |
> +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                            | :ref:`set_disable_shortcuts<class_MenuBar_method_set_disable_shortcuts>`\ (\ disabled\: :ref:`bool<class_bool>`\ )                        |
> +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                            | :ref:`set_menu_disabled<class_MenuBar_method_set_menu_disabled>`\ (\ menu\: :ref:`int<class_int>`, disabled\: :ref:`bool<class_bool>`\ )  |
> +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                            | :ref:`set_menu_hidden<class_MenuBar_method_set_menu_hidden>`\ (\ menu\: :ref:`int<class_int>`, hidden\: :ref:`bool<class_bool>`\ )        |
> +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                            | :ref:`set_menu_title<class_MenuBar_method_set_menu_title>`\ (\ menu\: :ref:`int<class_int>`, title\: :ref:`String<class_String>`\ )       |
> +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                            | :ref:`set_menu_tooltip<class_MenuBar_method_set_menu_tooltip>`\ (\ menu\: :ref:`int<class_int>`, tooltip\: :ref:`String<class_String>`\ ) |
> +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
>

## Theme Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------+-------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Color<class_Color>`       | :ref:`font_color<class_MenuBar_theme_color_font_color>`                             | ``Color(0.875, 0.875, 0.875, 1)``   |
> +---------------------------------+-------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Color<class_Color>`       | :ref:`font_disabled_color<class_MenuBar_theme_color_font_disabled_color>`           | ``Color(0.875, 0.875, 0.875, 0.5)`` |
> +---------------------------------+-------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Color<class_Color>`       | :ref:`font_focus_color<class_MenuBar_theme_color_font_focus_color>`                 | ``Color(0.95, 0.95, 0.95, 1)``      |
> +---------------------------------+-------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Color<class_Color>`       | :ref:`font_hover_color<class_MenuBar_theme_color_font_hover_color>`                 | ``Color(0.95, 0.95, 0.95, 1)``      |
> +---------------------------------+-------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Color<class_Color>`       | :ref:`font_hover_pressed_color<class_MenuBar_theme_color_font_hover_pressed_color>` | ``Color(1, 1, 1, 1)``               |
> +---------------------------------+-------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Color<class_Color>`       | :ref:`font_outline_color<class_MenuBar_theme_color_font_outline_color>`             | ``Color(0, 0, 0, 1)``               |
> +---------------------------------+-------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Color<class_Color>`       | :ref:`font_pressed_color<class_MenuBar_theme_color_font_pressed_color>`             | ``Color(1, 1, 1, 1)``               |
> +---------------------------------+-------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`int<class_int>`           | :ref:`h_separation<class_MenuBar_theme_constant_h_separation>`                      | ``4``                               |
> +---------------------------------+-------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`int<class_int>`           | :ref:`outline_size<class_MenuBar_theme_constant_outline_size>`                      | ``0``                               |
> +---------------------------------+-------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`Font<class_Font>`         | :ref:`font<class_MenuBar_theme_font_font>`                                          |                                     |
> +---------------------------------+-------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`int<class_int>`           | :ref:`font_size<class_MenuBar_theme_font_size_font_size>`                           |                                     |
> +---------------------------------+-------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`StyleBox<class_StyleBox>` | :ref:`disabled<class_MenuBar_theme_style_disabled>`                                 |                                     |
> +---------------------------------+-------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`StyleBox<class_StyleBox>` | :ref:`disabled_mirrored<class_MenuBar_theme_style_disabled_mirrored>`               |                                     |
> +---------------------------------+-------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`StyleBox<class_StyleBox>` | :ref:`hover<class_MenuBar_theme_style_hover>`                                       |                                     |
> +---------------------------------+-------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`StyleBox<class_StyleBox>` | :ref:`hover_mirrored<class_MenuBar_theme_style_hover_mirrored>`                     |                                     |
> +---------------------------------+-------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`StyleBox<class_StyleBox>` | :ref:`hover_pressed<class_MenuBar_theme_style_hover_pressed>`                       |                                     |
> +---------------------------------+-------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`StyleBox<class_StyleBox>` | :ref:`hover_pressed_mirrored<class_MenuBar_theme_style_hover_pressed_mirrored>`     |                                     |
> +---------------------------------+-------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`StyleBox<class_StyleBox>` | :ref:`normal<class_MenuBar_theme_style_normal>`                                     |                                     |
> +---------------------------------+-------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`StyleBox<class_StyleBox>` | :ref:`normal_mirrored<class_MenuBar_theme_style_normal_mirrored>`                   |                                     |
> +---------------------------------+-------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`StyleBox<class_StyleBox>` | :ref:`pressed<class_MenuBar_theme_style_pressed>`                                   |                                     |
> +---------------------------------+-------------------------------------------------------------------------------------+-------------------------------------+
> | :ref:`StyleBox<class_StyleBox>` | :ref:`pressed_mirrored<class_MenuBar_theme_style_pressed_mirrored>`                 |                                     |
> +---------------------------------+-------------------------------------------------------------------------------------+-------------------------------------+
>

----


## Property Descriptions



[bool<class_bool>] **flat** = `false` [🔗<class_MenuBar_property_flat>]


- |void| **set_flat**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_flat**\ (\ )

Flat **MenuBar** don't display item decoration.


----



[String<class_String>] **language** = `""` [🔗<class_MenuBar_property_language>]


- |void| **set_language**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_language**\ (\ )

Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.


----



[bool<class_bool>] **prefer_global_menu** = `true` [🔗<class_MenuBar_property_prefer_global_menu>]


- |void| **set_prefer_global_menu**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_prefer_global_menu**\ (\ )

If `true`, **MenuBar** will use system global menu when supported.

\ **Note:** If `true` and global menu is supported, this node is not displayed, has zero size, and all its child nodes except [PopupMenu<class_PopupMenu>]\ s are inaccessible.

\ **Note:** This property overrides the value of the [PopupMenu.prefer_native_menu<class_PopupMenu_property_prefer_native_menu>] property of the child nodes.


----



[int<class_int>] **start_index** = `-1` [🔗<class_MenuBar_property_start_index>]


- |void| **set_start_index**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_start_index**\ (\ )

Position order in the global menu to insert **MenuBar** items at. All menu items in the **MenuBar** are always inserted as a continuous range. Menus with lower [start_index<class_MenuBar_property_start_index>] are inserted first. Menus with [start_index<class_MenuBar_property_start_index>] equal to `-1` are inserted last.


----



[bool<class_bool>] **switch_on_hover** = `true` [🔗<class_MenuBar_property_switch_on_hover>]


- |void| **set_switch_on_hover**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_switch_on_hover**\ (\ )

If `true`, when the cursor hovers above menu item, it will close the current [PopupMenu<class_PopupMenu>] and open the other one.


----



[TextDirection<enum_Control_TextDirection>] **text_direction** = `0` [🔗<class_MenuBar_property_text_direction>]


- |void| **set_text_direction**\ (\ value\: [TextDirection<enum_Control_TextDirection>]\ )
- [TextDirection<enum_Control_TextDirection>] **get_text_direction**\ (\ )

Base text writing direction.


----


## Method Descriptions



[int<class_int>] **get_menu_count**\ (\ ) |const| [🔗<class_MenuBar_method_get_menu_count>]

Returns number of menu items.


----



[PopupMenu<class_PopupMenu>] **get_menu_popup**\ (\ menu\: [int<class_int>]\ ) |const| [🔗<class_MenuBar_method_get_menu_popup>]

Returns [PopupMenu<class_PopupMenu>] associated with menu item.


----



[String<class_String>] **get_menu_title**\ (\ menu\: [int<class_int>]\ ) |const| [🔗<class_MenuBar_method_get_menu_title>]

Returns menu item title.


----



[String<class_String>] **get_menu_tooltip**\ (\ menu\: [int<class_int>]\ ) |const| [🔗<class_MenuBar_method_get_menu_tooltip>]

Returns menu item tooltip.


----



[bool<class_bool>] **is_menu_disabled**\ (\ menu\: [int<class_int>]\ ) |const| [🔗<class_MenuBar_method_is_menu_disabled>]

Returns `true` if the menu item is disabled.


----



[bool<class_bool>] **is_menu_hidden**\ (\ menu\: [int<class_int>]\ ) |const| [🔗<class_MenuBar_method_is_menu_hidden>]

Returns `true` if the menu item is hidden.


----



[bool<class_bool>] **is_native_menu**\ (\ ) |const| [🔗<class_MenuBar_method_is_native_menu>]

Returns `true` if the current system's global menu is supported and used by this **MenuBar**.


----



|void| **set_disable_shortcuts**\ (\ disabled\: [bool<class_bool>]\ ) [🔗<class_MenuBar_method_set_disable_shortcuts>]

If `true`, shortcuts are disabled and cannot be used to trigger the button.


----



|void| **set_menu_disabled**\ (\ menu\: [int<class_int>], disabled\: [bool<class_bool>]\ ) [🔗<class_MenuBar_method_set_menu_disabled>]

If `true`, menu item is disabled.


----



|void| **set_menu_hidden**\ (\ menu\: [int<class_int>], hidden\: [bool<class_bool>]\ ) [🔗<class_MenuBar_method_set_menu_hidden>]

If `true`, menu item is hidden.


----



|void| **set_menu_title**\ (\ menu\: [int<class_int>], title\: [String<class_String>]\ ) [🔗<class_MenuBar_method_set_menu_title>]

Sets menu item title.


----



|void| **set_menu_tooltip**\ (\ menu\: [int<class_int>], tooltip\: [String<class_String>]\ ) [🔗<class_MenuBar_method_set_menu_tooltip>]

Sets menu item tooltip.


----


## Theme Property Descriptions



[Color<class_Color>] **font_color** = `Color(0.875, 0.875, 0.875, 1)` [🔗<class_MenuBar_theme_color_font_color>]

Default text [Color<class_Color>] of the menu item.


----



[Color<class_Color>] **font_disabled_color** = `Color(0.875, 0.875, 0.875, 0.5)` [🔗<class_MenuBar_theme_color_font_disabled_color>]

Text [Color<class_Color>] used when the menu item is disabled.


----



[Color<class_Color>] **font_focus_color** = `Color(0.95, 0.95, 0.95, 1)` [🔗<class_MenuBar_theme_color_font_focus_color>]

Text [Color<class_Color>] used when the menu item is focused. Only replaces the normal text color of the menu item. Disabled, hovered, and pressed states take precedence over this color.


----



[Color<class_Color>] **font_hover_color** = `Color(0.95, 0.95, 0.95, 1)` [🔗<class_MenuBar_theme_color_font_hover_color>]

Text [Color<class_Color>] used when the menu item is being hovered.


----



[Color<class_Color>] **font_hover_pressed_color** = `Color(1, 1, 1, 1)` [🔗<class_MenuBar_theme_color_font_hover_pressed_color>]

Text [Color<class_Color>] used when the menu item is being hovered and pressed.


----



[Color<class_Color>] **font_outline_color** = `Color(0, 0, 0, 1)` [🔗<class_MenuBar_theme_color_font_outline_color>]

The tint of text outline of the menu item.


----



[Color<class_Color>] **font_pressed_color** = `Color(1, 1, 1, 1)` [🔗<class_MenuBar_theme_color_font_pressed_color>]

Text [Color<class_Color>] used when the menu item is being pressed.


----



[int<class_int>] **h_separation** = `4` [🔗<class_MenuBar_theme_constant_h_separation>]

The horizontal space between menu items.


----



[int<class_int>] **outline_size** = `0` [🔗<class_MenuBar_theme_constant_outline_size>]

The size of the text outline.

\ **Note:** If using a font with [FontFile.multichannel_signed_distance_field<class_FontFile_property_multichannel_signed_distance_field>] enabled, its [FontFile.msdf_pixel_range<class_FontFile_property_msdf_pixel_range>] must be set to at least *twice* the value of [outline_size<class_MenuBar_theme_constant_outline_size>] for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.


----



[Font<class_Font>] **font** [🔗<class_MenuBar_theme_font_font>]

[Font<class_Font>] of the menu item's text.


----



[int<class_int>] **font_size** [🔗<class_MenuBar_theme_font_size_font_size>]

Font size of the menu item's text.


----



[StyleBox<class_StyleBox>] **disabled** [🔗<class_MenuBar_theme_style_disabled>]

[StyleBox<class_StyleBox>] used when the menu item is disabled.


----



[StyleBox<class_StyleBox>] **disabled_mirrored** [🔗<class_MenuBar_theme_style_disabled_mirrored>]

[StyleBox<class_StyleBox>] used when the menu item is disabled (for right-to-left layouts).


----



[StyleBox<class_StyleBox>] **hover** [🔗<class_MenuBar_theme_style_hover>]

[StyleBox<class_StyleBox>] used when the menu item is being hovered.


----



[StyleBox<class_StyleBox>] **hover_mirrored** [🔗<class_MenuBar_theme_style_hover_mirrored>]

[StyleBox<class_StyleBox>] used when the menu item is being hovered (for right-to-left layouts).


----



[StyleBox<class_StyleBox>] **hover_pressed** [🔗<class_MenuBar_theme_style_hover_pressed>]

[StyleBox<class_StyleBox>] used when the menu item is being pressed and hovered at the same time.


----



[StyleBox<class_StyleBox>] **hover_pressed_mirrored** [🔗<class_MenuBar_theme_style_hover_pressed_mirrored>]

[StyleBox<class_StyleBox>] used when the menu item is being pressed and hovered at the same time (for right-to-left layouts).


----



[StyleBox<class_StyleBox>] **normal** [🔗<class_MenuBar_theme_style_normal>]

Default [StyleBox<class_StyleBox>] for the menu item.


----



[StyleBox<class_StyleBox>] **normal_mirrored** [🔗<class_MenuBar_theme_style_normal_mirrored>]

Default [StyleBox<class_StyleBox>] for the menu item (for right-to-left layouts).


----



[StyleBox<class_StyleBox>] **pressed** [🔗<class_MenuBar_theme_style_pressed>]

[StyleBox<class_StyleBox>] used when the menu item is being pressed.


----



[StyleBox<class_StyleBox>] **pressed_mirrored** [🔗<class_MenuBar_theme_style_pressed_mirrored>]

[StyleBox<class_StyleBox>] used when the menu item is being pressed (for right-to-left layouts).

