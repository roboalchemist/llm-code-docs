:github_url: hide



# TextMesh

**Inherits:** [PrimitiveMesh<class_PrimitiveMesh>] **<** [Mesh<class_Mesh>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Generate a [PrimitiveMesh<class_PrimitiveMesh>] from the text.


## Description

Generate a [PrimitiveMesh<class_PrimitiveMesh>] from the text.

TextMesh can be generated only when using dynamic fonts with vector glyph contours. Bitmap fonts (including bitmap data in the TrueType/OpenType containers, like color emoji fonts) are not supported.

The UV layout is arranged in 4 horizontal strips, top to bottom: 40% of the height for the front face, 40% for the back face, 10% for the outer edges and 10% for the inner edges.


## Tutorials

- [../tutorials/3d/3d_text](3D text .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+-------------------+
> | :ref:`AutowrapMode<enum_TextServer_AutowrapMode>`                         | :ref:`autowrap_mode<class_TextMesh_property_autowrap_mode>`                                                 | ``0``             |
> +---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+-------------------+
> | :ref:`float<class_float>`                                                 | :ref:`curve_step<class_TextMesh_property_curve_step>`                                                       | ``0.5``           |
> +---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+-------------------+
> | :ref:`float<class_float>`                                                 | :ref:`depth<class_TextMesh_property_depth>`                                                                 | ``0.05``          |
> +---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+-------------------+
> | :ref:`Font<class_Font>`                                                   | :ref:`font<class_TextMesh_property_font>`                                                                   |                   |
> +---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+-------------------+
> | :ref:`int<class_int>`                                                     | :ref:`font_size<class_TextMesh_property_font_size>`                                                         | ``16``            |
> +---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+-------------------+
> | :ref:`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`         | :ref:`horizontal_alignment<class_TextMesh_property_horizontal_alignment>`                                   | ``1``             |
> +---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+-------------------+
> | |bitfield|\[:ref:`JustificationFlag<enum_TextServer_JustificationFlag>`\] | :ref:`justification_flags<class_TextMesh_property_justification_flags>`                                     | ``163``           |
> +---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+-------------------+
> | :ref:`String<class_String>`                                               | :ref:`language<class_TextMesh_property_language>`                                                           | ``""``            |
> +---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+-------------------+
> | :ref:`float<class_float>`                                                 | :ref:`line_spacing<class_TextMesh_property_line_spacing>`                                                   | ``0.0``           |
> +---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+-------------------+
> | :ref:`Vector2<class_Vector2>`                                             | :ref:`offset<class_TextMesh_property_offset>`                                                               | ``Vector2(0, 0)`` |
> +---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+-------------------+
> | :ref:`float<class_float>`                                                 | :ref:`pixel_size<class_TextMesh_property_pixel_size>`                                                       | ``0.01``          |
> +---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+-------------------+
> | :ref:`StructuredTextParser<enum_TextServer_StructuredTextParser>`         | :ref:`structured_text_bidi_override<class_TextMesh_property_structured_text_bidi_override>`                 | ``0``             |
> +---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+-------------------+
> | :ref:`Array<class_Array>`                                                 | :ref:`structured_text_bidi_override_options<class_TextMesh_property_structured_text_bidi_override_options>` | ``[]``            |
> +---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+-------------------+
> | :ref:`String<class_String>`                                               | :ref:`text<class_TextMesh_property_text>`                                                                   | ``""``            |
> +---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+-------------------+
> | :ref:`Direction<enum_TextServer_Direction>`                               | :ref:`text_direction<class_TextMesh_property_text_direction>`                                               | ``0``             |
> +---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+-------------------+
> | :ref:`bool<class_bool>`                                                   | :ref:`uppercase<class_TextMesh_property_uppercase>`                                                         | ``false``         |
> +---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+-------------------+
> | :ref:`VerticalAlignment<enum_@GlobalScope_VerticalAlignment>`             | :ref:`vertical_alignment<class_TextMesh_property_vertical_alignment>`                                       | ``1``             |
> +---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+-------------------+
> | :ref:`float<class_float>`                                                 | :ref:`width<class_TextMesh_property_width>`                                                                 | ``500.0``         |
> +---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+-------------------+
>

----


## Property Descriptions



[AutowrapMode<enum_TextServer_AutowrapMode>] **autowrap_mode** = `0` [🔗<class_TextMesh_property_autowrap_mode>]


- |void| **set_autowrap_mode**\ (\ value\: [AutowrapMode<enum_TextServer_AutowrapMode>]\ )
- [AutowrapMode<enum_TextServer_AutowrapMode>] **get_autowrap_mode**\ (\ )

If set to something other than [TextServer.AUTOWRAP_OFF<class_TextServer_constant_AUTOWRAP_OFF>], the text gets wrapped inside the node's bounding rectangle. If you resize the node, it will change its height automatically to show all the text.


----



[float<class_float>] **curve_step** = `0.5` [🔗<class_TextMesh_property_curve_step>]


- |void| **set_curve_step**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_curve_step**\ (\ )

Step (in pixels) used to approximate Bézier curves. Lower values result in smoother curves, but is slower to generate and render. Consider adjusting this according to the font size and the typical viewing distance.

\ **Note:** Changing this property will regenerate the mesh, which is a slow operation, especially with large font sizes and long texts.


----



[float<class_float>] **depth** = `0.05` [🔗<class_TextMesh_property_depth>]


- |void| **set_depth**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_depth**\ (\ )

Depths of the mesh, if set to `0.0` only front surface, is generated, and UV layout is changed to use full texture for the front face only.


----



[Font<class_Font>] **font** [🔗<class_TextMesh_property_font>]


- |void| **set_font**\ (\ value\: [Font<class_Font>]\ )
- [Font<class_Font>] **get_font**\ (\ )

Font configuration used to display text.


----



[int<class_int>] **font_size** = `16` [🔗<class_TextMesh_property_font_size>]


- |void| **set_font_size**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_font_size**\ (\ )

Font size of the **TextMesh**'s text. This property works in tandem with [pixel_size<class_TextMesh_property_pixel_size>]. Higher values will result in a more detailed font, regardless of [curve_step<class_TextMesh_property_curve_step>] and [pixel_size<class_TextMesh_property_pixel_size>]. Consider keeping this value below 63 (inclusive) for good performance, and adjust [pixel_size<class_TextMesh_property_pixel_size>] as needed to enlarge text.

\ **Note:** Changing this property will regenerate the mesh, which is a slow operation, especially with large font sizes and long texts. To change the text's size in real-time efficiently, change the node's [Node3D.scale<class_Node3D_property_scale>] instead.


----



[HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>] **horizontal_alignment** = `1` [🔗<class_TextMesh_property_horizontal_alignment>]


- |void| **set_horizontal_alignment**\ (\ value\: [HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>]\ )
- [HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>] **get_horizontal_alignment**\ (\ )

Controls the text's horizontal alignment. Supports left, center, right, and fill (also known as justify).


----



|bitfield|\[[JustificationFlag<enum_TextServer_JustificationFlag>]\] **justification_flags** = `163` [🔗<class_TextMesh_property_justification_flags>]


- |void| **set_justification_flags**\ (\ value\: |bitfield|\[[JustificationFlag<enum_TextServer_JustificationFlag>]\]\ )
- |bitfield|\[[JustificationFlag<enum_TextServer_JustificationFlag>]\] **get_justification_flags**\ (\ )

Line fill alignment rules.


----



[String<class_String>] **language** = `""` [🔗<class_TextMesh_property_language>]


- |void| **set_language**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_language**\ (\ )

Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.


----



[float<class_float>] **line_spacing** = `0.0` [🔗<class_TextMesh_property_line_spacing>]


- |void| **set_line_spacing**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_line_spacing**\ (\ )

Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.


----



[Vector2<class_Vector2>] **offset** = `Vector2(0, 0)` [🔗<class_TextMesh_property_offset>]


- |void| **set_offset**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_offset**\ (\ )

The text drawing offset (in pixels).

\ **Note:** Changing this property will regenerate the mesh, which is a slow operation. To change the text's position in real-time efficiently, change the node's [Node3D.position<class_Node3D_property_position>] instead.


----



[float<class_float>] **pixel_size** = `0.01` [🔗<class_TextMesh_property_pixel_size>]


- |void| **set_pixel_size**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_pixel_size**\ (\ )

The size of one pixel's width on the text to scale it in 3D. This property works in tandem with [font_size<class_TextMesh_property_font_size>].

\ **Note:** Changing this property will regenerate the mesh, which is a slow operation, especially with large font sizes and long texts. To change the text's size in real-time efficiently, change the node's [Node3D.scale<class_Node3D_property_scale>] instead.


----



[StructuredTextParser<enum_TextServer_StructuredTextParser>] **structured_text_bidi_override** = `0` [🔗<class_TextMesh_property_structured_text_bidi_override>]


- |void| **set_structured_text_bidi_override**\ (\ value\: [StructuredTextParser<enum_TextServer_StructuredTextParser>]\ )
- [StructuredTextParser<enum_TextServer_StructuredTextParser>] **get_structured_text_bidi_override**\ (\ )

Set BiDi algorithm override for the structured text.


----



[Array<class_Array>] **structured_text_bidi_override_options** = `[]` [🔗<class_TextMesh_property_structured_text_bidi_override_options>]


- |void| **set_structured_text_bidi_override_options**\ (\ value\: [Array<class_Array>]\ )
- [Array<class_Array>] **get_structured_text_bidi_override_options**\ (\ )

Set additional options for BiDi override.


----



[String<class_String>] **text** = `""` [🔗<class_TextMesh_property_text>]


- |void| **set_text**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_text**\ (\ )

The text to generate mesh from.

\ **Note:** Due to being a [Resource<class_Resource>], it doesn't follow the rules of [Node.auto_translate_mode<class_Node_property_auto_translate_mode>]. If disabling translation is desired, it should be done manually with [Object.set_message_translation()<class_Object_method_set_message_translation>].


----



[Direction<enum_TextServer_Direction>] **text_direction** = `0` [🔗<class_TextMesh_property_text_direction>]


- |void| **set_text_direction**\ (\ value\: [Direction<enum_TextServer_Direction>]\ )
- [Direction<enum_TextServer_Direction>] **get_text_direction**\ (\ )

Base text writing direction.


----



[bool<class_bool>] **uppercase** = `false` [🔗<class_TextMesh_property_uppercase>]


- |void| **set_uppercase**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_uppercase**\ (\ )

If `true`, all the text displays as UPPERCASE.


----



[VerticalAlignment<enum_@GlobalScope_VerticalAlignment>] **vertical_alignment** = `1` [🔗<class_TextMesh_property_vertical_alignment>]


- |void| **set_vertical_alignment**\ (\ value\: [VerticalAlignment<enum_@GlobalScope_VerticalAlignment>]\ )
- [VerticalAlignment<enum_@GlobalScope_VerticalAlignment>] **get_vertical_alignment**\ (\ )

Controls the text's vertical alignment. Supports top, center, and bottom.


----



[float<class_float>] **width** = `500.0` [🔗<class_TextMesh_property_width>]


- |void| **set_width**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_width**\ (\ )

Text width (in pixels), used for fill alignment.

