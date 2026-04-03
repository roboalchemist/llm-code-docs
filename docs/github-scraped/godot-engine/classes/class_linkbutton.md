:github_url: hide



# LinkButton

**Inherits:** [BaseButton<class_BaseButton>] **<** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A button that represents a link.


## Description

A button that represents a link. This type of button is primarily used for interactions that cause a context change (like linking to a web page).

See also [BaseButton<class_BaseButton>] which contains common properties and methods associated with this node.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                       | :ref:`ellipsis_char<class_LinkButton_property_ellipsis_char>`                                                 | ``"…"``                                                                             |
> +-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
> | :ref:`FocusMode<enum_Control_FocusMode>`                          | focus_mode                                                                                                    | ``3`` (overrides :ref:`Control<class_Control_property_focus_mode>`)                 |
> +-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                       | :ref:`language<class_LinkButton_property_language>`                                                           | ``""``                                                                              |
> +-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
> | :ref:`CursorShape<enum_Control_CursorShape>`                      | mouse_default_cursor_shape                                                                                    | ``2`` (overrides :ref:`Control<class_Control_property_mouse_default_cursor_shape>`) |
> +-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
> | :ref:`StructuredTextParser<enum_TextServer_StructuredTextParser>` | :ref:`structured_text_bidi_override<class_LinkButton_property_structured_text_bidi_override>`                 | ``0``                                                                               |
> +-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`                                         | :ref:`structured_text_bidi_override_options<class_LinkButton_property_structured_text_bidi_override_options>` | ``[]``                                                                              |
> +-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                       | :ref:`text<class_LinkButton_property_text>`                                                                   | ``""``                                                                              |
> +-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
> | :ref:`TextDirection<enum_Control_TextDirection>`                  | :ref:`text_direction<class_LinkButton_property_text_direction>`                                               | ``0``                                                                               |
> +-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
> | :ref:`OverrunBehavior<enum_TextServer_OverrunBehavior>`           | :ref:`text_overrun_behavior<class_LinkButton_property_text_overrun_behavior>`                                 | ``0``                                                                               |
> +-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
> | :ref:`UnderlineMode<enum_LinkButton_UnderlineMode>`               | :ref:`underline<class_LinkButton_property_underline>`                                                         | ``0``                                                                               |
> +-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                       | :ref:`uri<class_LinkButton_property_uri>`                                                                     | ``""``                                                                              |
> +-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
>

## Theme Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------+----------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`Color<class_Color>`       | :ref:`font_color<class_LinkButton_theme_color_font_color>`                             | ``Color(0.875, 0.875, 0.875, 1)`` |
> +---------------------------------+----------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`Color<class_Color>`       | :ref:`font_disabled_color<class_LinkButton_theme_color_font_disabled_color>`           | ``Color(0, 0, 0, 1)``             |
> +---------------------------------+----------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`Color<class_Color>`       | :ref:`font_focus_color<class_LinkButton_theme_color_font_focus_color>`                 | ``Color(0.95, 0.95, 0.95, 1)``    |
> +---------------------------------+----------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`Color<class_Color>`       | :ref:`font_hover_color<class_LinkButton_theme_color_font_hover_color>`                 | ``Color(0.95, 0.95, 0.95, 1)``    |
> +---------------------------------+----------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`Color<class_Color>`       | :ref:`font_hover_pressed_color<class_LinkButton_theme_color_font_hover_pressed_color>` | ``Color(0, 0, 0, 1)``             |
> +---------------------------------+----------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`Color<class_Color>`       | :ref:`font_outline_color<class_LinkButton_theme_color_font_outline_color>`             | ``Color(0, 0, 0, 1)``             |
> +---------------------------------+----------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`Color<class_Color>`       | :ref:`font_pressed_color<class_LinkButton_theme_color_font_pressed_color>`             | ``Color(1, 1, 1, 1)``             |
> +---------------------------------+----------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`int<class_int>`           | :ref:`outline_size<class_LinkButton_theme_constant_outline_size>`                      | ``0``                             |
> +---------------------------------+----------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`int<class_int>`           | :ref:`underline_spacing<class_LinkButton_theme_constant_underline_spacing>`            | ``2``                             |
> +---------------------------------+----------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`Font<class_Font>`         | :ref:`font<class_LinkButton_theme_font_font>`                                          |                                   |
> +---------------------------------+----------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`int<class_int>`           | :ref:`font_size<class_LinkButton_theme_font_size_font_size>`                           |                                   |
> +---------------------------------+----------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`StyleBox<class_StyleBox>` | :ref:`focus<class_LinkButton_theme_style_focus>`                                       |                                   |
> +---------------------------------+----------------------------------------------------------------------------------------+-----------------------------------+
>

----


## Enumerations



enum **UnderlineMode**: [🔗<enum_LinkButton_UnderlineMode>]



[UnderlineMode<enum_LinkButton_UnderlineMode>] **UNDERLINE_MODE_ALWAYS** = `0`

The LinkButton will always show an underline at the bottom of its text.



[UnderlineMode<enum_LinkButton_UnderlineMode>] **UNDERLINE_MODE_ON_HOVER** = `1`

The LinkButton will show an underline at the bottom of its text when the mouse cursor is over it.



[UnderlineMode<enum_LinkButton_UnderlineMode>] **UNDERLINE_MODE_NEVER** = `2`

The LinkButton will never show an underline at the bottom of its text.


----


## Property Descriptions



[String<class_String>] **ellipsis_char** = `"…"` [🔗<class_LinkButton_property_ellipsis_char>]


- |void| **set_ellipsis_char**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_ellipsis_char**\ (\ )

Ellipsis character used for text clipping.


----



[String<class_String>] **language** = `""` [🔗<class_LinkButton_property_language>]


- |void| **set_language**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_language**\ (\ )

Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.


----



[StructuredTextParser<enum_TextServer_StructuredTextParser>] **structured_text_bidi_override** = `0` [🔗<class_LinkButton_property_structured_text_bidi_override>]


- |void| **set_structured_text_bidi_override**\ (\ value\: [StructuredTextParser<enum_TextServer_StructuredTextParser>]\ )
- [StructuredTextParser<enum_TextServer_StructuredTextParser>] **get_structured_text_bidi_override**\ (\ )

Set BiDi algorithm override for the structured text.


----



[Array<class_Array>] **structured_text_bidi_override_options** = `[]` [🔗<class_LinkButton_property_structured_text_bidi_override_options>]


- |void| **set_structured_text_bidi_override_options**\ (\ value\: [Array<class_Array>]\ )
- [Array<class_Array>] **get_structured_text_bidi_override_options**\ (\ )

Set additional options for BiDi override.


----



[String<class_String>] **text** = `""` [🔗<class_LinkButton_property_text>]


- |void| **set_text**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_text**\ (\ )

The button's text that will be displayed inside the button's area.


----



[TextDirection<enum_Control_TextDirection>] **text_direction** = `0` [🔗<class_LinkButton_property_text_direction>]


- |void| **set_text_direction**\ (\ value\: [TextDirection<enum_Control_TextDirection>]\ )
- [TextDirection<enum_Control_TextDirection>] **get_text_direction**\ (\ )

Base text writing direction.


----



[OverrunBehavior<enum_TextServer_OverrunBehavior>] **text_overrun_behavior** = `0` [🔗<class_LinkButton_property_text_overrun_behavior>]


- |void| **set_text_overrun_behavior**\ (\ value\: [OverrunBehavior<enum_TextServer_OverrunBehavior>]\ )
- [OverrunBehavior<enum_TextServer_OverrunBehavior>] **get_text_overrun_behavior**\ (\ )

Sets the clipping behavior when the text exceeds the node's bounding rectangle.


----



[UnderlineMode<enum_LinkButton_UnderlineMode>] **underline** = `0` [🔗<class_LinkButton_property_underline>]


- |void| **set_underline_mode**\ (\ value\: [UnderlineMode<enum_LinkButton_UnderlineMode>]\ )
- [UnderlineMode<enum_LinkButton_UnderlineMode>] **get_underline_mode**\ (\ )

The underline mode to use for the text.


----



[String<class_String>] **uri** = `""` [🔗<class_LinkButton_property_uri>]


- |void| **set_uri**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_uri**\ (\ )

The [URI ](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier)_ for this **LinkButton**. If set to a valid URI, pressing the button opens the URI using the operating system's default program for the protocol (via [OS.shell_open()<class_OS_method_shell_open>]). HTTP and HTTPS URLs open the default web browser.


> **TABS**
>

    uri = "https://godotengine.org"  # Opens the URL in the default web browser.
    uri = "C:\SomeFolder"  # Opens the file explorer at the given path.
    uri = "C:\SomeImage.png"  # Opens the given image in the default viewing app.


    Uri = "https://godotengine.org"; // Opens the URL in the default web browser.
    Uri = "C:\SomeFolder"; // Opens the file explorer at the given path.
    Uri = "C:\SomeImage.png"; // Opens the given image in the default viewing app.




----


## Theme Property Descriptions



[Color<class_Color>] **font_color** = `Color(0.875, 0.875, 0.875, 1)` [🔗<class_LinkButton_theme_color_font_color>]

Default text [Color<class_Color>] of the **LinkButton**.


----



[Color<class_Color>] **font_disabled_color** = `Color(0, 0, 0, 1)` [🔗<class_LinkButton_theme_color_font_disabled_color>]

Text [Color<class_Color>] used when the **LinkButton** is disabled.


----



[Color<class_Color>] **font_focus_color** = `Color(0.95, 0.95, 0.95, 1)` [🔗<class_LinkButton_theme_color_font_focus_color>]

Text [Color<class_Color>] used when the **LinkButton** is focused. Only replaces the normal text color of the button. Disabled, hovered, and pressed states take precedence over this color.


----



[Color<class_Color>] **font_hover_color** = `Color(0.95, 0.95, 0.95, 1)` [🔗<class_LinkButton_theme_color_font_hover_color>]

Text [Color<class_Color>] used when the **LinkButton** is being hovered.


----



[Color<class_Color>] **font_hover_pressed_color** = `Color(0, 0, 0, 1)` [🔗<class_LinkButton_theme_color_font_hover_pressed_color>]

Text [Color<class_Color>] used when the **LinkButton** is being hovered and pressed.


----



[Color<class_Color>] **font_outline_color** = `Color(0, 0, 0, 1)` [🔗<class_LinkButton_theme_color_font_outline_color>]

The tint of text outline of the **LinkButton**.


----



[Color<class_Color>] **font_pressed_color** = `Color(1, 1, 1, 1)` [🔗<class_LinkButton_theme_color_font_pressed_color>]

Text [Color<class_Color>] used when the **LinkButton** is being pressed.


----



[int<class_int>] **outline_size** = `0` [🔗<class_LinkButton_theme_constant_outline_size>]

The size of the text outline.

\ **Note:** If using a font with [FontFile.multichannel_signed_distance_field<class_FontFile_property_multichannel_signed_distance_field>] enabled, its [FontFile.msdf_pixel_range<class_FontFile_property_msdf_pixel_range>] must be set to at least *twice* the value of [outline_size<class_LinkButton_theme_constant_outline_size>] for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.


----



[int<class_int>] **underline_spacing** = `2` [🔗<class_LinkButton_theme_constant_underline_spacing>]

The vertical space between the baseline of text and the underline.


----



[Font<class_Font>] **font** [🔗<class_LinkButton_theme_font_font>]

[Font<class_Font>] of the **LinkButton**'s text.


----



[int<class_int>] **font_size** [🔗<class_LinkButton_theme_font_size_font_size>]

Font size of the **LinkButton**'s text.


----



[StyleBox<class_StyleBox>] **focus** [🔗<class_LinkButton_theme_style_focus>]

[StyleBox<class_StyleBox>] used when the **LinkButton** is focused. The [focus<class_LinkButton_theme_style_focus>] [StyleBox<class_StyleBox>] is displayed *over* the base [StyleBox<class_StyleBox>], so a partially transparent [StyleBox<class_StyleBox>] should be used to ensure the base [StyleBox<class_StyleBox>] remains visible. A [StyleBox<class_StyleBox>] that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a [StyleBoxEmpty<class_StyleBoxEmpty>] resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.

