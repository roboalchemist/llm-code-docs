:github_url: hide



# SystemFont

**Inherits:** [Font<class_Font>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A font loaded from a system font. Falls back to a default theme font if not implemented on the host OS.


## Description

**SystemFont** loads a font from a system font with the first matching name from [font_names<class_SystemFont_property_font_names>].

It will attempt to match font style, but it's not guaranteed.

The returned font might be part of a font collection or be a variable font with OpenType "weight", "width" and/or "italic" features set.

You can create [FontVariation<class_FontVariation>] of the system font for precise control over its features.

\ **Note:** This class is implemented on iOS, Linux, macOS and Windows, on other platforms it will fallback to default theme font.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`bool<class_bool>`                                         | :ref:`allow_system_fallback<class_SystemFont_property_allow_system_fallback>`                           | ``true``                |
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`FontAntialiasing<enum_TextServer_FontAntialiasing>`       | :ref:`antialiasing<class_SystemFont_property_antialiasing>`                                             | ``1``                   |
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`bool<class_bool>`                                         | :ref:`disable_embedded_bitmaps<class_SystemFont_property_disable_embedded_bitmaps>`                     | ``true``                |
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`bool<class_bool>`                                         | :ref:`font_italic<class_SystemFont_property_font_italic>`                                               | ``false``               |
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>`               | :ref:`font_names<class_SystemFont_property_font_names>`                                                 | ``PackedStringArray()`` |
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`int<class_int>`                                           | :ref:`font_stretch<class_SystemFont_property_font_stretch>`                                             | ``100``                 |
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`int<class_int>`                                           | :ref:`font_weight<class_SystemFont_property_font_weight>`                                               | ``400``                 |
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`bool<class_bool>`                                         | :ref:`force_autohinter<class_SystemFont_property_force_autohinter>`                                     | ``false``               |
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`bool<class_bool>`                                         | :ref:`generate_mipmaps<class_SystemFont_property_generate_mipmaps>`                                     | ``false``               |
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`Hinting<enum_TextServer_Hinting>`                         | :ref:`hinting<class_SystemFont_property_hinting>`                                                       | ``1``                   |
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`bool<class_bool>`                                         | :ref:`keep_rounding_remainders<class_SystemFont_property_keep_rounding_remainders>`                     | ``true``                |
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`bool<class_bool>`                                         | :ref:`modulate_color_glyphs<class_SystemFont_property_modulate_color_glyphs>`                           | ``false``               |
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`int<class_int>`                                           | :ref:`msdf_pixel_range<class_SystemFont_property_msdf_pixel_range>`                                     | ``16``                  |
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`int<class_int>`                                           | :ref:`msdf_size<class_SystemFont_property_msdf_size>`                                                   | ``48``                  |
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`bool<class_bool>`                                         | :ref:`multichannel_signed_distance_field<class_SystemFont_property_multichannel_signed_distance_field>` | ``false``               |
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`float<class_float>`                                       | :ref:`oversampling<class_SystemFont_property_oversampling>`                                             | ``0.0``                 |
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`SubpixelPositioning<enum_TextServer_SubpixelPositioning>` | :ref:`subpixel_positioning<class_SystemFont_property_subpixel_positioning>`                             | ``1``                   |
> +-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+-------------------------+
>

----


## Property Descriptions



[bool<class_bool>] **allow_system_fallback** = `true` [🔗<class_SystemFont_property_allow_system_fallback>]


- |void| **set_allow_system_fallback**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_allow_system_fallback**\ (\ )

If set to `true`, system fonts can be automatically used as fallbacks.


----



[FontAntialiasing<enum_TextServer_FontAntialiasing>] **antialiasing** = `1` [🔗<class_SystemFont_property_antialiasing>]


- |void| **set_antialiasing**\ (\ value\: [FontAntialiasing<enum_TextServer_FontAntialiasing>]\ )
- [FontAntialiasing<enum_TextServer_FontAntialiasing>] **get_antialiasing**\ (\ )

Font anti-aliasing mode.


----



[bool<class_bool>] **disable_embedded_bitmaps** = `true` [🔗<class_SystemFont_property_disable_embedded_bitmaps>]


- |void| **set_disable_embedded_bitmaps**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_disable_embedded_bitmaps**\ (\ )

If set to `true`, embedded font bitmap loading is disabled (bitmap-only and color fonts ignore this property).


----



[bool<class_bool>] **font_italic** = `false` [🔗<class_SystemFont_property_font_italic>]


- |void| **set_font_italic**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_font_italic**\ (\ )

If set to `true`, italic or oblique font is preferred.


----



[PackedStringArray<class_PackedStringArray>] **font_names** = `PackedStringArray()` [🔗<class_SystemFont_property_font_names>]


- |void| **set_font_names**\ (\ value\: [PackedStringArray<class_PackedStringArray>]\ )
- [PackedStringArray<class_PackedStringArray>] **get_font_names**\ (\ )

Array of font family names to search, first matching font found is used.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray<class_PackedStringArray>] for more details.


----



[int<class_int>] **font_stretch** = `100` [🔗<class_SystemFont_property_font_stretch>]


- |void| **set_font_stretch**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_font_stretch**\ (\ )

Preferred font stretch amount, compared to a normal width. A percentage value between `50%` and `200%`.


----



[int<class_int>] **font_weight** = `400` [🔗<class_SystemFont_property_font_weight>]


- |void| **set_font_weight**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_font_weight**\ (\ )

Preferred weight (boldness) of the font. A value in the `100...999` range, normal font weight is `400`, bold font weight is `700`.


----



[bool<class_bool>] **force_autohinter** = `false` [🔗<class_SystemFont_property_force_autohinter>]


- |void| **set_force_autohinter**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_force_autohinter**\ (\ )

If set to `true`, auto-hinting is supported and preferred over font built-in hinting.


----



[bool<class_bool>] **generate_mipmaps** = `false` [🔗<class_SystemFont_property_generate_mipmaps>]


- |void| **set_generate_mipmaps**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_generate_mipmaps**\ (\ )

If set to `true`, generate mipmaps for the font textures.


----



[Hinting<enum_TextServer_Hinting>] **hinting** = `1` [🔗<class_SystemFont_property_hinting>]


- |void| **set_hinting**\ (\ value\: [Hinting<enum_TextServer_Hinting>]\ )
- [Hinting<enum_TextServer_Hinting>] **get_hinting**\ (\ )

Font hinting mode.


----



[bool<class_bool>] **keep_rounding_remainders** = `true` [🔗<class_SystemFont_property_keep_rounding_remainders>]


- |void| **set_keep_rounding_remainders**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_keep_rounding_remainders**\ (\ )

If set to `true`, when aligning glyphs to the pixel boundaries rounding remainders are accumulated to ensure more uniform glyph distribution. This setting has no effect if subpixel positioning is enabled.


----



[bool<class_bool>] **modulate_color_glyphs** = `false` [🔗<class_SystemFont_property_modulate_color_glyphs>]


- |void| **set_modulate_color_glyphs**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_modulate_color_glyphs**\ (\ )

If set to `true`, color modulation is applied when drawing colored glyphs, otherwise it's applied to the monochrome glyphs only.


----



[int<class_int>] **msdf_pixel_range** = `16` [🔗<class_SystemFont_property_msdf_pixel_range>]


- |void| **set_msdf_pixel_range**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_msdf_pixel_range**\ (\ )

The width of the range around the shape between the minimum and maximum representable signed distance. If using font outlines, [msdf_pixel_range<class_SystemFont_property_msdf_pixel_range>] must be set to at least *twice* the size of the largest font outline. The default [msdf_pixel_range<class_SystemFont_property_msdf_pixel_range>] value of `16` allows outline sizes up to `8` to look correct.


----



[int<class_int>] **msdf_size** = `48` [🔗<class_SystemFont_property_msdf_size>]


- |void| **set_msdf_size**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_msdf_size**\ (\ )

Source font size used to generate MSDF textures. Higher values allow for more precision, but are slower to render and require more memory. Only increase this value if you notice a visible lack of precision in glyph rendering.


----



[bool<class_bool>] **multichannel_signed_distance_field** = `false` [🔗<class_SystemFont_property_multichannel_signed_distance_field>]


- |void| **set_multichannel_signed_distance_field**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_multichannel_signed_distance_field**\ (\ )

If set to `true`, glyphs of all sizes are rendered using single multichannel signed distance field generated from the dynamic font vector data.


----



[float<class_float>] **oversampling** = `0.0` [🔗<class_SystemFont_property_oversampling>]


- |void| **set_oversampling**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_oversampling**\ (\ )

If set to a positive value, overrides the oversampling factor of the viewport this font is used in. See [Viewport.oversampling<class_Viewport_property_oversampling>]. This value doesn't override the `oversampling` parameter of `draw_*` methods.


----



[SubpixelPositioning<enum_TextServer_SubpixelPositioning>] **subpixel_positioning** = `1` [🔗<class_SystemFont_property_subpixel_positioning>]


- |void| **set_subpixel_positioning**\ (\ value\: [SubpixelPositioning<enum_TextServer_SubpixelPositioning>]\ )
- [SubpixelPositioning<enum_TextServer_SubpixelPositioning>] **get_subpixel_positioning**\ (\ )

Font glyph subpixel positioning mode. Subpixel positioning provides shaper text and better kerning for smaller font sizes, at the cost of memory usage and font rasterization speed. Use [TextServer.SUBPIXEL_POSITIONING_AUTO<class_TextServer_constant_SUBPIXEL_POSITIONING_AUTO>] to automatically enable it based on the font size.

