:github_url: hide



# TextLine

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Holds a line of text.


## Description

Abstraction over [TextServer<class_TextServer>] for handling a single line of text.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------------------------------+-----------------------------------------------------------------------------+-----------+
> | :ref:`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`         | :ref:`alignment<class_TextLine_property_alignment>`                         | ``0``     |
> +---------------------------------------------------------------------------+-----------------------------------------------------------------------------+-----------+
> | :ref:`Direction<enum_TextServer_Direction>`                               | :ref:`direction<class_TextLine_property_direction>`                         | ``0``     |
> +---------------------------------------------------------------------------+-----------------------------------------------------------------------------+-----------+
> | :ref:`String<class_String>`                                               | :ref:`ellipsis_char<class_TextLine_property_ellipsis_char>`                 | ``"…"``   |
> +---------------------------------------------------------------------------+-----------------------------------------------------------------------------+-----------+
> | |bitfield|\[:ref:`JustificationFlag<enum_TextServer_JustificationFlag>`\] | :ref:`flags<class_TextLine_property_flags>`                                 | ``3``     |
> +---------------------------------------------------------------------------+-----------------------------------------------------------------------------+-----------+
> | :ref:`Orientation<enum_TextServer_Orientation>`                           | :ref:`orientation<class_TextLine_property_orientation>`                     | ``0``     |
> +---------------------------------------------------------------------------+-----------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                                   | :ref:`preserve_control<class_TextLine_property_preserve_control>`           | ``false`` |
> +---------------------------------------------------------------------------+-----------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                                   | :ref:`preserve_invalid<class_TextLine_property_preserve_invalid>`           | ``true``  |
> +---------------------------------------------------------------------------+-----------------------------------------------------------------------------+-----------+
> | :ref:`OverrunBehavior<enum_TextServer_OverrunBehavior>`                   | :ref:`text_overrun_behavior<class_TextLine_property_text_overrun_behavior>` | ``3``     |
> +---------------------------------------------------------------------------+-----------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                                                 | :ref:`width<class_TextLine_property_width>`                                 | ``-1.0``  |
> +---------------------------------------------------------------------------+-----------------------------------------------------------------------------+-----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                     | :ref:`add_object<class_TextLine_method_add_object>`\ (\ key\: :ref:`Variant<class_Variant>`, size\: :ref:`Vector2<class_Vector2>`, inline_align\: :ref:`InlineAlignment<enum_@GlobalScope_InlineAlignment>` = 5, length\: :ref:`int<class_int>` = 1, baseline\: :ref:`float<class_float>` = 0.0\ ) |
> +---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                     | :ref:`add_string<class_TextLine_method_add_string>`\ (\ text\: :ref:`String<class_String>`, font\: :ref:`Font<class_Font>`, font_size\: :ref:`int<class_int>`, language\: :ref:`String<class_String>` = "", meta\: :ref:`Variant<class_Variant>` = null\ )                                         |
> +---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                      | :ref:`clear<class_TextLine_method_clear>`\ (\ )                                                                                                                                                                                                                                                    |
> +---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                      | :ref:`draw<class_TextLine_method_draw>`\ (\ canvas\: :ref:`RID<class_RID>`, pos\: :ref:`Vector2<class_Vector2>`, color\: :ref:`Color<class_Color>` = Color(1, 1, 1, 1), oversampling\: :ref:`float<class_float>` = 0.0\ ) |const|                                                                  |
> +---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                      | :ref:`draw_outline<class_TextLine_method_draw_outline>`\ (\ canvas\: :ref:`RID<class_RID>`, pos\: :ref:`Vector2<class_Vector2>`, outline_size\: :ref:`int<class_int>` = 1, color\: :ref:`Color<class_Color>` = Color(1, 1, 1, 1), oversampling\: :ref:`float<class_float>` = 0.0\ ) |const|        |
> +---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`TextLine<class_TextLine>`             | :ref:`duplicate<class_TextLine_method_duplicate>`\ (\ ) |const|                                                                                                                                                                                                                                    |
> +---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Direction<enum_TextServer_Direction>` | :ref:`get_inferred_direction<class_TextLine_method_get_inferred_direction>`\ (\ ) |const|                                                                                                                                                                                                          |
> +---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                   | :ref:`get_line_ascent<class_TextLine_method_get_line_ascent>`\ (\ ) |const|                                                                                                                                                                                                                        |
> +---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                   | :ref:`get_line_descent<class_TextLine_method_get_line_descent>`\ (\ ) |const|                                                                                                                                                                                                                      |
> +---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                   | :ref:`get_line_underline_position<class_TextLine_method_get_line_underline_position>`\ (\ ) |const|                                                                                                                                                                                                |
> +---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                   | :ref:`get_line_underline_thickness<class_TextLine_method_get_line_underline_thickness>`\ (\ ) |const|                                                                                                                                                                                              |
> +---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                   | :ref:`get_line_width<class_TextLine_method_get_line_width>`\ (\ ) |const|                                                                                                                                                                                                                          |
> +---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2<class_Rect2>`                   | :ref:`get_object_rect<class_TextLine_method_get_object_rect>`\ (\ key\: :ref:`Variant<class_Variant>`\ ) |const|                                                                                                                                                                                   |
> +---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`                   | :ref:`get_objects<class_TextLine_method_get_objects>`\ (\ ) |const|                                                                                                                                                                                                                                |
> +---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                       | :ref:`get_rid<class_TextLine_method_get_rid>`\ (\ ) |const|                                                                                                                                                                                                                                        |
> +---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`               | :ref:`get_size<class_TextLine_method_get_size>`\ (\ ) |const|                                                                                                                                                                                                                                      |
> +---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                     | :ref:`has_object<class_TextLine_method_has_object>`\ (\ key\: :ref:`Variant<class_Variant>`\ ) |const|                                                                                                                                                                                             |
> +---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                       | :ref:`hit_test<class_TextLine_method_hit_test>`\ (\ coords\: :ref:`float<class_float>`\ ) |const|                                                                                                                                                                                                  |
> +---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                     | :ref:`resize_object<class_TextLine_method_resize_object>`\ (\ key\: :ref:`Variant<class_Variant>`, size\: :ref:`Vector2<class_Vector2>`, inline_align\: :ref:`InlineAlignment<enum_@GlobalScope_InlineAlignment>` = 5, baseline\: :ref:`float<class_float>` = 0.0\ )                               |
> +---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                      | :ref:`set_bidi_override<class_TextLine_method_set_bidi_override>`\ (\ override\: :ref:`Array<class_Array>`\ )                                                                                                                                                                                      |
> +---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                      | :ref:`tab_align<class_TextLine_method_tab_align>`\ (\ tab_stops\: :ref:`PackedFloat32Array<class_PackedFloat32Array>`\ )                                                                                                                                                                           |
> +---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>] **alignment** = `0` [🔗<class_TextLine_property_alignment>]


- |void| **set_horizontal_alignment**\ (\ value\: [HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>]\ )
- [HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>] **get_horizontal_alignment**\ (\ )

Sets text alignment within the line as if the line was horizontal.


----



[Direction<enum_TextServer_Direction>] **direction** = `0` [🔗<class_TextLine_property_direction>]


- |void| **set_direction**\ (\ value\: [Direction<enum_TextServer_Direction>]\ )
- [Direction<enum_TextServer_Direction>] **get_direction**\ (\ )

Text writing direction.


----



[String<class_String>] **ellipsis_char** = `"…"` [🔗<class_TextLine_property_ellipsis_char>]


- |void| **set_ellipsis_char**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_ellipsis_char**\ (\ )

Ellipsis character used for text clipping.


----



|bitfield|\[[JustificationFlag<enum_TextServer_JustificationFlag>]\] **flags** = `3` [🔗<class_TextLine_property_flags>]


- |void| **set_flags**\ (\ value\: |bitfield|\[[JustificationFlag<enum_TextServer_JustificationFlag>]\]\ )
- |bitfield|\[[JustificationFlag<enum_TextServer_JustificationFlag>]\] **get_flags**\ (\ )

Line alignment rules. For more info see [TextServer<class_TextServer>].


----



[Orientation<enum_TextServer_Orientation>] **orientation** = `0` [🔗<class_TextLine_property_orientation>]


- |void| **set_orientation**\ (\ value\: [Orientation<enum_TextServer_Orientation>]\ )
- [Orientation<enum_TextServer_Orientation>] **get_orientation**\ (\ )

Text orientation.


----



[bool<class_bool>] **preserve_control** = `false` [🔗<class_TextLine_property_preserve_control>]


- |void| **set_preserve_control**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_preserve_control**\ (\ )

If set to `true` text will display control characters.


----



[bool<class_bool>] **preserve_invalid** = `true` [🔗<class_TextLine_property_preserve_invalid>]


- |void| **set_preserve_invalid**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_preserve_invalid**\ (\ )

If set to `true` text will display invalid characters.


----



[OverrunBehavior<enum_TextServer_OverrunBehavior>] **text_overrun_behavior** = `3` [🔗<class_TextLine_property_text_overrun_behavior>]


- |void| **set_text_overrun_behavior**\ (\ value\: [OverrunBehavior<enum_TextServer_OverrunBehavior>]\ )
- [OverrunBehavior<enum_TextServer_OverrunBehavior>] **get_text_overrun_behavior**\ (\ )

The clipping behavior when the text exceeds the text line's set width.


----



[float<class_float>] **width** = `-1.0` [🔗<class_TextLine_property_width>]


- |void| **set_width**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_width**\ (\ )

Text line width.


----


## Method Descriptions



[bool<class_bool>] **add_object**\ (\ key\: [Variant<class_Variant>], size\: [Vector2<class_Vector2>], inline_align\: [InlineAlignment<enum_@GlobalScope_InlineAlignment>] = 5, length\: [int<class_int>] = 1, baseline\: [float<class_float>] = 0.0\ ) [🔗<class_TextLine_method_add_object>]

Adds inline object to the text buffer, `key` must be unique. In the text, object is represented as `length` object replacement characters.


----



[bool<class_bool>] **add_string**\ (\ text\: [String<class_String>], font\: [Font<class_Font>], font_size\: [int<class_int>], language\: [String<class_String>] = "", meta\: [Variant<class_Variant>] = null\ ) [🔗<class_TextLine_method_add_string>]

Adds text span and font to draw it.


----



|void| **clear**\ (\ ) [🔗<class_TextLine_method_clear>]

Clears text line (removes text and inline objects).


----



|void| **draw**\ (\ canvas\: [RID<class_RID>], pos\: [Vector2<class_Vector2>], color\: [Color<class_Color>] = Color(1, 1, 1, 1), oversampling\: [float<class_float>] = 0.0\ ) |const| [🔗<class_TextLine_method_draw>]

Draw text into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.


----



|void| **draw_outline**\ (\ canvas\: [RID<class_RID>], pos\: [Vector2<class_Vector2>], outline_size\: [int<class_int>] = 1, color\: [Color<class_Color>] = Color(1, 1, 1, 1), oversampling\: [float<class_float>] = 0.0\ ) |const| [🔗<class_TextLine_method_draw_outline>]

Draw text into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.


----



[TextLine<class_TextLine>] **duplicate**\ (\ ) |const| [🔗<class_TextLine_method_duplicate>]

Duplicates this **TextLine**.


----



[Direction<enum_TextServer_Direction>] **get_inferred_direction**\ (\ ) |const| [🔗<class_TextLine_method_get_inferred_direction>]

Returns the text writing direction inferred by the BiDi algorithm.


----



[float<class_float>] **get_line_ascent**\ (\ ) |const| [🔗<class_TextLine_method_get_line_ascent>]

Returns the text ascent (number of pixels above the baseline for horizontal layout or to the left of baseline for vertical).


----



[float<class_float>] **get_line_descent**\ (\ ) |const| [🔗<class_TextLine_method_get_line_descent>]

Returns the text descent (number of pixels below the baseline for horizontal layout or to the right of baseline for vertical).


----



[float<class_float>] **get_line_underline_position**\ (\ ) |const| [🔗<class_TextLine_method_get_line_underline_position>]

Returns pixel offset of the underline below the baseline.


----



[float<class_float>] **get_line_underline_thickness**\ (\ ) |const| [🔗<class_TextLine_method_get_line_underline_thickness>]

Returns thickness of the underline.


----



[float<class_float>] **get_line_width**\ (\ ) |const| [🔗<class_TextLine_method_get_line_width>]

Returns width (for horizontal layout) or height (for vertical) of the text.


----



[Rect2<class_Rect2>] **get_object_rect**\ (\ key\: [Variant<class_Variant>]\ ) |const| [🔗<class_TextLine_method_get_object_rect>]

Returns bounding rectangle of the inline object.


----



[Array<class_Array>] **get_objects**\ (\ ) |const| [🔗<class_TextLine_method_get_objects>]

Returns array of inline objects.


----



[RID<class_RID>] **get_rid**\ (\ ) |const| [🔗<class_TextLine_method_get_rid>]

Returns TextServer buffer RID.


----



[Vector2<class_Vector2>] **get_size**\ (\ ) |const| [🔗<class_TextLine_method_get_size>]

Returns size of the bounding box of the text.


----



[bool<class_bool>] **has_object**\ (\ key\: [Variant<class_Variant>]\ ) |const| [🔗<class_TextLine_method_has_object>]

Returns `true` if an object with `key` is embedded in this line.


----



[int<class_int>] **hit_test**\ (\ coords\: [float<class_float>]\ ) |const| [🔗<class_TextLine_method_hit_test>]

Returns caret character offset at the specified pixel offset at the baseline. This function always returns a valid position.


----



[bool<class_bool>] **resize_object**\ (\ key\: [Variant<class_Variant>], size\: [Vector2<class_Vector2>], inline_align\: [InlineAlignment<enum_@GlobalScope_InlineAlignment>] = 5, baseline\: [float<class_float>] = 0.0\ ) [🔗<class_TextLine_method_resize_object>]

Sets new size and alignment of embedded object.


----



|void| **set_bidi_override**\ (\ override\: [Array<class_Array>]\ ) [🔗<class_TextLine_method_set_bidi_override>]

Overrides BiDi for the structured text.

Override ranges should cover full source text without overlaps. BiDi algorithm will be used on each range separately.


----



|void| **tab_align**\ (\ tab_stops\: [PackedFloat32Array<class_PackedFloat32Array>]\ ) [🔗<class_TextLine_method_tab_align>]

Aligns text to the given tab-stops.

