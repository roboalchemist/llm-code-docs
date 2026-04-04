:github_url: hide

> **META**
	:keywords: text



# Label3D

**Inherits:** [GeometryInstance3D<class_GeometryInstance3D>] **<** [VisualInstance3D<class_VisualInstance3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A node for displaying plain text in 3D space.


## Description

A node for displaying plain text in 3D space. By adjusting various properties of this node, you can configure things such as the text's appearance and whether it always faces the camera.


## Tutorials

- [../tutorials/3d/3d_text](3D text .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                                 | :ref:`alpha_antialiasing_edge<class_Label3D_property_alpha_antialiasing_edge>`                             | ``0.0``                                                                                    |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`AlphaAntiAliasing<enum_BaseMaterial3D_AlphaAntiAliasing>`           | :ref:`alpha_antialiasing_mode<class_Label3D_property_alpha_antialiasing_mode>`                             | ``0``                                                                                      |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`AlphaCutMode<enum_Label3D_AlphaCutMode>`                            | :ref:`alpha_cut<class_Label3D_property_alpha_cut>`                                                         | ``0``                                                                                      |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                                 | :ref:`alpha_hash_scale<class_Label3D_property_alpha_hash_scale>`                                           | ``1.0``                                                                                    |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                                 | :ref:`alpha_scissor_threshold<class_Label3D_property_alpha_scissor_threshold>`                             | ``0.5``                                                                                    |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`AutowrapMode<enum_TextServer_AutowrapMode>`                         | :ref:`autowrap_mode<class_Label3D_property_autowrap_mode>`                                                 | ``0``                                                                                      |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | |bitfield|\[:ref:`LineBreakFlag<enum_TextServer_LineBreakFlag>`\]         | :ref:`autowrap_trim_flags<class_Label3D_property_autowrap_trim_flags>`                                     | ``192``                                                                                    |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`BillboardMode<enum_BaseMaterial3D_BillboardMode>`                   | :ref:`billboard<class_Label3D_property_billboard>`                                                         | ``0``                                                                                      |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`ShadowCastingSetting<enum_GeometryInstance3D_ShadowCastingSetting>` | cast_shadow                                                                                                | ``0`` (overrides :ref:`GeometryInstance3D<class_GeometryInstance3D_property_cast_shadow>`) |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                   | :ref:`double_sided<class_Label3D_property_double_sided>`                                                   | ``true``                                                                                   |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                   | :ref:`fixed_size<class_Label3D_property_fixed_size>`                                                       | ``false``                                                                                  |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`Font<class_Font>`                                                   | :ref:`font<class_Label3D_property_font>`                                                                   |                                                                                            |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                     | :ref:`font_size<class_Label3D_property_font_size>`                                                         | ``32``                                                                                     |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`GIMode<enum_GeometryInstance3D_GIMode>`                             | gi_mode                                                                                                    | ``0`` (overrides :ref:`GeometryInstance3D<class_GeometryInstance3D_property_gi_mode>`)     |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`         | :ref:`horizontal_alignment<class_Label3D_property_horizontal_alignment>`                                   | ``1``                                                                                      |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | |bitfield|\[:ref:`JustificationFlag<enum_TextServer_JustificationFlag>`\] | :ref:`justification_flags<class_Label3D_property_justification_flags>`                                     | ``163``                                                                                    |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                               | :ref:`language<class_Label3D_property_language>`                                                           | ``""``                                                                                     |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                                 | :ref:`line_spacing<class_Label3D_property_line_spacing>`                                                   | ``0.0``                                                                                    |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`Color<class_Color>`                                                 | :ref:`modulate<class_Label3D_property_modulate>`                                                           | ``Color(1, 1, 1, 1)``                                                                      |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                   | :ref:`no_depth_test<class_Label3D_property_no_depth_test>`                                                 | ``false``                                                                                  |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`                                             | :ref:`offset<class_Label3D_property_offset>`                                                               | ``Vector2(0, 0)``                                                                          |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`Color<class_Color>`                                                 | :ref:`outline_modulate<class_Label3D_property_outline_modulate>`                                           | ``Color(0, 0, 0, 1)``                                                                      |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                     | :ref:`outline_render_priority<class_Label3D_property_outline_render_priority>`                             | ``-1``                                                                                     |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                     | :ref:`outline_size<class_Label3D_property_outline_size>`                                                   | ``12``                                                                                     |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                                 | :ref:`pixel_size<class_Label3D_property_pixel_size>`                                                       | ``0.005``                                                                                  |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                     | :ref:`render_priority<class_Label3D_property_render_priority>`                                             | ``0``                                                                                      |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                   | :ref:`shaded<class_Label3D_property_shaded>`                                                               | ``false``                                                                                  |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`StructuredTextParser<enum_TextServer_StructuredTextParser>`         | :ref:`structured_text_bidi_override<class_Label3D_property_structured_text_bidi_override>`                 | ``0``                                                                                      |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`                                                 | :ref:`structured_text_bidi_override_options<class_Label3D_property_structured_text_bidi_override_options>` | ``[]``                                                                                     |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                               | :ref:`text<class_Label3D_property_text>`                                                                   | ``""``                                                                                     |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`Direction<enum_TextServer_Direction>`                               | :ref:`text_direction<class_Label3D_property_text_direction>`                                               | ``0``                                                                                      |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`TextureFilter<enum_BaseMaterial3D_TextureFilter>`                   | :ref:`texture_filter<class_Label3D_property_texture_filter>`                                               | ``3``                                                                                      |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                   | :ref:`uppercase<class_Label3D_property_uppercase>`                                                         | ``false``                                                                                  |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`VerticalAlignment<enum_@GlobalScope_VerticalAlignment>`             | :ref:`vertical_alignment<class_Label3D_property_vertical_alignment>`                                       | ``1``                                                                                      |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                                 | :ref:`width<class_Label3D_property_width>`                                                                 | ``500.0``                                                                                  |
> +---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`TriangleMesh<class_TriangleMesh>` | :ref:`generate_triangle_mesh<class_Label3D_method_generate_triangle_mesh>`\ (\ ) |const|                                                           |
> +-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                 | :ref:`get_draw_flag<class_Label3D_method_get_draw_flag>`\ (\ flag\: :ref:`DrawFlags<enum_Label3D_DrawFlags>`\ ) |const|                            |
> +-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                  | :ref:`set_draw_flag<class_Label3D_method_set_draw_flag>`\ (\ flag\: :ref:`DrawFlags<enum_Label3D_DrawFlags>`, enabled\: :ref:`bool<class_bool>`\ ) |
> +-----------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **DrawFlags**: [🔗<enum_Label3D_DrawFlags>]



[DrawFlags<enum_Label3D_DrawFlags>] **FLAG_SHADED** = `0`

If set, lights in the environment affect the label.



[DrawFlags<enum_Label3D_DrawFlags>] **FLAG_DOUBLE_SIDED** = `1`

If set, text can be seen from the back as well. If not, the text is invisible when looking at it from behind.



[DrawFlags<enum_Label3D_DrawFlags>] **FLAG_DISABLE_DEPTH_TEST** = `2`

Disables the depth test, so this object is drawn on top of all others. However, objects drawn after it in the draw order may cover it.



[DrawFlags<enum_Label3D_DrawFlags>] **FLAG_FIXED_SIZE** = `3`

Label is scaled by depth so that it always appears the same size on screen.



[DrawFlags<enum_Label3D_DrawFlags>] **FLAG_MAX** = `4`

Represents the size of the [DrawFlags<enum_Label3D_DrawFlags>] enum.


----



enum **AlphaCutMode**: [🔗<enum_Label3D_AlphaCutMode>]



[AlphaCutMode<enum_Label3D_AlphaCutMode>] **ALPHA_CUT_DISABLED** = `0`

This mode performs standard alpha blending. It can display translucent areas, but transparency sorting issues may be visible when multiple transparent materials are overlapping. [GeometryInstance3D.cast_shadow<class_GeometryInstance3D_property_cast_shadow>] has no effect when this transparency mode is used; the **Label3D** will never cast shadows.



[AlphaCutMode<enum_Label3D_AlphaCutMode>] **ALPHA_CUT_DISCARD** = `1`

This mode only allows fully transparent or fully opaque pixels. Harsh edges will be visible unless some form of screen-space antialiasing is enabled (see [ProjectSettings.rendering/anti_aliasing/quality/screen_space_aa<class_ProjectSettings_property_rendering/anti_aliasing/quality/screen_space_aa>]). This mode is also known as *alpha testing* or *1-bit transparency*.

\ **Note:** This mode might have issues with anti-aliased fonts and outlines, try adjusting [alpha_scissor_threshold<class_Label3D_property_alpha_scissor_threshold>] or using MSDF font.

\ **Note:** When using text with overlapping glyphs (e.g., cursive scripts), this mode might have transparency sorting issues between the main text and the outline.



[AlphaCutMode<enum_Label3D_AlphaCutMode>] **ALPHA_CUT_OPAQUE_PREPASS** = `2`

This mode draws fully opaque pixels in the depth prepass. This is slower than [ALPHA_CUT_DISABLED<class_Label3D_constant_ALPHA_CUT_DISABLED>] or [ALPHA_CUT_DISCARD<class_Label3D_constant_ALPHA_CUT_DISCARD>], but it allows displaying translucent areas and smooth edges while using proper sorting.

\ **Note:** When using text with overlapping glyphs (e.g., cursive scripts), this mode might have transparency sorting issues between the main text and the outline.



[AlphaCutMode<enum_Label3D_AlphaCutMode>] **ALPHA_CUT_HASH** = `3`

This mode draws cuts off all values below a spatially-deterministic threshold, the rest will remain opaque.


----


## Property Descriptions



[float<class_float>] **alpha_antialiasing_edge** = `0.0` [🔗<class_Label3D_property_alpha_antialiasing_edge>]


- |void| **set_alpha_antialiasing_edge**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_alpha_antialiasing_edge**\ (\ )

Threshold at which antialiasing will be applied on the alpha channel.


----



[AlphaAntiAliasing<enum_BaseMaterial3D_AlphaAntiAliasing>] **alpha_antialiasing_mode** = `0` [🔗<class_Label3D_property_alpha_antialiasing_mode>]


- |void| **set_alpha_antialiasing**\ (\ value\: [AlphaAntiAliasing<enum_BaseMaterial3D_AlphaAntiAliasing>]\ )
- [AlphaAntiAliasing<enum_BaseMaterial3D_AlphaAntiAliasing>] **get_alpha_antialiasing**\ (\ )

The type of alpha antialiasing to apply.


----



[AlphaCutMode<enum_Label3D_AlphaCutMode>] **alpha_cut** = `0` [🔗<class_Label3D_property_alpha_cut>]


- |void| **set_alpha_cut_mode**\ (\ value\: [AlphaCutMode<enum_Label3D_AlphaCutMode>]\ )
- [AlphaCutMode<enum_Label3D_AlphaCutMode>] **get_alpha_cut_mode**\ (\ )

The alpha cutting mode to use for the sprite.


----



[float<class_float>] **alpha_hash_scale** = `1.0` [🔗<class_Label3D_property_alpha_hash_scale>]


- |void| **set_alpha_hash_scale**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_alpha_hash_scale**\ (\ )

The hashing scale for Alpha Hash. Recommended values between `0` and `2`.


----



[float<class_float>] **alpha_scissor_threshold** = `0.5` [🔗<class_Label3D_property_alpha_scissor_threshold>]


- |void| **set_alpha_scissor_threshold**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_alpha_scissor_threshold**\ (\ )

Threshold at which the alpha scissor will discard values.


----



[AutowrapMode<enum_TextServer_AutowrapMode>] **autowrap_mode** = `0` [🔗<class_Label3D_property_autowrap_mode>]


- |void| **set_autowrap_mode**\ (\ value\: [AutowrapMode<enum_TextServer_AutowrapMode>]\ )
- [AutowrapMode<enum_TextServer_AutowrapMode>] **get_autowrap_mode**\ (\ )

If set to something other than [TextServer.AUTOWRAP_OFF<class_TextServer_constant_AUTOWRAP_OFF>], the text gets wrapped inside the node's bounding rectangle. If you resize the node, it will change its height automatically to show all the text.


----



|bitfield|\[[LineBreakFlag<enum_TextServer_LineBreakFlag>]\] **autowrap_trim_flags** = `192` [🔗<class_Label3D_property_autowrap_trim_flags>]


- |void| **set_autowrap_trim_flags**\ (\ value\: |bitfield|\[[LineBreakFlag<enum_TextServer_LineBreakFlag>]\]\ )
- |bitfield|\[[LineBreakFlag<enum_TextServer_LineBreakFlag>]\] **get_autowrap_trim_flags**\ (\ )

Autowrap space trimming flags. See [TextServer.BREAK_TRIM_START_EDGE_SPACES<class_TextServer_constant_BREAK_TRIM_START_EDGE_SPACES>] and [TextServer.BREAK_TRIM_END_EDGE_SPACES<class_TextServer_constant_BREAK_TRIM_END_EDGE_SPACES>] for more info.


----



[BillboardMode<enum_BaseMaterial3D_BillboardMode>] **billboard** = `0` [🔗<class_Label3D_property_billboard>]


- |void| **set_billboard_mode**\ (\ value\: [BillboardMode<enum_BaseMaterial3D_BillboardMode>]\ )
- [BillboardMode<enum_BaseMaterial3D_BillboardMode>] **get_billboard_mode**\ (\ )

The billboard mode to use for the label.


----



[bool<class_bool>] **double_sided** = `true` [🔗<class_Label3D_property_double_sided>]


- |void| **set_draw_flag**\ (\ flag\: [DrawFlags<enum_Label3D_DrawFlags>], enabled\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_draw_flag**\ (\ flag\: [DrawFlags<enum_Label3D_DrawFlags>]\ ) |const|

If `true`, text can be seen from the back as well, if `false`, it is invisible when looking at it from behind.


----



[bool<class_bool>] **fixed_size** = `false` [🔗<class_Label3D_property_fixed_size>]


- |void| **set_draw_flag**\ (\ flag\: [DrawFlags<enum_Label3D_DrawFlags>], enabled\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_draw_flag**\ (\ flag\: [DrawFlags<enum_Label3D_DrawFlags>]\ ) |const|

If `true`, the label is rendered at the same size regardless of distance. The label's size on screen is the same as if the camera was `1.0` units away from the label's origin, regardless of the actual distance from the camera. The [Camera3D<class_Camera3D>]'s field of view (or [Camera3D.size<class_Camera3D_property_size>] when in orthogonal/frustum mode) still affects the size the label is drawn at.


----



[Font<class_Font>] **font** [🔗<class_Label3D_property_font>]


- |void| **set_font**\ (\ value\: [Font<class_Font>]\ )
- [Font<class_Font>] **get_font**\ (\ )

Font configuration used to display text.


----



[int<class_int>] **font_size** = `32` [🔗<class_Label3D_property_font_size>]


- |void| **set_font_size**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_font_size**\ (\ )

Font size of the **Label3D**'s text. To make the font look more detailed when up close, increase [font_size<class_Label3D_property_font_size>] while decreasing [pixel_size<class_Label3D_property_pixel_size>] at the same time.

Higher font sizes require more time to render new characters, which can cause stuttering during gameplay.


----



[HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>] **horizontal_alignment** = `1` [🔗<class_Label3D_property_horizontal_alignment>]


- |void| **set_horizontal_alignment**\ (\ value\: [HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>]\ )
- [HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>] **get_horizontal_alignment**\ (\ )

Controls the text's horizontal alignment. Supports left, center, right, and fill (also known as justify).


----



|bitfield|\[[JustificationFlag<enum_TextServer_JustificationFlag>]\] **justification_flags** = `163` [🔗<class_Label3D_property_justification_flags>]


- |void| **set_justification_flags**\ (\ value\: |bitfield|\[[JustificationFlag<enum_TextServer_JustificationFlag>]\]\ )
- |bitfield|\[[JustificationFlag<enum_TextServer_JustificationFlag>]\] **get_justification_flags**\ (\ )

Line fill alignment rules.


----



[String<class_String>] **language** = `""` [🔗<class_Label3D_property_language>]


- |void| **set_language**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_language**\ (\ )

Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.


----



[float<class_float>] **line_spacing** = `0.0` [🔗<class_Label3D_property_line_spacing>]


- |void| **set_line_spacing**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_line_spacing**\ (\ )

Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.


----



[Color<class_Color>] **modulate** = `Color(1, 1, 1, 1)` [🔗<class_Label3D_property_modulate>]


- |void| **set_modulate**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_modulate**\ (\ )

Text [Color<class_Color>] of the **Label3D**.


----



[bool<class_bool>] **no_depth_test** = `false` [🔗<class_Label3D_property_no_depth_test>]


- |void| **set_draw_flag**\ (\ flag\: [DrawFlags<enum_Label3D_DrawFlags>], enabled\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_draw_flag**\ (\ flag\: [DrawFlags<enum_Label3D_DrawFlags>]\ ) |const|

If `true`, depth testing is disabled and the object will be drawn in render order.


----



[Vector2<class_Vector2>] **offset** = `Vector2(0, 0)` [🔗<class_Label3D_property_offset>]


- |void| **set_offset**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_offset**\ (\ )

The text drawing offset (in pixels).


----



[Color<class_Color>] **outline_modulate** = `Color(0, 0, 0, 1)` [🔗<class_Label3D_property_outline_modulate>]


- |void| **set_outline_modulate**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_outline_modulate**\ (\ )

The tint of text outline.


----



[int<class_int>] **outline_render_priority** = `-1` [🔗<class_Label3D_property_outline_render_priority>]


- |void| **set_outline_render_priority**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_outline_render_priority**\ (\ )

Sets the render priority for the text outline. Higher priority objects will be sorted in front of lower priority objects.

\ **Note:** This only applies if [alpha_cut<class_Label3D_property_alpha_cut>] is set to [ALPHA_CUT_DISABLED<class_Label3D_constant_ALPHA_CUT_DISABLED>] (default value).

\ **Note:** This only applies to sorting of transparent objects. This will not impact how transparent objects are sorted relative to opaque objects. This is because opaque objects are not sorted, while transparent objects are sorted from back to front (subject to priority).


----



[int<class_int>] **outline_size** = `12` [🔗<class_Label3D_property_outline_size>]


- |void| **set_outline_size**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_outline_size**\ (\ )

Text outline size.


----



[float<class_float>] **pixel_size** = `0.005` [🔗<class_Label3D_property_pixel_size>]


- |void| **set_pixel_size**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_pixel_size**\ (\ )

The size of one pixel's width on the label to scale it in 3D. To make the font look more detailed when up close, increase [font_size<class_Label3D_property_font_size>] while decreasing [pixel_size<class_Label3D_property_pixel_size>] at the same time.


----



[int<class_int>] **render_priority** = `0` [🔗<class_Label3D_property_render_priority>]


- |void| **set_render_priority**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_render_priority**\ (\ )

Sets the render priority for the text. Higher priority objects will be sorted in front of lower priority objects.

\ **Note:** This only applies if [alpha_cut<class_Label3D_property_alpha_cut>] is set to [ALPHA_CUT_DISABLED<class_Label3D_constant_ALPHA_CUT_DISABLED>] (default value).

\ **Note:** This only applies to sorting of transparent objects. This will not impact how transparent objects are sorted relative to opaque objects. This is because opaque objects are not sorted, while transparent objects are sorted from back to front (subject to priority).


----



[bool<class_bool>] **shaded** = `false` [🔗<class_Label3D_property_shaded>]


- |void| **set_draw_flag**\ (\ flag\: [DrawFlags<enum_Label3D_DrawFlags>], enabled\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_draw_flag**\ (\ flag\: [DrawFlags<enum_Label3D_DrawFlags>]\ ) |const|

If `true`, the [Light3D<class_Light3D>] in the [Environment<class_Environment>] has effects on the label.


----



[StructuredTextParser<enum_TextServer_StructuredTextParser>] **structured_text_bidi_override** = `0` [🔗<class_Label3D_property_structured_text_bidi_override>]


- |void| **set_structured_text_bidi_override**\ (\ value\: [StructuredTextParser<enum_TextServer_StructuredTextParser>]\ )
- [StructuredTextParser<enum_TextServer_StructuredTextParser>] **get_structured_text_bidi_override**\ (\ )

Set BiDi algorithm override for the structured text.


----



[Array<class_Array>] **structured_text_bidi_override_options** = `[]` [🔗<class_Label3D_property_structured_text_bidi_override_options>]


- |void| **set_structured_text_bidi_override_options**\ (\ value\: [Array<class_Array>]\ )
- [Array<class_Array>] **get_structured_text_bidi_override_options**\ (\ )

Set additional options for BiDi override.


----



[String<class_String>] **text** = `""` [🔗<class_Label3D_property_text>]


- |void| **set_text**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_text**\ (\ )

The text to display on screen.


----



[Direction<enum_TextServer_Direction>] **text_direction** = `0` [🔗<class_Label3D_property_text_direction>]


- |void| **set_text_direction**\ (\ value\: [Direction<enum_TextServer_Direction>]\ )
- [Direction<enum_TextServer_Direction>] **get_text_direction**\ (\ )

Base text writing direction.


----



[TextureFilter<enum_BaseMaterial3D_TextureFilter>] **texture_filter** = `3` [🔗<class_Label3D_property_texture_filter>]


- |void| **set_texture_filter**\ (\ value\: [TextureFilter<enum_BaseMaterial3D_TextureFilter>]\ )
- [TextureFilter<enum_BaseMaterial3D_TextureFilter>] **get_texture_filter**\ (\ )

Filter flags for the texture.


----



[bool<class_bool>] **uppercase** = `false` [🔗<class_Label3D_property_uppercase>]


- |void| **set_uppercase**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_uppercase**\ (\ )

If `true`, all the text displays as UPPERCASE.


----



[VerticalAlignment<enum_@GlobalScope_VerticalAlignment>] **vertical_alignment** = `1` [🔗<class_Label3D_property_vertical_alignment>]


- |void| **set_vertical_alignment**\ (\ value\: [VerticalAlignment<enum_@GlobalScope_VerticalAlignment>]\ )
- [VerticalAlignment<enum_@GlobalScope_VerticalAlignment>] **get_vertical_alignment**\ (\ )

Controls the text's vertical alignment. Supports top, center, and bottom.


----



[float<class_float>] **width** = `500.0` [🔗<class_Label3D_property_width>]


- |void| **set_width**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_width**\ (\ )

Text width (in pixels), used for autowrap and fill alignment.


----


## Method Descriptions



[TriangleMesh<class_TriangleMesh>] **generate_triangle_mesh**\ (\ ) |const| [🔗<class_Label3D_method_generate_triangle_mesh>]

Returns a [TriangleMesh<class_TriangleMesh>] with the label's vertices following its current configuration (such as its [pixel_size<class_Label3D_property_pixel_size>]).


----



[bool<class_bool>] **get_draw_flag**\ (\ flag\: [DrawFlags<enum_Label3D_DrawFlags>]\ ) |const| [🔗<class_Label3D_method_get_draw_flag>]

Returns the value of the specified flag.


----



|void| **set_draw_flag**\ (\ flag\: [DrawFlags<enum_Label3D_DrawFlags>], enabled\: [bool<class_bool>]\ ) [🔗<class_Label3D_method_set_draw_flag>]

If `true`, the specified `flag` will be enabled.

