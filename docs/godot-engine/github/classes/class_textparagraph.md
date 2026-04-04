:github_url: hide



# TextParagraph

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Holds a paragraph of text.


## Description

Abstraction over [TextServer<class_TextServer>] for handling a single paragraph of text.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------------------------------+----------------------------------------------------------------------------------+-----------+
> | :ref:`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`         | :ref:`alignment<class_TextParagraph_property_alignment>`                         | ``0``     |
> +---------------------------------------------------------------------------+----------------------------------------------------------------------------------+-----------+
> | |bitfield|\[:ref:`LineBreakFlag<enum_TextServer_LineBreakFlag>`\]         | :ref:`break_flags<class_TextParagraph_property_break_flags>`                     | ``3``     |
> +---------------------------------------------------------------------------+----------------------------------------------------------------------------------+-----------+
> | :ref:`String<class_String>`                                               | :ref:`custom_punctuation<class_TextParagraph_property_custom_punctuation>`       | ``""``    |
> +---------------------------------------------------------------------------+----------------------------------------------------------------------------------+-----------+
> | :ref:`Direction<enum_TextServer_Direction>`                               | :ref:`direction<class_TextParagraph_property_direction>`                         | ``0``     |
> +---------------------------------------------------------------------------+----------------------------------------------------------------------------------+-----------+
> | :ref:`String<class_String>`                                               | :ref:`ellipsis_char<class_TextParagraph_property_ellipsis_char>`                 | ``"…"``   |
> +---------------------------------------------------------------------------+----------------------------------------------------------------------------------+-----------+
> | |bitfield|\[:ref:`JustificationFlag<enum_TextServer_JustificationFlag>`\] | :ref:`justification_flags<class_TextParagraph_property_justification_flags>`     | ``163``   |
> +---------------------------------------------------------------------------+----------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                                                 | :ref:`line_spacing<class_TextParagraph_property_line_spacing>`                   | ``0.0``   |
> +---------------------------------------------------------------------------+----------------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`                                                     | :ref:`max_lines_visible<class_TextParagraph_property_max_lines_visible>`         | ``-1``    |
> +---------------------------------------------------------------------------+----------------------------------------------------------------------------------+-----------+
> | :ref:`Orientation<enum_TextServer_Orientation>`                           | :ref:`orientation<class_TextParagraph_property_orientation>`                     | ``0``     |
> +---------------------------------------------------------------------------+----------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                                   | :ref:`preserve_control<class_TextParagraph_property_preserve_control>`           | ``false`` |
> +---------------------------------------------------------------------------+----------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                                   | :ref:`preserve_invalid<class_TextParagraph_property_preserve_invalid>`           | ``true``  |
> +---------------------------------------------------------------------------+----------------------------------------------------------------------------------+-----------+
> | :ref:`OverrunBehavior<enum_TextServer_OverrunBehavior>`                   | :ref:`text_overrun_behavior<class_TextParagraph_property_text_overrun_behavior>` | ``0``     |
> +---------------------------------------------------------------------------+----------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                                                 | :ref:`width<class_TextParagraph_property_width>`                                 | ``-1.0``  |
> +---------------------------------------------------------------------------+----------------------------------------------------------------------------------+-----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                     | :ref:`add_object<class_TextParagraph_method_add_object>`\ (\ key\: :ref:`Variant<class_Variant>`, size\: :ref:`Vector2<class_Vector2>`, inline_align\: :ref:`InlineAlignment<enum_@GlobalScope_InlineAlignment>` = 5, length\: :ref:`int<class_int>` = 1, baseline\: :ref:`float<class_float>` = 0.0\ )                                                    |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                     | :ref:`add_string<class_TextParagraph_method_add_string>`\ (\ text\: :ref:`String<class_String>`, font\: :ref:`Font<class_Font>`, font_size\: :ref:`int<class_int>`, language\: :ref:`String<class_String>` = "", meta\: :ref:`Variant<class_Variant>` = null\ )                                                                                            |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                      | :ref:`clear<class_TextParagraph_method_clear>`\ (\ )                                                                                                                                                                                                                                                                                                       |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                      | :ref:`clear_dropcap<class_TextParagraph_method_clear_dropcap>`\ (\ )                                                                                                                                                                                                                                                                                       |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                      | :ref:`draw<class_TextParagraph_method_draw>`\ (\ canvas\: :ref:`RID<class_RID>`, pos\: :ref:`Vector2<class_Vector2>`, color\: :ref:`Color<class_Color>` = Color(1, 1, 1, 1), dc_color\: :ref:`Color<class_Color>` = Color(1, 1, 1, 1), oversampling\: :ref:`float<class_float>` = 0.0\ ) |const|                                                           |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                      | :ref:`draw_dropcap<class_TextParagraph_method_draw_dropcap>`\ (\ canvas\: :ref:`RID<class_RID>`, pos\: :ref:`Vector2<class_Vector2>`, color\: :ref:`Color<class_Color>` = Color(1, 1, 1, 1), oversampling\: :ref:`float<class_float>` = 0.0\ ) |const|                                                                                                     |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                      | :ref:`draw_dropcap_outline<class_TextParagraph_method_draw_dropcap_outline>`\ (\ canvas\: :ref:`RID<class_RID>`, pos\: :ref:`Vector2<class_Vector2>`, outline_size\: :ref:`int<class_int>` = 1, color\: :ref:`Color<class_Color>` = Color(1, 1, 1, 1), oversampling\: :ref:`float<class_float>` = 0.0\ ) |const|                                           |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                      | :ref:`draw_line<class_TextParagraph_method_draw_line>`\ (\ canvas\: :ref:`RID<class_RID>`, pos\: :ref:`Vector2<class_Vector2>`, line\: :ref:`int<class_int>`, color\: :ref:`Color<class_Color>` = Color(1, 1, 1, 1), oversampling\: :ref:`float<class_float>` = 0.0\ ) |const|                                                                             |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                      | :ref:`draw_line_outline<class_TextParagraph_method_draw_line_outline>`\ (\ canvas\: :ref:`RID<class_RID>`, pos\: :ref:`Vector2<class_Vector2>`, line\: :ref:`int<class_int>`, outline_size\: :ref:`int<class_int>` = 1, color\: :ref:`Color<class_Color>` = Color(1, 1, 1, 1), oversampling\: :ref:`float<class_float>` = 0.0\ ) |const|                   |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                      | :ref:`draw_outline<class_TextParagraph_method_draw_outline>`\ (\ canvas\: :ref:`RID<class_RID>`, pos\: :ref:`Vector2<class_Vector2>`, outline_size\: :ref:`int<class_int>` = 1, color\: :ref:`Color<class_Color>` = Color(1, 1, 1, 1), dc_color\: :ref:`Color<class_Color>` = Color(1, 1, 1, 1), oversampling\: :ref:`float<class_float>` = 0.0\ ) |const| |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`TextParagraph<class_TextParagraph>`   | :ref:`duplicate<class_TextParagraph_method_duplicate>`\ (\ ) |const|                                                                                                                                                                                                                                                                                       |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                       | :ref:`get_dropcap_lines<class_TextParagraph_method_get_dropcap_lines>`\ (\ ) |const|                                                                                                                                                                                                                                                                       |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                       | :ref:`get_dropcap_rid<class_TextParagraph_method_get_dropcap_rid>`\ (\ ) |const|                                                                                                                                                                                                                                                                           |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`               | :ref:`get_dropcap_size<class_TextParagraph_method_get_dropcap_size>`\ (\ ) |const|                                                                                                                                                                                                                                                                         |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Direction<enum_TextServer_Direction>` | :ref:`get_inferred_direction<class_TextParagraph_method_get_inferred_direction>`\ (\ ) |const|                                                                                                                                                                                                                                                             |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                   | :ref:`get_line_ascent<class_TextParagraph_method_get_line_ascent>`\ (\ line\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                             |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                       | :ref:`get_line_count<class_TextParagraph_method_get_line_count>`\ (\ ) |const|                                                                                                                                                                                                                                                                             |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                   | :ref:`get_line_descent<class_TextParagraph_method_get_line_descent>`\ (\ line\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                           |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2<class_Rect2>`                   | :ref:`get_line_object_rect<class_TextParagraph_method_get_line_object_rect>`\ (\ line\: :ref:`int<class_int>`, key\: :ref:`Variant<class_Variant>`\ ) |const|                                                                                                                                                                                              |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`                   | :ref:`get_line_objects<class_TextParagraph_method_get_line_objects>`\ (\ line\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                           |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2i<class_Vector2i>`             | :ref:`get_line_range<class_TextParagraph_method_get_line_range>`\ (\ line\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                               |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                       | :ref:`get_line_rid<class_TextParagraph_method_get_line_rid>`\ (\ line\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                                   |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`               | :ref:`get_line_size<class_TextParagraph_method_get_line_size>`\ (\ line\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                                 |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                   | :ref:`get_line_underline_position<class_TextParagraph_method_get_line_underline_position>`\ (\ line\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                     |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                   | :ref:`get_line_underline_thickness<class_TextParagraph_method_get_line_underline_thickness>`\ (\ line\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                   |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                   | :ref:`get_line_width<class_TextParagraph_method_get_line_width>`\ (\ line\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                               |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`               | :ref:`get_non_wrapped_size<class_TextParagraph_method_get_non_wrapped_size>`\ (\ ) |const|                                                                                                                                                                                                                                                                 |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2i<class_Vector2i>`             | :ref:`get_range<class_TextParagraph_method_get_range>`\ (\ ) |const|                                                                                                                                                                                                                                                                                       |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                       | :ref:`get_rid<class_TextParagraph_method_get_rid>`\ (\ ) |const|                                                                                                                                                                                                                                                                                           |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`               | :ref:`get_size<class_TextParagraph_method_get_size>`\ (\ ) |const|                                                                                                                                                                                                                                                                                         |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                     | :ref:`has_object<class_TextParagraph_method_has_object>`\ (\ key\: :ref:`Variant<class_Variant>`\ ) |const|                                                                                                                                                                                                                                                |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                       | :ref:`hit_test<class_TextParagraph_method_hit_test>`\ (\ coords\: :ref:`Vector2<class_Vector2>`\ ) |const|                                                                                                                                                                                                                                                 |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                     | :ref:`resize_object<class_TextParagraph_method_resize_object>`\ (\ key\: :ref:`Variant<class_Variant>`, size\: :ref:`Vector2<class_Vector2>`, inline_align\: :ref:`InlineAlignment<enum_@GlobalScope_InlineAlignment>` = 5, baseline\: :ref:`float<class_float>` = 0.0\ )                                                                                  |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                      | :ref:`set_bidi_override<class_TextParagraph_method_set_bidi_override>`\ (\ override\: :ref:`Array<class_Array>`\ )                                                                                                                                                                                                                                         |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                     | :ref:`set_dropcap<class_TextParagraph_method_set_dropcap>`\ (\ text\: :ref:`String<class_String>`, font\: :ref:`Font<class_Font>`, font_size\: :ref:`int<class_int>`, dropcap_margins\: :ref:`Rect2<class_Rect2>` = Rect2(0, 0, 0, 0), language\: :ref:`String<class_String>` = ""\ )                                                                      |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                      | :ref:`tab_align<class_TextParagraph_method_tab_align>`\ (\ tab_stops\: :ref:`PackedFloat32Array<class_PackedFloat32Array>`\ )                                                                                                                                                                                                                              |
> +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>] **alignment** = `0` [🔗<class_TextParagraph_property_alignment>]


- |void| **set_alignment**\ (\ value\: [HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>]\ )
- [HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>] **get_alignment**\ (\ )

Paragraph horizontal alignment.


----



|bitfield|\[[LineBreakFlag<enum_TextServer_LineBreakFlag>]\] **break_flags** = `3` [🔗<class_TextParagraph_property_break_flags>]


- |void| **set_break_flags**\ (\ value\: |bitfield|\[[LineBreakFlag<enum_TextServer_LineBreakFlag>]\]\ )
- |bitfield|\[[LineBreakFlag<enum_TextServer_LineBreakFlag>]\] **get_break_flags**\ (\ )

Line breaking rules. For more info see [TextServer<class_TextServer>].


----



[String<class_String>] **custom_punctuation** = `""` [🔗<class_TextParagraph_property_custom_punctuation>]


- |void| **set_custom_punctuation**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_custom_punctuation**\ (\ )

Custom punctuation character list, used for word breaking. If set to empty string, server defaults are used.


----



[Direction<enum_TextServer_Direction>] **direction** = `0` [🔗<class_TextParagraph_property_direction>]


- |void| **set_direction**\ (\ value\: [Direction<enum_TextServer_Direction>]\ )
- [Direction<enum_TextServer_Direction>] **get_direction**\ (\ )

Text writing direction.


----



[String<class_String>] **ellipsis_char** = `"…"` [🔗<class_TextParagraph_property_ellipsis_char>]


- |void| **set_ellipsis_char**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_ellipsis_char**\ (\ )

Ellipsis character used for text clipping.


----



|bitfield|\[[JustificationFlag<enum_TextServer_JustificationFlag>]\] **justification_flags** = `163` [🔗<class_TextParagraph_property_justification_flags>]


- |void| **set_justification_flags**\ (\ value\: |bitfield|\[[JustificationFlag<enum_TextServer_JustificationFlag>]\]\ )
- |bitfield|\[[JustificationFlag<enum_TextServer_JustificationFlag>]\] **get_justification_flags**\ (\ )

Line fill alignment rules.


----



[float<class_float>] **line_spacing** = `0.0` [🔗<class_TextParagraph_property_line_spacing>]


- |void| **set_line_spacing**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_line_spacing**\ (\ )

Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.


----



[int<class_int>] **max_lines_visible** = `-1` [🔗<class_TextParagraph_property_max_lines_visible>]


- |void| **set_max_lines_visible**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_max_lines_visible**\ (\ )

Limits the lines of text shown.


----



[Orientation<enum_TextServer_Orientation>] **orientation** = `0` [🔗<class_TextParagraph_property_orientation>]


- |void| **set_orientation**\ (\ value\: [Orientation<enum_TextServer_Orientation>]\ )
- [Orientation<enum_TextServer_Orientation>] **get_orientation**\ (\ )

Text orientation.


----



[bool<class_bool>] **preserve_control** = `false` [🔗<class_TextParagraph_property_preserve_control>]


- |void| **set_preserve_control**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_preserve_control**\ (\ )

If set to `true` text will display control characters.


----



[bool<class_bool>] **preserve_invalid** = `true` [🔗<class_TextParagraph_property_preserve_invalid>]


- |void| **set_preserve_invalid**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_preserve_invalid**\ (\ )

If set to `true` text will display invalid characters.


----



[OverrunBehavior<enum_TextServer_OverrunBehavior>] **text_overrun_behavior** = `0` [🔗<class_TextParagraph_property_text_overrun_behavior>]


- |void| **set_text_overrun_behavior**\ (\ value\: [OverrunBehavior<enum_TextServer_OverrunBehavior>]\ )
- [OverrunBehavior<enum_TextServer_OverrunBehavior>] **get_text_overrun_behavior**\ (\ )

The clipping behavior when the text exceeds the paragraph's set width.


----



[float<class_float>] **width** = `-1.0` [🔗<class_TextParagraph_property_width>]


- |void| **set_width**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_width**\ (\ )

Paragraph width.


----


## Method Descriptions



[bool<class_bool>] **add_object**\ (\ key\: [Variant<class_Variant>], size\: [Vector2<class_Vector2>], inline_align\: [InlineAlignment<enum_@GlobalScope_InlineAlignment>] = 5, length\: [int<class_int>] = 1, baseline\: [float<class_float>] = 0.0\ ) [🔗<class_TextParagraph_method_add_object>]

Adds inline object to the text buffer, `key` must be unique. In the text, object is represented as `length` object replacement characters.


----



[bool<class_bool>] **add_string**\ (\ text\: [String<class_String>], font\: [Font<class_Font>], font_size\: [int<class_int>], language\: [String<class_String>] = "", meta\: [Variant<class_Variant>] = null\ ) [🔗<class_TextParagraph_method_add_string>]

Adds text span and font to draw it.


----



|void| **clear**\ (\ ) [🔗<class_TextParagraph_method_clear>]

Clears text paragraph (removes text and inline objects).


----



|void| **clear_dropcap**\ (\ ) [🔗<class_TextParagraph_method_clear_dropcap>]

Removes dropcap.


----



|void| **draw**\ (\ canvas\: [RID<class_RID>], pos\: [Vector2<class_Vector2>], color\: [Color<class_Color>] = Color(1, 1, 1, 1), dc_color\: [Color<class_Color>] = Color(1, 1, 1, 1), oversampling\: [float<class_float>] = 0.0\ ) |const| [🔗<class_TextParagraph_method_draw>]

Draw all lines of the text and drop cap into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.


----



|void| **draw_dropcap**\ (\ canvas\: [RID<class_RID>], pos\: [Vector2<class_Vector2>], color\: [Color<class_Color>] = Color(1, 1, 1, 1), oversampling\: [float<class_float>] = 0.0\ ) |const| [🔗<class_TextParagraph_method_draw_dropcap>]

Draw drop cap into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.


----



|void| **draw_dropcap_outline**\ (\ canvas\: [RID<class_RID>], pos\: [Vector2<class_Vector2>], outline_size\: [int<class_int>] = 1, color\: [Color<class_Color>] = Color(1, 1, 1, 1), oversampling\: [float<class_float>] = 0.0\ ) |const| [🔗<class_TextParagraph_method_draw_dropcap_outline>]

Draw drop cap outline into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.


----



|void| **draw_line**\ (\ canvas\: [RID<class_RID>], pos\: [Vector2<class_Vector2>], line\: [int<class_int>], color\: [Color<class_Color>] = Color(1, 1, 1, 1), oversampling\: [float<class_float>] = 0.0\ ) |const| [🔗<class_TextParagraph_method_draw_line>]

Draw single line of text into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.


----



|void| **draw_line_outline**\ (\ canvas\: [RID<class_RID>], pos\: [Vector2<class_Vector2>], line\: [int<class_int>], outline_size\: [int<class_int>] = 1, color\: [Color<class_Color>] = Color(1, 1, 1, 1), oversampling\: [float<class_float>] = 0.0\ ) |const| [🔗<class_TextParagraph_method_draw_line_outline>]

Draw outline of the single line of text into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.


----



|void| **draw_outline**\ (\ canvas\: [RID<class_RID>], pos\: [Vector2<class_Vector2>], outline_size\: [int<class_int>] = 1, color\: [Color<class_Color>] = Color(1, 1, 1, 1), dc_color\: [Color<class_Color>] = Color(1, 1, 1, 1), oversampling\: [float<class_float>] = 0.0\ ) |const| [🔗<class_TextParagraph_method_draw_outline>]

Draw outlines of all lines of the text and drop cap into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.


----



[TextParagraph<class_TextParagraph>] **duplicate**\ (\ ) |const| [🔗<class_TextParagraph_method_duplicate>]

Duplicates this **TextParagraph**.


----



[int<class_int>] **get_dropcap_lines**\ (\ ) |const| [🔗<class_TextParagraph_method_get_dropcap_lines>]

Returns number of lines used by dropcap.


----



[RID<class_RID>] **get_dropcap_rid**\ (\ ) |const| [🔗<class_TextParagraph_method_get_dropcap_rid>]

Returns drop cap text buffer RID.


----



[Vector2<class_Vector2>] **get_dropcap_size**\ (\ ) |const| [🔗<class_TextParagraph_method_get_dropcap_size>]

Returns drop cap bounding box size.


----



[Direction<enum_TextServer_Direction>] **get_inferred_direction**\ (\ ) |const| [🔗<class_TextParagraph_method_get_inferred_direction>]

Returns the text writing direction inferred by the BiDi algorithm.


----



[float<class_float>] **get_line_ascent**\ (\ line\: [int<class_int>]\ ) |const| [🔗<class_TextParagraph_method_get_line_ascent>]

Returns the text line ascent (number of pixels above the baseline for horizontal layout or to the left of baseline for vertical).


----



[int<class_int>] **get_line_count**\ (\ ) |const| [🔗<class_TextParagraph_method_get_line_count>]

Returns number of lines in the paragraph.


----



[float<class_float>] **get_line_descent**\ (\ line\: [int<class_int>]\ ) |const| [🔗<class_TextParagraph_method_get_line_descent>]

Returns the text line descent (number of pixels below the baseline for horizontal layout or to the right of baseline for vertical).


----



[Rect2<class_Rect2>] **get_line_object_rect**\ (\ line\: [int<class_int>], key\: [Variant<class_Variant>]\ ) |const| [🔗<class_TextParagraph_method_get_line_object_rect>]

Returns bounding rectangle of the inline object.


----



[Array<class_Array>] **get_line_objects**\ (\ line\: [int<class_int>]\ ) |const| [🔗<class_TextParagraph_method_get_line_objects>]

Returns array of inline objects in the line.


----



[Vector2i<class_Vector2i>] **get_line_range**\ (\ line\: [int<class_int>]\ ) |const| [🔗<class_TextParagraph_method_get_line_range>]

Returns character range of the line.


----



[RID<class_RID>] **get_line_rid**\ (\ line\: [int<class_int>]\ ) |const| [🔗<class_TextParagraph_method_get_line_rid>]

Returns TextServer line buffer RID.


----



[Vector2<class_Vector2>] **get_line_size**\ (\ line\: [int<class_int>]\ ) |const| [🔗<class_TextParagraph_method_get_line_size>]

Returns size of the bounding box of the line of text. Returned size is rounded up.


----



[float<class_float>] **get_line_underline_position**\ (\ line\: [int<class_int>]\ ) |const| [🔗<class_TextParagraph_method_get_line_underline_position>]

Returns pixel offset of the underline below the baseline.


----



[float<class_float>] **get_line_underline_thickness**\ (\ line\: [int<class_int>]\ ) |const| [🔗<class_TextParagraph_method_get_line_underline_thickness>]

Returns thickness of the underline.


----



[float<class_float>] **get_line_width**\ (\ line\: [int<class_int>]\ ) |const| [🔗<class_TextParagraph_method_get_line_width>]

Returns width (for horizontal layout) or height (for vertical) of the line of text.


----



[Vector2<class_Vector2>] **get_non_wrapped_size**\ (\ ) |const| [🔗<class_TextParagraph_method_get_non_wrapped_size>]

Returns the size of the bounding box of the paragraph, without line breaks.


----



[Vector2i<class_Vector2i>] **get_range**\ (\ ) |const| [🔗<class_TextParagraph_method_get_range>]

Returns the character range of the paragraph.


----



[RID<class_RID>] **get_rid**\ (\ ) |const| [🔗<class_TextParagraph_method_get_rid>]

Returns TextServer full string buffer RID.


----



[Vector2<class_Vector2>] **get_size**\ (\ ) |const| [🔗<class_TextParagraph_method_get_size>]

Returns the size of the bounding box of the paragraph.


----



[bool<class_bool>] **has_object**\ (\ key\: [Variant<class_Variant>]\ ) |const| [🔗<class_TextParagraph_method_has_object>]

Returns `true` if an object with `key` is embedded in this shaped text buffer.


----



[int<class_int>] **hit_test**\ (\ coords\: [Vector2<class_Vector2>]\ ) |const| [🔗<class_TextParagraph_method_hit_test>]

Returns caret character offset at the specified coordinates. This function always returns a valid position.


----



[bool<class_bool>] **resize_object**\ (\ key\: [Variant<class_Variant>], size\: [Vector2<class_Vector2>], inline_align\: [InlineAlignment<enum_@GlobalScope_InlineAlignment>] = 5, baseline\: [float<class_float>] = 0.0\ ) [🔗<class_TextParagraph_method_resize_object>]

Sets new size and alignment of embedded object.


----



|void| **set_bidi_override**\ (\ override\: [Array<class_Array>]\ ) [🔗<class_TextParagraph_method_set_bidi_override>]

Overrides BiDi for the structured text.

Override ranges should cover full source text without overlaps. BiDi algorithm will be used on each range separately.


----



[bool<class_bool>] **set_dropcap**\ (\ text\: [String<class_String>], font\: [Font<class_Font>], font_size\: [int<class_int>], dropcap_margins\: [Rect2<class_Rect2>] = Rect2(0, 0, 0, 0), language\: [String<class_String>] = ""\ ) [🔗<class_TextParagraph_method_set_dropcap>]

Sets drop cap, overrides previously set drop cap. Drop cap (dropped capital) is a decorative element at the beginning of a paragraph that is larger than the rest of the text.


----



|void| **tab_align**\ (\ tab_stops\: [PackedFloat32Array<class_PackedFloat32Array>]\ ) [🔗<class_TextParagraph_method_tab_align>]

Aligns paragraph to the given tab-stops.

