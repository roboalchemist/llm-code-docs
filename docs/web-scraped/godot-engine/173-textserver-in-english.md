# TextServer in English

# TextServer

Inherits:RefCounted<Object
Inherited By:TextServerExtension
A server interface for font management and text rendering.

## Description

TextServeris the API backend for managing fonts and rendering text.
Note:This is a low-level API, consider usingTextLine,TextParagraph, andFontclasses instead.
This is an abstract class, so to get the currently activeTextServerinstance, use the following code:

```
var ts = TextServerManager.get_primary_interface()
```

```
var ts = TextServerManager.GetPrimaryInterface();
```

## Methods

| RID | create_font() |
|---|---|
| RID | create_font_linked_variation(font_rid:RID) |
| RID | create_shaped_text(direction:Direction= 0, orientation:Orientation= 0) |
| void | draw_hex_code_box(canvas:RID, size:int, pos:Vector2, index:int, color:Color)const |
| void | font_clear_glyphs(font_rid:RID, size:Vector2i) |
| void | font_clear_kerning_map(font_rid:RID, size:int) |
| void | font_clear_size_cache(font_rid:RID) |
| void | font_clear_system_fallback_cache() |
| void | font_clear_textures(font_rid:RID, size:Vector2i) |
| void | font_draw_glyph(font_rid:RID, canvas:RID, size:int, pos:Vector2, index:int, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const |
| void | font_draw_glyph_outline(font_rid:RID, canvas:RID, size:int, outline_size:int, pos:Vector2, index:int, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const |
| FontAntialiasing | font_get_antialiasing(font_rid:RID)const |
| float | font_get_ascent(font_rid:RID, size:int)const |
| float | font_get_baseline_offset(font_rid:RID)const |
| int | font_get_char_from_glyph_index(font_rid:RID, size:int, glyph_index:int)const |
| float | font_get_descent(font_rid:RID, size:int)const |
| bool | font_get_disable_embedded_bitmaps(font_rid:RID)const |
| float | font_get_embolden(font_rid:RID)const |
| int | font_get_face_count(font_rid:RID)const |
| int | font_get_face_index(font_rid:RID)const |
| int | font_get_fixed_size(font_rid:RID)const |
| FixedSizeScaleMode | font_get_fixed_size_scale_mode(font_rid:RID)const |
| bool | font_get_generate_mipmaps(font_rid:RID)const |
| float | font_get_global_oversampling()const |
| Vector2 | font_get_glyph_advance(font_rid:RID, size:int, glyph:int)const |
| Dictionary | font_get_glyph_contours(font:RID, size:int, index:int)const |
| int | font_get_glyph_index(font_rid:RID, size:int, char:int, variation_selector:int)const |
| PackedInt32Array | font_get_glyph_list(font_rid:RID, size:Vector2i)const |
| Vector2 | font_get_glyph_offset(font_rid:RID, size:Vector2i, glyph:int)const |
| Vector2 | font_get_glyph_size(font_rid:RID, size:Vector2i, glyph:int)const |
| int | font_get_glyph_texture_idx(font_rid:RID, size:Vector2i, glyph:int)const |
| RID | font_get_glyph_texture_rid(font_rid:RID, size:Vector2i, glyph:int)const |
| Vector2 | font_get_glyph_texture_size(font_rid:RID, size:Vector2i, glyph:int)const |
| Rect2 | font_get_glyph_uv_rect(font_rid:RID, size:Vector2i, glyph:int)const |
| Hinting | font_get_hinting(font_rid:RID)const |
| bool | font_get_keep_rounding_remainders(font_rid:RID)const |
| Vector2 | font_get_kerning(font_rid:RID, size:int, glyph_pair:Vector2i)const |
| Array[Vector2i] | font_get_kerning_list(font_rid:RID, size:int)const |
| bool | font_get_language_support_override(font_rid:RID, language:String) |
| PackedStringArray | font_get_language_support_overrides(font_rid:RID) |
| int | font_get_msdf_pixel_range(font_rid:RID)const |
| int | font_get_msdf_size(font_rid:RID)const |
| String | font_get_name(font_rid:RID)const |
| Dictionary | font_get_opentype_feature_overrides(font_rid:RID)const |
| Dictionary | font_get_ot_name_strings(font_rid:RID)const |
| float | font_get_oversampling(font_rid:RID)const |
| float | font_get_scale(font_rid:RID, size:int)const |
| bool | font_get_script_support_override(font_rid:RID, script:String) |
| PackedStringArray | font_get_script_support_overrides(font_rid:RID) |
| Array[Dictionary] | font_get_size_cache_info(font_rid:RID)const |
| Array[Vector2i] | font_get_size_cache_list(font_rid:RID)const |
| int | font_get_spacing(font_rid:RID, spacing:SpacingType)const |
| int | font_get_stretch(font_rid:RID)const |
| BitField[FontStyle] | font_get_style(font_rid:RID)const |
| String | font_get_style_name(font_rid:RID)const |
| SubpixelPositioning | font_get_subpixel_positioning(font_rid:RID)const |
| String | font_get_supported_chars(font_rid:RID)const |
| PackedInt32Array | font_get_supported_glyphs(font_rid:RID)const |
| int | font_get_texture_count(font_rid:RID, size:Vector2i)const |
| Image | font_get_texture_image(font_rid:RID, size:Vector2i, texture_index:int)const |
| PackedInt32Array | font_get_texture_offsets(font_rid:RID, size:Vector2i, texture_index:int)const |
| Transform2D | font_get_transform(font_rid:RID)const |
| float | font_get_underline_position(font_rid:RID, size:int)const |
| float | font_get_underline_thickness(font_rid:RID, size:int)const |
| Dictionary | font_get_variation_coordinates(font_rid:RID)const |
| int | font_get_weight(font_rid:RID)const |
| bool | font_has_char(font_rid:RID, char:int)const |
| bool | font_is_allow_system_fallback(font_rid:RID)const |
| bool | font_is_force_autohinter(font_rid:RID)const |
| bool | font_is_language_supported(font_rid:RID, language:String)const |
| bool | font_is_modulate_color_glyphs(font_rid:RID)const |
| bool | font_is_multichannel_signed_distance_field(font_rid:RID)const |
| bool | font_is_script_supported(font_rid:RID, script:String)const |
| void | font_remove_glyph(font_rid:RID, size:Vector2i, glyph:int) |
| void | font_remove_kerning(font_rid:RID, size:int, glyph_pair:Vector2i) |
| void | font_remove_language_support_override(font_rid:RID, language:String) |
| void | font_remove_script_support_override(font_rid:RID, script:String) |
| void | font_remove_size_cache(font_rid:RID, size:Vector2i) |
| void | font_remove_texture(font_rid:RID, size:Vector2i, texture_index:int) |
| void | font_render_glyph(font_rid:RID, size:Vector2i, index:int) |
| void | font_render_range(font_rid:RID, size:Vector2i, start:int, end:int) |
| void | font_set_allow_system_fallback(font_rid:RID, allow_system_fallback:bool) |
| void | font_set_antialiasing(font_rid:RID, antialiasing:FontAntialiasing) |
| void | font_set_ascent(font_rid:RID, size:int, ascent:float) |
| void | font_set_baseline_offset(font_rid:RID, baseline_offset:float) |
| void | font_set_data(font_rid:RID, data:PackedByteArray) |
| void | font_set_descent(font_rid:RID, size:int, descent:float) |
| void | font_set_disable_embedded_bitmaps(font_rid:RID, disable_embedded_bitmaps:bool) |
| void | font_set_embolden(font_rid:RID, strength:float) |
| void | font_set_face_index(font_rid:RID, face_index:int) |
| void | font_set_fixed_size(font_rid:RID, fixed_size:int) |
| void | font_set_fixed_size_scale_mode(font_rid:RID, fixed_size_scale_mode:FixedSizeScaleMode) |
| void | font_set_force_autohinter(font_rid:RID, force_autohinter:bool) |
| void | font_set_generate_mipmaps(font_rid:RID, generate_mipmaps:bool) |
| void | font_set_global_oversampling(oversampling:float) |
| void | font_set_glyph_advance(font_rid:RID, size:int, glyph:int, advance:Vector2) |
| void | font_set_glyph_offset(font_rid:RID, size:Vector2i, glyph:int, offset:Vector2) |
| void | font_set_glyph_size(font_rid:RID, size:Vector2i, glyph:int, gl_size:Vector2) |
| void | font_set_glyph_texture_idx(font_rid:RID, size:Vector2i, glyph:int, texture_idx:int) |
| void | font_set_glyph_uv_rect(font_rid:RID, size:Vector2i, glyph:int, uv_rect:Rect2) |
| void | font_set_hinting(font_rid:RID, hinting:Hinting) |
| void | font_set_keep_rounding_remainders(font_rid:RID, keep_rounding_remainders:bool) |
| void | font_set_kerning(font_rid:RID, size:int, glyph_pair:Vector2i, kerning:Vector2) |
| void | font_set_language_support_override(font_rid:RID, language:String, supported:bool) |
| void | font_set_modulate_color_glyphs(font_rid:RID, force_autohinter:bool) |
| void | font_set_msdf_pixel_range(font_rid:RID, msdf_pixel_range:int) |
| void | font_set_msdf_size(font_rid:RID, msdf_size:int) |
| void | font_set_multichannel_signed_distance_field(font_rid:RID, msdf:bool) |
| void | font_set_name(font_rid:RID, name:String) |
| void | font_set_opentype_feature_overrides(font_rid:RID, overrides:Dictionary) |
| void | font_set_oversampling(font_rid:RID, oversampling:float) |
| void | font_set_scale(font_rid:RID, size:int, scale:float) |
| void | font_set_script_support_override(font_rid:RID, script:String, supported:bool) |
| void | font_set_spacing(font_rid:RID, spacing:SpacingType, value:int) |
| void | font_set_stretch(font_rid:RID, weight:int) |
| void | font_set_style(font_rid:RID, style:BitField[FontStyle]) |
| void | font_set_style_name(font_rid:RID, name:String) |
| void | font_set_subpixel_positioning(font_rid:RID, subpixel_positioning:SubpixelPositioning) |
| void | font_set_texture_image(font_rid:RID, size:Vector2i, texture_index:int, image:Image) |
| void | font_set_texture_offsets(font_rid:RID, size:Vector2i, texture_index:int, offset:PackedInt32Array) |
| void | font_set_transform(font_rid:RID, transform:Transform2D) |
| void | font_set_underline_position(font_rid:RID, size:int, underline_position:float) |
| void | font_set_underline_thickness(font_rid:RID, size:int, underline_thickness:float) |
| void | font_set_variation_coordinates(font_rid:RID, variation_coordinates:Dictionary) |
| void | font_set_weight(font_rid:RID, weight:int) |
| Dictionary | font_supported_feature_list(font_rid:RID)const |
| Dictionary | font_supported_variation_list(font_rid:RID)const |
| String | format_number(number:String, language:String= "")const |
| void | free_rid(rid:RID) |
| int | get_features()const |
| Vector2 | get_hex_code_box_size(size:int, index:int)const |
| String | get_name()const |
| PackedByteArray | get_support_data()const |
| String | get_support_data_filename()const |
| String | get_support_data_info()const |
| bool | has(rid:RID) |
| bool | has_feature(feature:Feature)const |
| int | is_confusable(string:String, dict:PackedStringArray)const |
| bool | is_locale_right_to_left(locale:String)const |
| bool | is_locale_using_support_data(locale:String)const |
| bool | is_valid_identifier(string:String)const |
| bool | is_valid_letter(unicode:int)const |
| bool | load_support_data(filename:String) |
| int | name_to_tag(name:String)const |
| String | parse_number(number:String, language:String= "")const |
| Array[Vector3i] | parse_structured_text(parser_type:StructuredTextParser, args:Array, text:String)const |
| String | percent_sign(language:String= "")const |
| bool | save_support_data(filename:String)const |
| int | shaped_get_run_count(shaped:RID)const |
| Direction | shaped_get_run_direction(shaped:RID, index:int)const |
| RID | shaped_get_run_font_rid(shaped:RID, index:int)const |
| int | shaped_get_run_font_size(shaped:RID, index:int)const |
| String | shaped_get_run_language(shaped:RID, index:int)const |
| Variant | shaped_get_run_object(shaped:RID, index:int)const |
| Vector2i | shaped_get_run_range(shaped:RID, index:int)const |
| String | shaped_get_run_text(shaped:RID, index:int)const |
| int | shaped_get_span_count(shaped:RID)const |
| Variant | shaped_get_span_embedded_object(shaped:RID, index:int)const |
| Variant | shaped_get_span_meta(shaped:RID, index:int)const |
| Variant | shaped_get_span_object(shaped:RID, index:int)const |
| String | shaped_get_span_text(shaped:RID, index:int)const |
| String | shaped_get_text(shaped:RID)const |
| void | shaped_set_span_update_font(shaped:RID, index:int, fonts:Array[RID], size:int, opentype_features:Dictionary= {}) |
| bool | shaped_text_add_object(shaped:RID, key:Variant, size:Vector2, inline_align:InlineAlignment= 5, length:int= 1, baseline:float= 0.0) |
| bool | shaped_text_add_string(shaped:RID, text:String, fonts:Array[RID], size:int, opentype_features:Dictionary= {}, language:String= "", meta:Variant= null) |
| void | shaped_text_clear(rid:RID) |
| int | shaped_text_closest_character_pos(shaped:RID, pos:int)const |
| void | shaped_text_draw(shaped:RID, canvas:RID, pos:Vector2, clip_l:float= -1, clip_r:float= -1, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const |
| void | shaped_text_draw_outline(shaped:RID, canvas:RID, pos:Vector2, clip_l:float= -1, clip_r:float= -1, outline_size:int= 1, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const |
| RID | shaped_text_duplicate(rid:RID) |
| float | shaped_text_fit_to_width(shaped:RID, width:float, justification_flags:BitField[JustificationFlag] = 3) |
| float | shaped_text_get_ascent(shaped:RID)const |
| Dictionary | shaped_text_get_carets(shaped:RID, position:int)const |
| PackedInt32Array | shaped_text_get_character_breaks(shaped:RID)const |
| int | shaped_text_get_custom_ellipsis(shaped:RID)const |
| String | shaped_text_get_custom_punctuation(shaped:RID)const |
| float | shaped_text_get_descent(shaped:RID)const |
| Direction | shaped_text_get_direction(shaped:RID)const |
| Direction | shaped_text_get_dominant_direction_in_range(shaped:RID, start:int, end:int)const |
| int | shaped_text_get_ellipsis_glyph_count(shaped:RID)const |
| Array[Dictionary] | shaped_text_get_ellipsis_glyphs(shaped:RID)const |
| int | shaped_text_get_ellipsis_pos(shaped:RID)const |
| int | shaped_text_get_glyph_count(shaped:RID)const |
| Array[Dictionary] | shaped_text_get_glyphs(shaped:RID)const |
| Vector2 | shaped_text_get_grapheme_bounds(shaped:RID, pos:int)const |
| Direction | shaped_text_get_inferred_direction(shaped:RID)const |
| PackedInt32Array | shaped_text_get_line_breaks(shaped:RID, width:float, start:int= 0, break_flags:BitField[LineBreakFlag] = 3)const |
| PackedInt32Array | shaped_text_get_line_breaks_adv(shaped:RID, width:PackedFloat32Array, start:int= 0, once:bool= true, break_flags:BitField[LineBreakFlag] = 3)const |
| int | shaped_text_get_object_glyph(shaped:RID, key:Variant)const |
| Vector2i | shaped_text_get_object_range(shaped:RID, key:Variant)const |
| Rect2 | shaped_text_get_object_rect(shaped:RID, key:Variant)const |
| Array | shaped_text_get_objects(shaped:RID)const |
| Orientation | shaped_text_get_orientation(shaped:RID)const |
| RID | shaped_text_get_parent(shaped:RID)const |
| bool | shaped_text_get_preserve_control(shaped:RID)const |
| bool | shaped_text_get_preserve_invalid(shaped:RID)const |
| Vector2i | shaped_text_get_range(shaped:RID)const |
| PackedVector2Array | shaped_text_get_selection(shaped:RID, start:int, end:int)const |
| Vector2 | shaped_text_get_size(shaped:RID)const |
| int | shaped_text_get_spacing(shaped:RID, spacing:SpacingType)const |
| int | shaped_text_get_trim_pos(shaped:RID)const |
| float | shaped_text_get_underline_position(shaped:RID)const |
| float | shaped_text_get_underline_thickness(shaped:RID)const |
| float | shaped_text_get_width(shaped:RID)const |
| PackedInt32Array | shaped_text_get_word_breaks(shaped:RID, grapheme_flags:BitField[GraphemeFlag] = 264, skip_grapheme_flags:BitField[GraphemeFlag] = 4)const |
| bool | shaped_text_has_object(shaped:RID, key:Variant)const |
| bool | shaped_text_has_visible_chars(shaped:RID)const |
| int | shaped_text_hit_test_grapheme(shaped:RID, coords:float)const |
| int | shaped_text_hit_test_position(shaped:RID, coords:float)const |
| bool | shaped_text_is_ready(shaped:RID)const |
| int | shaped_text_next_character_pos(shaped:RID, pos:int)const |
| int | shaped_text_next_grapheme_pos(shaped:RID, pos:int)const |
| void | shaped_text_overrun_trim_to_width(shaped:RID, width:float= 0, overrun_trim_flags:BitField[TextOverrunFlag] = 0) |
| int | shaped_text_prev_character_pos(shaped:RID, pos:int)const |
| int | shaped_text_prev_grapheme_pos(shaped:RID, pos:int)const |
| bool | shaped_text_resize_object(shaped:RID, key:Variant, size:Vector2, inline_align:InlineAlignment= 5, baseline:float= 0.0) |
| void | shaped_text_set_bidi_override(shaped:RID, override:Array) |
| void | shaped_text_set_custom_ellipsis(shaped:RID, char:int) |
| void | shaped_text_set_custom_punctuation(shaped:RID, punct:String) |
| void | shaped_text_set_direction(shaped:RID, direction:Direction= 0) |
| void | shaped_text_set_orientation(shaped:RID, orientation:Orientation= 0) |
| void | shaped_text_set_preserve_control(shaped:RID, enabled:bool) |
| void | shaped_text_set_preserve_invalid(shaped:RID, enabled:bool) |
| void | shaped_text_set_spacing(shaped:RID, spacing:SpacingType, value:int) |
| bool | shaped_text_shape(shaped:RID) |
| Array[Dictionary] | shaped_text_sort_logical(shaped:RID) |
| RID | shaped_text_substr(shaped:RID, start:int, length:int)const |
| float | shaped_text_tab_align(shaped:RID, tab_stops:PackedFloat32Array) |
| bool | spoof_check(string:String)const |
| PackedInt32Array | string_get_character_breaks(string:String, language:String= "")const |
| PackedInt32Array | string_get_word_breaks(string:String, language:String= "", chars_per_line:int= 0)const |
| String | string_to_lower(string:String, language:String= "")const |
| String | string_to_title(string:String, language:String= "")const |
| String | string_to_upper(string:String, language:String= "")const |
| String | strip_diacritics(string:String)const |
| String | tag_to_name(tag:int)const |

create_font()
create_font_linked_variation(font_rid:RID)
create_shaped_text(direction:Direction= 0, orientation:Orientation= 0)
void
draw_hex_code_box(canvas:RID, size:int, pos:Vector2, index:int, color:Color)const
void
font_clear_glyphs(font_rid:RID, size:Vector2i)
void
font_clear_kerning_map(font_rid:RID, size:int)
void
font_clear_size_cache(font_rid:RID)
void
font_clear_system_fallback_cache()
void
font_clear_textures(font_rid:RID, size:Vector2i)
void
font_draw_glyph(font_rid:RID, canvas:RID, size:int, pos:Vector2, index:int, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const
void
font_draw_glyph_outline(font_rid:RID, canvas:RID, size:int, outline_size:int, pos:Vector2, index:int, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const
FontAntialiasing
font_get_antialiasing(font_rid:RID)const
float
font_get_ascent(font_rid:RID, size:int)const
float
font_get_baseline_offset(font_rid:RID)const
font_get_char_from_glyph_index(font_rid:RID, size:int, glyph_index:int)const
float
font_get_descent(font_rid:RID, size:int)const
bool
font_get_disable_embedded_bitmaps(font_rid:RID)const
float
font_get_embolden(font_rid:RID)const
font_get_face_count(font_rid:RID)const
font_get_face_index(font_rid:RID)const
font_get_fixed_size(font_rid:RID)const
FixedSizeScaleMode
font_get_fixed_size_scale_mode(font_rid:RID)const
bool
font_get_generate_mipmaps(font_rid:RID)const
float
font_get_global_oversampling()const
Vector2
font_get_glyph_advance(font_rid:RID, size:int, glyph:int)const
Dictionary
font_get_glyph_contours(font:RID, size:int, index:int)const
font_get_glyph_index(font_rid:RID, size:int, char:int, variation_selector:int)const
PackedInt32Array
font_get_glyph_list(font_rid:RID, size:Vector2i)const
Vector2
font_get_glyph_offset(font_rid:RID, size:Vector2i, glyph:int)const
Vector2
font_get_glyph_size(font_rid:RID, size:Vector2i, glyph:int)const
font_get_glyph_texture_idx(font_rid:RID, size:Vector2i, glyph:int)const
font_get_glyph_texture_rid(font_rid:RID, size:Vector2i, glyph:int)const
Vector2
font_get_glyph_texture_size(font_rid:RID, size:Vector2i, glyph:int)const
Rect2
font_get_glyph_uv_rect(font_rid:RID, size:Vector2i, glyph:int)const
Hinting
font_get_hinting(font_rid:RID)const
bool
font_get_keep_rounding_remainders(font_rid:RID)const
Vector2
font_get_kerning(font_rid:RID, size:int, glyph_pair:Vector2i)const
Array[Vector2i]
font_get_kerning_list(font_rid:RID, size:int)const
bool
font_get_language_support_override(font_rid:RID, language:String)
PackedStringArray
font_get_language_support_overrides(font_rid:RID)
font_get_msdf_pixel_range(font_rid:RID)const
font_get_msdf_size(font_rid:RID)const
String
font_get_name(font_rid:RID)const
Dictionary
font_get_opentype_feature_overrides(font_rid:RID)const
Dictionary
font_get_ot_name_strings(font_rid:RID)const
float
font_get_oversampling(font_rid:RID)const
float
font_get_scale(font_rid:RID, size:int)const
bool
font_get_script_support_override(font_rid:RID, script:String)
PackedStringArray
font_get_script_support_overrides(font_rid:RID)
Array[Dictionary]
font_get_size_cache_info(font_rid:RID)const
Array[Vector2i]
font_get_size_cache_list(font_rid:RID)const
font_get_spacing(font_rid:RID, spacing:SpacingType)const
font_get_stretch(font_rid:RID)const
BitField[FontStyle]
font_get_style(font_rid:RID)const
String
font_get_style_name(font_rid:RID)const
SubpixelPositioning
font_get_subpixel_positioning(font_rid:RID)const
String
font_get_supported_chars(font_rid:RID)const
PackedInt32Array
font_get_supported_glyphs(font_rid:RID)const
font_get_texture_count(font_rid:RID, size:Vector2i)const
Image
font_get_texture_image(font_rid:RID, size:Vector2i, texture_index:int)const
PackedInt32Array
font_get_texture_offsets(font_rid:RID, size:Vector2i, texture_index:int)const
Transform2D
font_get_transform(font_rid:RID)const
float
font_get_underline_position(font_rid:RID, size:int)const
float
font_get_underline_thickness(font_rid:RID, size:int)const
Dictionary
font_get_variation_coordinates(font_rid:RID)const
font_get_weight(font_rid:RID)const
bool
font_has_char(font_rid:RID, char:int)const
bool
font_is_allow_system_fallback(font_rid:RID)const
bool
font_is_force_autohinter(font_rid:RID)const
bool
font_is_language_supported(font_rid:RID, language:String)const
bool
font_is_modulate_color_glyphs(font_rid:RID)const
bool
font_is_multichannel_signed_distance_field(font_rid:RID)const
bool
font_is_script_supported(font_rid:RID, script:String)const
void
font_remove_glyph(font_rid:RID, size:Vector2i, glyph:int)
void
font_remove_kerning(font_rid:RID, size:int, glyph_pair:Vector2i)
void
font_remove_language_support_override(font_rid:RID, language:String)
void
font_remove_script_support_override(font_rid:RID, script:String)
void
font_remove_size_cache(font_rid:RID, size:Vector2i)
void
font_remove_texture(font_rid:RID, size:Vector2i, texture_index:int)
void
font_render_glyph(font_rid:RID, size:Vector2i, index:int)
void
font_render_range(font_rid:RID, size:Vector2i, start:int, end:int)
void
font_set_allow_system_fallback(font_rid:RID, allow_system_fallback:bool)
void
font_set_antialiasing(font_rid:RID, antialiasing:FontAntialiasing)
void
font_set_ascent(font_rid:RID, size:int, ascent:float)
void
font_set_baseline_offset(font_rid:RID, baseline_offset:float)
void
font_set_data(font_rid:RID, data:PackedByteArray)
void
font_set_descent(font_rid:RID, size:int, descent:float)
void
font_set_disable_embedded_bitmaps(font_rid:RID, disable_embedded_bitmaps:bool)
void
font_set_embolden(font_rid:RID, strength:float)
void
font_set_face_index(font_rid:RID, face_index:int)
void
font_set_fixed_size(font_rid:RID, fixed_size:int)
void
font_set_fixed_size_scale_mode(font_rid:RID, fixed_size_scale_mode:FixedSizeScaleMode)
void
font_set_force_autohinter(font_rid:RID, force_autohinter:bool)
void
font_set_generate_mipmaps(font_rid:RID, generate_mipmaps:bool)
void
font_set_global_oversampling(oversampling:float)
void
font_set_glyph_advance(font_rid:RID, size:int, glyph:int, advance:Vector2)
void
font_set_glyph_offset(font_rid:RID, size:Vector2i, glyph:int, offset:Vector2)
void
font_set_glyph_size(font_rid:RID, size:Vector2i, glyph:int, gl_size:Vector2)
void
font_set_glyph_texture_idx(font_rid:RID, size:Vector2i, glyph:int, texture_idx:int)
void
font_set_glyph_uv_rect(font_rid:RID, size:Vector2i, glyph:int, uv_rect:Rect2)
void
font_set_hinting(font_rid:RID, hinting:Hinting)
void
font_set_keep_rounding_remainders(font_rid:RID, keep_rounding_remainders:bool)
void
font_set_kerning(font_rid:RID, size:int, glyph_pair:Vector2i, kerning:Vector2)
void
font_set_language_support_override(font_rid:RID, language:String, supported:bool)
void
font_set_modulate_color_glyphs(font_rid:RID, force_autohinter:bool)
void
font_set_msdf_pixel_range(font_rid:RID, msdf_pixel_range:int)
void
font_set_msdf_size(font_rid:RID, msdf_size:int)
void
font_set_multichannel_signed_distance_field(font_rid:RID, msdf:bool)
void
font_set_name(font_rid:RID, name:String)
void
font_set_opentype_feature_overrides(font_rid:RID, overrides:Dictionary)
void
font_set_oversampling(font_rid:RID, oversampling:float)
void
font_set_scale(font_rid:RID, size:int, scale:float)
void
font_set_script_support_override(font_rid:RID, script:String, supported:bool)
void
font_set_spacing(font_rid:RID, spacing:SpacingType, value:int)
void
font_set_stretch(font_rid:RID, weight:int)
void
font_set_style(font_rid:RID, style:BitField[FontStyle])
void
font_set_style_name(font_rid:RID, name:String)
void
font_set_subpixel_positioning(font_rid:RID, subpixel_positioning:SubpixelPositioning)
void
font_set_texture_image(font_rid:RID, size:Vector2i, texture_index:int, image:Image)
void
font_set_texture_offsets(font_rid:RID, size:Vector2i, texture_index:int, offset:PackedInt32Array)
void
font_set_transform(font_rid:RID, transform:Transform2D)
void
font_set_underline_position(font_rid:RID, size:int, underline_position:float)
void
font_set_underline_thickness(font_rid:RID, size:int, underline_thickness:float)
void
font_set_variation_coordinates(font_rid:RID, variation_coordinates:Dictionary)
void
font_set_weight(font_rid:RID, weight:int)
Dictionary
font_supported_feature_list(font_rid:RID)const
Dictionary
font_supported_variation_list(font_rid:RID)const
String
format_number(number:String, language:String= "")const
void
free_rid(rid:RID)
get_features()const
Vector2
get_hex_code_box_size(size:int, index:int)const
String
get_name()const
PackedByteArray
get_support_data()const
String
get_support_data_filename()const
String
get_support_data_info()const
bool
has(rid:RID)
bool
has_feature(feature:Feature)const
is_confusable(string:String, dict:PackedStringArray)const
bool
is_locale_right_to_left(locale:String)const
bool
is_locale_using_support_data(locale:String)const
bool
is_valid_identifier(string:String)const
bool
is_valid_letter(unicode:int)const
bool
load_support_data(filename:String)
name_to_tag(name:String)const
String
parse_number(number:String, language:String= "")const
Array[Vector3i]
parse_structured_text(parser_type:StructuredTextParser, args:Array, text:String)const
String
percent_sign(language:String= "")const
bool
save_support_data(filename:String)const
shaped_get_run_count(shaped:RID)const
Direction
shaped_get_run_direction(shaped:RID, index:int)const
shaped_get_run_font_rid(shaped:RID, index:int)const
shaped_get_run_font_size(shaped:RID, index:int)const
String
shaped_get_run_language(shaped:RID, index:int)const
Variant
shaped_get_run_object(shaped:RID, index:int)const
Vector2i
shaped_get_run_range(shaped:RID, index:int)const
String
shaped_get_run_text(shaped:RID, index:int)const
shaped_get_span_count(shaped:RID)const
Variant
shaped_get_span_embedded_object(shaped:RID, index:int)const
Variant
shaped_get_span_meta(shaped:RID, index:int)const
Variant
shaped_get_span_object(shaped:RID, index:int)const
String
shaped_get_span_text(shaped:RID, index:int)const
String
shaped_get_text(shaped:RID)const
void
shaped_set_span_update_font(shaped:RID, index:int, fonts:Array[RID], size:int, opentype_features:Dictionary= {})
bool
shaped_text_add_object(shaped:RID, key:Variant, size:Vector2, inline_align:InlineAlignment= 5, length:int= 1, baseline:float= 0.0)
bool
shaped_text_add_string(shaped:RID, text:String, fonts:Array[RID], size:int, opentype_features:Dictionary= {}, language:String= "", meta:Variant= null)
void
shaped_text_clear(rid:RID)
shaped_text_closest_character_pos(shaped:RID, pos:int)const
void
shaped_text_draw(shaped:RID, canvas:RID, pos:Vector2, clip_l:float= -1, clip_r:float= -1, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const
void
shaped_text_draw_outline(shaped:RID, canvas:RID, pos:Vector2, clip_l:float= -1, clip_r:float= -1, outline_size:int= 1, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const
shaped_text_duplicate(rid:RID)
float
shaped_text_fit_to_width(shaped:RID, width:float, justification_flags:BitField[JustificationFlag] = 3)
float
shaped_text_get_ascent(shaped:RID)const
Dictionary
shaped_text_get_carets(shaped:RID, position:int)const
PackedInt32Array
shaped_text_get_character_breaks(shaped:RID)const
shaped_text_get_custom_ellipsis(shaped:RID)const
String
shaped_text_get_custom_punctuation(shaped:RID)const
float
shaped_text_get_descent(shaped:RID)const
Direction
shaped_text_get_direction(shaped:RID)const
Direction
shaped_text_get_dominant_direction_in_range(shaped:RID, start:int, end:int)const
shaped_text_get_ellipsis_glyph_count(shaped:RID)const
Array[Dictionary]
shaped_text_get_ellipsis_glyphs(shaped:RID)const
shaped_text_get_ellipsis_pos(shaped:RID)const
shaped_text_get_glyph_count(shaped:RID)const
Array[Dictionary]
shaped_text_get_glyphs(shaped:RID)const
Vector2
shaped_text_get_grapheme_bounds(shaped:RID, pos:int)const
Direction
shaped_text_get_inferred_direction(shaped:RID)const
PackedInt32Array
shaped_text_get_line_breaks(shaped:RID, width:float, start:int= 0, break_flags:BitField[LineBreakFlag] = 3)const
PackedInt32Array
shaped_text_get_line_breaks_adv(shaped:RID, width:PackedFloat32Array, start:int= 0, once:bool= true, break_flags:BitField[LineBreakFlag] = 3)const
shaped_text_get_object_glyph(shaped:RID, key:Variant)const
Vector2i
shaped_text_get_object_range(shaped:RID, key:Variant)const
Rect2
shaped_text_get_object_rect(shaped:RID, key:Variant)const
Array
shaped_text_get_objects(shaped:RID)const
Orientation
shaped_text_get_orientation(shaped:RID)const
shaped_text_get_parent(shaped:RID)const
bool
shaped_text_get_preserve_control(shaped:RID)const
bool
shaped_text_get_preserve_invalid(shaped:RID)const
Vector2i
shaped_text_get_range(shaped:RID)const
PackedVector2Array
shaped_text_get_selection(shaped:RID, start:int, end:int)const
Vector2
shaped_text_get_size(shaped:RID)const
shaped_text_get_spacing(shaped:RID, spacing:SpacingType)const
shaped_text_get_trim_pos(shaped:RID)const
float
shaped_text_get_underline_position(shaped:RID)const
float
shaped_text_get_underline_thickness(shaped:RID)const
float
shaped_text_get_width(shaped:RID)const
PackedInt32Array
shaped_text_get_word_breaks(shaped:RID, grapheme_flags:BitField[GraphemeFlag] = 264, skip_grapheme_flags:BitField[GraphemeFlag] = 4)const
bool
shaped_text_has_object(shaped:RID, key:Variant)const
bool
shaped_text_has_visible_chars(shaped:RID)const
shaped_text_hit_test_grapheme(shaped:RID, coords:float)const
shaped_text_hit_test_position(shaped:RID, coords:float)const
bool
shaped_text_is_ready(shaped:RID)const
shaped_text_next_character_pos(shaped:RID, pos:int)const
shaped_text_next_grapheme_pos(shaped:RID, pos:int)const
void
shaped_text_overrun_trim_to_width(shaped:RID, width:float= 0, overrun_trim_flags:BitField[TextOverrunFlag] = 0)
shaped_text_prev_character_pos(shaped:RID, pos:int)const
shaped_text_prev_grapheme_pos(shaped:RID, pos:int)const
bool
shaped_text_resize_object(shaped:RID, key:Variant, size:Vector2, inline_align:InlineAlignment= 5, baseline:float= 0.0)
void
shaped_text_set_bidi_override(shaped:RID, override:Array)
void
shaped_text_set_custom_ellipsis(shaped:RID, char:int)
void
shaped_text_set_custom_punctuation(shaped:RID, punct:String)
void
shaped_text_set_direction(shaped:RID, direction:Direction= 0)
void
shaped_text_set_orientation(shaped:RID, orientation:Orientation= 0)
void
shaped_text_set_preserve_control(shaped:RID, enabled:bool)
void
shaped_text_set_preserve_invalid(shaped:RID, enabled:bool)
void
shaped_text_set_spacing(shaped:RID, spacing:SpacingType, value:int)
bool
shaped_text_shape(shaped:RID)
Array[Dictionary]
shaped_text_sort_logical(shaped:RID)
shaped_text_substr(shaped:RID, start:int, length:int)const
float
shaped_text_tab_align(shaped:RID, tab_stops:PackedFloat32Array)
bool
spoof_check(string:String)const
PackedInt32Array
string_get_character_breaks(string:String, language:String= "")const
PackedInt32Array
string_get_word_breaks(string:String, language:String= "", chars_per_line:int= 0)const
String
string_to_lower(string:String, language:String= "")const
String
string_to_title(string:String, language:String= "")const
String
string_to_upper(string:String, language:String= "")const
String
strip_diacritics(string:String)const
String
tag_to_name(tag:int)const

## Enumerations

enumFontAntialiasing:🔗
FontAntialiasingFONT_ANTIALIASING_NONE=0
Font glyphs are rasterized as 1-bit bitmaps.
FontAntialiasingFONT_ANTIALIASING_GRAY=1
Font glyphs are rasterized as 8-bit grayscale anti-aliased bitmaps.
FontAntialiasingFONT_ANTIALIASING_LCD=2
Font glyphs are rasterized for LCD screens.
LCD subpixel layout is determined by the value of theProjectSettings.gui/theme/lcd_subpixel_layoutsetting.
LCD subpixel anti-aliasing mode is suitable only for rendering horizontal, unscaled text in 2D.
enumFontLCDSubpixelLayout:🔗
FontLCDSubpixelLayoutFONT_LCD_SUBPIXEL_LAYOUT_NONE=0
Unknown or unsupported subpixel layout, LCD subpixel antialiasing is disabled.
FontLCDSubpixelLayoutFONT_LCD_SUBPIXEL_LAYOUT_HRGB=1
Horizontal RGB subpixel layout.
FontLCDSubpixelLayoutFONT_LCD_SUBPIXEL_LAYOUT_HBGR=2
Horizontal BGR subpixel layout.
FontLCDSubpixelLayoutFONT_LCD_SUBPIXEL_LAYOUT_VRGB=3
Vertical RGB subpixel layout.
FontLCDSubpixelLayoutFONT_LCD_SUBPIXEL_LAYOUT_VBGR=4
Vertical BGR subpixel layout.
FontLCDSubpixelLayoutFONT_LCD_SUBPIXEL_LAYOUT_MAX=5
Represents the size of theFontLCDSubpixelLayoutenum.
enumDirection:🔗
DirectionDIRECTION_AUTO=0
Text direction is determined based on contents and current locale.
DirectionDIRECTION_LTR=1
Text is written from left to right.
DirectionDIRECTION_RTL=2
Text is written from right to left.
DirectionDIRECTION_INHERITED=3
Text writing direction is the same as base string writing direction. Used for BiDi override only.
enumOrientation:🔗
OrientationORIENTATION_HORIZONTAL=0
Text is written horizontally.
OrientationORIENTATION_VERTICAL=1
Left to right text is written vertically from top to bottom.
Right to left text is written vertically from bottom to top.
flagsJustificationFlag:🔗
JustificationFlagJUSTIFICATION_NONE=0
Do not justify text.
JustificationFlagJUSTIFICATION_KASHIDA=1
Justify text by adding and removing kashidas.
JustificationFlagJUSTIFICATION_WORD_BOUND=2
Justify text by changing width of the spaces between the words.
JustificationFlagJUSTIFICATION_TRIM_EDGE_SPACES=4
Remove trailing and leading spaces from the justified text.
JustificationFlagJUSTIFICATION_AFTER_LAST_TAB=8
Only apply justification to the part of the text after the last tab.
JustificationFlagJUSTIFICATION_CONSTRAIN_ELLIPSIS=16
Apply justification to the trimmed line with ellipsis.
JustificationFlagJUSTIFICATION_SKIP_LAST_LINE=32
Do not apply justification to the last line of the paragraph.
JustificationFlagJUSTIFICATION_SKIP_LAST_LINE_WITH_VISIBLE_CHARS=64
Do not apply justification to the last line of the paragraph with visible characters (takes precedence overJUSTIFICATION_SKIP_LAST_LINE).
JustificationFlagJUSTIFICATION_DO_NOT_SKIP_SINGLE_LINE=128
Always apply justification to the paragraphs with a single line (JUSTIFICATION_SKIP_LAST_LINEandJUSTIFICATION_SKIP_LAST_LINE_WITH_VISIBLE_CHARSare ignored).
enumAutowrapMode:🔗
AutowrapModeAUTOWRAP_OFF=0
Autowrap is disabled.
AutowrapModeAUTOWRAP_ARBITRARY=1
Wraps the text inside the node's bounding rectangle by allowing to break lines at arbitrary positions, which is useful when very limited space is available.
AutowrapModeAUTOWRAP_WORD=2
Wraps the text inside the node's bounding rectangle by soft-breaking between words.
AutowrapModeAUTOWRAP_WORD_SMART=3
Behaves similarly toAUTOWRAP_WORD, but force-breaks a word if that single word does not fit in one line.
flagsLineBreakFlag:🔗
LineBreakFlagBREAK_NONE=0
Do not break the line.
LineBreakFlagBREAK_MANDATORY=1
Break the line at the line mandatory break characters (e.g."\n").
LineBreakFlagBREAK_WORD_BOUND=2
Break the line between the words.
LineBreakFlagBREAK_GRAPHEME_BOUND=4
Break the line between any unconnected graphemes.
LineBreakFlagBREAK_ADAPTIVE=8
Should be used only in conjunction withBREAK_WORD_BOUND, break the line between any unconnected graphemes, if it's impossible to break it between the words.
LineBreakFlagBREAK_TRIM_EDGE_SPACES=16
Deprecated:UseBREAK_TRIM_START_EDGE_SPACES|BREAK_TRIM_END_EDGE_SPACESinstead.
Remove edge spaces from the broken line segments.
LineBreakFlagBREAK_TRIM_INDENT=32
Subtract first line indentation width from all lines after the first one.
LineBreakFlagBREAK_TRIM_START_EDGE_SPACES=64
Remove spaces and line break characters from the start of broken line segments.
E.g, after line breaking, the second segment of the following texttest\nnext, isnextif the flag is set, and ``next`` if it is not.
LineBreakFlagBREAK_TRIM_END_EDGE_SPACES=128
Remove spaces and line break characters from the end of broken line segments.
E.g, after line breaking, the first segment of the following texttest\nnext, istestif the flag is set, andtest\nif it is not.
enumVisibleCharactersBehavior:🔗
VisibleCharactersBehaviorVC_CHARS_BEFORE_SHAPING=0
Trims text before the shaping. e.g, increasingLabel.visible_charactersorRichTextLabel.visible_charactersvalue is visually identical to typing the text.
Note:In this mode, trimmed text is not processed at all. It is not accounted for in line breaking and size calculations.
VisibleCharactersBehaviorVC_CHARS_AFTER_SHAPING=1
Displays glyphs that are mapped to the firstLabel.visible_charactersorRichTextLabel.visible_characterscharacters from the beginning of the text.
VisibleCharactersBehaviorVC_GLYPHS_AUTO=2
DisplaysLabel.visible_ratioorRichTextLabel.visible_ratioglyphs, starting from the left or from the right, depending onControl.layout_directionvalue.
VisibleCharactersBehaviorVC_GLYPHS_LTR=3
DisplaysLabel.visible_ratioorRichTextLabel.visible_ratioglyphs, starting from the left.
VisibleCharactersBehaviorVC_GLYPHS_RTL=4
DisplaysLabel.visible_ratioorRichTextLabel.visible_ratioglyphs, starting from the right.
enumOverrunBehavior:🔗
OverrunBehaviorOVERRUN_NO_TRIMMING=0
No text trimming is performed.
OverrunBehaviorOVERRUN_TRIM_CHAR=1
Trims the text per character.
OverrunBehaviorOVERRUN_TRIM_WORD=2
Trims the text per word.
OverrunBehaviorOVERRUN_TRIM_ELLIPSIS=3
Trims the text per character and adds an ellipsis to indicate that parts are hidden if trimmed text is 6 characters or longer.
OverrunBehaviorOVERRUN_TRIM_WORD_ELLIPSIS=4
Trims the text per word and adds an ellipsis to indicate that parts are hidden if trimmed text is 6 characters or longer.
OverrunBehaviorOVERRUN_TRIM_ELLIPSIS_FORCE=5
Trims the text per character and adds an ellipsis to indicate that parts are hidden regardless of trimmed text length.
OverrunBehaviorOVERRUN_TRIM_WORD_ELLIPSIS_FORCE=6
Trims the text per word and adds an ellipsis to indicate that parts are hidden regardless of trimmed text length.
flagsTextOverrunFlag:🔗
TextOverrunFlagOVERRUN_NO_TRIM=0
No trimming is performed.
TextOverrunFlagOVERRUN_TRIM=1
Trims the text when it exceeds the given width.
TextOverrunFlagOVERRUN_TRIM_WORD_ONLY=2
Trims the text per word instead of per grapheme.
TextOverrunFlagOVERRUN_ADD_ELLIPSIS=4
Determines whether an ellipsis should be added at the end of the text.
TextOverrunFlagOVERRUN_ENFORCE_ELLIPSIS=8
Determines whether the ellipsis at the end of the text is enforced and may not be hidden.
TextOverrunFlagOVERRUN_JUSTIFICATION_AWARE=16
Accounts for the text being justified before attempting to trim it (seeJustificationFlag).
TextOverrunFlagOVERRUN_SHORT_STRING_ELLIPSIS=32
Determines whether the ellipsis should be added regardless of the string length, otherwise it is added only if the string is 6 characters or longer.
flagsGraphemeFlag:🔗
GraphemeFlagGRAPHEME_IS_VALID=1
Grapheme is supported by the font, and can be drawn.
GraphemeFlagGRAPHEME_IS_RTL=2
Grapheme is part of right-to-left or bottom-to-top run.
GraphemeFlagGRAPHEME_IS_VIRTUAL=4
Grapheme is not part of source text, it was added by justification process.
GraphemeFlagGRAPHEME_IS_SPACE=8
Grapheme is whitespace.
GraphemeFlagGRAPHEME_IS_BREAK_HARD=16
Grapheme is mandatory break point (e.g."\n").
GraphemeFlagGRAPHEME_IS_BREAK_SOFT=32
Grapheme is optional break point (e.g. space).
GraphemeFlagGRAPHEME_IS_TAB=64
Grapheme is the tabulation character.
GraphemeFlagGRAPHEME_IS_ELONGATION=128
Grapheme is kashida.
GraphemeFlagGRAPHEME_IS_PUNCTUATION=256
Grapheme is punctuation character.
GraphemeFlagGRAPHEME_IS_UNDERSCORE=512
Grapheme is underscore character.
GraphemeFlagGRAPHEME_IS_CONNECTED=1024
Grapheme is connected to the previous grapheme. Breaking line before this grapheme is not safe.
GraphemeFlagGRAPHEME_IS_SAFE_TO_INSERT_TATWEEL=2048
It is safe to insert a U+0640 before this grapheme for elongation.
GraphemeFlagGRAPHEME_IS_EMBEDDED_OBJECT=4096
Grapheme is an object replacement character for the embedded object.
GraphemeFlagGRAPHEME_IS_SOFT_HYPHEN=8192
Grapheme is a soft hyphen.
enumHinting:🔗
HintingHINTING_NONE=0
Disables font hinting (smoother but less crisp).
HintingHINTING_LIGHT=1
Use the light font hinting mode.
HintingHINTING_NORMAL=2
Use the default font hinting mode (crisper but less smooth).
Note:This hinting mode changes both horizontal and vertical glyph metrics. If applied to monospace font, some glyphs might have different width.
enumSubpixelPositioning:🔗
SubpixelPositioningSUBPIXEL_POSITIONING_DISABLED=0
Glyph horizontal position is rounded to the whole pixel size, each glyph is rasterized once.
SubpixelPositioningSUBPIXEL_POSITIONING_AUTO=1
Glyph horizontal position is rounded based on font size.

- To one quarter of the pixel size if font size is smaller or equal toSUBPIXEL_POSITIONING_ONE_QUARTER_MAX_SIZE.
To one quarter of the pixel size if font size is smaller or equal toSUBPIXEL_POSITIONING_ONE_QUARTER_MAX_SIZE.
- To one half of the pixel size if font size is smaller or equal toSUBPIXEL_POSITIONING_ONE_HALF_MAX_SIZE.
To one half of the pixel size if font size is smaller or equal toSUBPIXEL_POSITIONING_ONE_HALF_MAX_SIZE.
- To the whole pixel size for larger fonts.
To the whole pixel size for larger fonts.
SubpixelPositioningSUBPIXEL_POSITIONING_ONE_HALF=2
Glyph horizontal position is rounded to one half of the pixel size, each glyph is rasterized up to two times.
SubpixelPositioningSUBPIXEL_POSITIONING_ONE_QUARTER=3
Glyph horizontal position is rounded to one quarter of the pixel size, each glyph is rasterized up to four times.
SubpixelPositioningSUBPIXEL_POSITIONING_ONE_HALF_MAX_SIZE=20
Maximum font size which will use "one half of the pixel" subpixel positioning inSUBPIXEL_POSITIONING_AUTOmode.
SubpixelPositioningSUBPIXEL_POSITIONING_ONE_QUARTER_MAX_SIZE=16
Maximum font size which will use "one quarter of the pixel" subpixel positioning inSUBPIXEL_POSITIONING_AUTOmode.
enumFeature:🔗
FeatureFEATURE_SIMPLE_LAYOUT=1
TextServer supports simple text layouts.
FeatureFEATURE_BIDI_LAYOUT=2
TextServer supports bidirectional text layouts.
FeatureFEATURE_VERTICAL_LAYOUT=4
TextServer supports vertical layouts.
FeatureFEATURE_SHAPING=8
TextServer supports complex text shaping.
FeatureFEATURE_KASHIDA_JUSTIFICATION=16
TextServer supports justification using kashidas.
FeatureFEATURE_BREAK_ITERATORS=32
TextServer supports complex line/word breaking rules (e.g. dictionary based).
FeatureFEATURE_FONT_BITMAP=64
TextServer supports loading bitmap fonts.
FeatureFEATURE_FONT_DYNAMIC=128
TextServer supports loading dynamic (TrueType, OpeType, etc.) fonts.
FeatureFEATURE_FONT_MSDF=256
TextServer supports multichannel signed distance field dynamic font rendering.
FeatureFEATURE_FONT_SYSTEM=512
TextServer supports loading system fonts.
FeatureFEATURE_FONT_VARIABLE=1024
TextServer supports variable fonts.
FeatureFEATURE_CONTEXT_SENSITIVE_CASE_CONVERSION=2048
TextServer supports locale dependent and context sensitive case conversion.
FeatureFEATURE_USE_SUPPORT_DATA=4096
TextServer require external data file for some features, seeload_support_data().
FeatureFEATURE_UNICODE_IDENTIFIERS=8192
TextServer supports UAX #31 identifier validation, seeis_valid_identifier().
FeatureFEATURE_UNICODE_SECURITY=16384
TextServer supportsUnicode Technical Report #36andUnicode Technical Standard #39based spoof detection features.
enumContourPointTag:🔗
ContourPointTagCONTOUR_CURVE_TAG_ON=1
Contour point is on the curve.
ContourPointTagCONTOUR_CURVE_TAG_OFF_CONIC=0
Contour point isn't on the curve, but serves as a control point for a conic (quadratic) Bézier arc.
ContourPointTagCONTOUR_CURVE_TAG_OFF_CUBIC=2
Contour point isn't on the curve, but serves as a control point for a cubic Bézier arc.
enumSpacingType:🔗
SpacingTypeSPACING_GLYPH=0
Spacing for each glyph.
SpacingTypeSPACING_SPACE=1
Spacing for the space character.
SpacingTypeSPACING_TOP=2
Spacing at the top of the line.
SpacingTypeSPACING_BOTTOM=3
Spacing at the bottom of the line.
SpacingTypeSPACING_MAX=4
Represents the size of theSpacingTypeenum.
flagsFontStyle:🔗
FontStyleFONT_BOLD=1
Font is bold.
FontStyleFONT_ITALIC=2
Font is italic or oblique.
FontStyleFONT_FIXED_WIDTH=4
Font has fixed-width characters (also known as monospace).
enumStructuredTextParser:🔗
StructuredTextParserSTRUCTURED_TEXT_DEFAULT=0
Use default Unicode BiDi algorithm.
StructuredTextParserSTRUCTURED_TEXT_URI=1
BiDi override for URI.
StructuredTextParserSTRUCTURED_TEXT_FILE=2
BiDi override for file path.
StructuredTextParserSTRUCTURED_TEXT_EMAIL=3
BiDi override for email.
StructuredTextParserSTRUCTURED_TEXT_LIST=4
BiDi override for lists. Structured text options: list separatorString.
StructuredTextParserSTRUCTURED_TEXT_GDSCRIPT=5
BiDi override for GDScript.
StructuredTextParserSTRUCTURED_TEXT_CUSTOM=6
User defined structured text BiDi override function.
enumFixedSizeScaleMode:🔗
FixedSizeScaleModeFIXED_SIZE_SCALE_DISABLE=0
Bitmap font is not scaled.
FixedSizeScaleModeFIXED_SIZE_SCALE_INTEGER_ONLY=1
Bitmap font is scaled to the closest integer multiple of the font's fixed size. This is the recommended option for pixel art fonts.
FixedSizeScaleModeFIXED_SIZE_SCALE_ENABLED=2
Bitmap font is scaled to an arbitrary (fractional) size. This is the recommended option for non-pixel art fonts.

## Method Descriptions

RIDcreate_font()🔗
Creates a new, empty font cache entry resource. To free the resulting resource, use thefree_rid()method.
RIDcreate_font_linked_variation(font_rid:RID)🔗
Creates a new variation existing font which is reusing the same glyph cache and font data. To free the resulting resource, use thefree_rid()method.
RIDcreate_shaped_text(direction:Direction= 0, orientation:Orientation= 0)🔗
Creates a new buffer for complex text layout, with the givendirectionandorientation. To free the resulting buffer, usefree_rid()method.
Note:Direction is ignored if server does not supportFEATURE_BIDI_LAYOUTfeature (supported byTextServerAdvanced).
Note:Orientation is ignored if server does not supportFEATURE_VERTICAL_LAYOUTfeature (supported byTextServerAdvanced).
voiddraw_hex_code_box(canvas:RID, size:int, pos:Vector2, index:int, color:Color)const🔗
Draws box displaying character hexadecimal code. Used for replacing missing characters.
voidfont_clear_glyphs(font_rid:RID, size:Vector2i)🔗
Removes all rendered glyph information from the cache entry.
Note:This function will not remove textures associated with the glyphs, usefont_remove_texture()to remove them manually.
voidfont_clear_kerning_map(font_rid:RID, size:int)🔗
Removes all kerning overrides.
voidfont_clear_size_cache(font_rid:RID)🔗
Removes all font sizes from the cache entry.
voidfont_clear_system_fallback_cache()🔗
Frees all automatically loaded system fonts.
voidfont_clear_textures(font_rid:RID, size:Vector2i)🔗
Removes all textures from font cache entry.
Note:This function will not remove glyphs associated with the texture, usefont_remove_glyph()to remove them manually.
voidfont_draw_glyph(font_rid:RID, canvas:RID, size:int, pos:Vector2, index:int, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const🔗
Draws single glyph into a canvas item at the position, usingfont_ridat the sizesize. Ifoversamplingis greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.
Note:Glyph index is specific to the font, use glyphs indices returned byshaped_text_get_glyphs()orfont_get_glyph_index().
Note:If there are pending glyphs to render, calling this function might trigger the texture cache update.
voidfont_draw_glyph_outline(font_rid:RID, canvas:RID, size:int, outline_size:int, pos:Vector2, index:int, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const🔗
Draws single glyph outline of sizeoutline_sizeinto a canvas item at the position, usingfont_ridat the sizesize. Ifoversamplingis greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.
Note:Glyph index is specific to the font, use glyphs indices returned byshaped_text_get_glyphs()orfont_get_glyph_index().
Note:If there are pending glyphs to render, calling this function might trigger the texture cache update.
FontAntialiasingfont_get_antialiasing(font_rid:RID)const🔗
Returns font anti-aliasing mode.
floatfont_get_ascent(font_rid:RID, size:int)const🔗
Returns the font ascent (number of pixels above the baseline).
floatfont_get_baseline_offset(font_rid:RID)const🔗
Returns extra baseline offset (as a fraction of font height).
intfont_get_char_from_glyph_index(font_rid:RID, size:int, glyph_index:int)const🔗
Returns character code associated withglyph_index, or0ifglyph_indexis invalid. Seefont_get_glyph_index().
floatfont_get_descent(font_rid:RID, size:int)const🔗
Returns the font descent (number of pixels below the baseline).
boolfont_get_disable_embedded_bitmaps(font_rid:RID)const🔗
Returns whether the font's embedded bitmap loading is disabled.
floatfont_get_embolden(font_rid:RID)const🔗
Returns font embolden strength.
intfont_get_face_count(font_rid:RID)const🔗
Returns number of faces in the TrueType / OpenType collection.
intfont_get_face_index(font_rid:RID)const🔗
Returns an active face index in the TrueType / OpenType collection.
intfont_get_fixed_size(font_rid:RID)const🔗
Returns bitmap font fixed size.
FixedSizeScaleModefont_get_fixed_size_scale_mode(font_rid:RID)const🔗
Returns bitmap font scaling mode.
boolfont_get_generate_mipmaps(font_rid:RID)const🔗
Returnstrueif font texture mipmap generation is enabled.
floatfont_get_global_oversampling()const🔗
Deprecated:UseViewportoversampling, or theoversamplingargument of thedraw_*methods instead.
This method does nothing and always returns1.0.
Vector2font_get_glyph_advance(font_rid:RID, size:int, glyph:int)const🔗
Returns glyph advance (offset of the next glyph).
Note:Advance for glyphs outlines is the same as the base glyph advance and is not saved.
Dictionaryfont_get_glyph_contours(font:RID, size:int, index:int)const🔗
Returns outline contours of the glyph as aDictionarywith the following contents:
points-PackedVector3Array, containing outline points.xandyare point coordinates.zis the type of the point, using theContourPointTagvalues.
contours-PackedInt32Array, containing indices the end points of each contour.
orientation-bool, contour orientation. Iftrue, clockwise contours must be filled.

- Two successiveCONTOUR_CURVE_TAG_ONpoints indicate a line segment.
Two successiveCONTOUR_CURVE_TAG_ONpoints indicate a line segment.
- OneCONTOUR_CURVE_TAG_OFF_CONICpoint between twoCONTOUR_CURVE_TAG_ONpoints indicates a single conic (quadratic) Bézier arc.
OneCONTOUR_CURVE_TAG_OFF_CONICpoint between twoCONTOUR_CURVE_TAG_ONpoints indicates a single conic (quadratic) Bézier arc.
- TwoCONTOUR_CURVE_TAG_OFF_CUBICpoints between twoCONTOUR_CURVE_TAG_ONpoints indicate a single cubic Bézier arc.
TwoCONTOUR_CURVE_TAG_OFF_CUBICpoints between twoCONTOUR_CURVE_TAG_ONpoints indicate a single cubic Bézier arc.
- Two successiveCONTOUR_CURVE_TAG_OFF_CONICpoints indicate two successive conic (quadratic) Bézier arcs with a virtualCONTOUR_CURVE_TAG_ONpoint at their middle.
Two successiveCONTOUR_CURVE_TAG_OFF_CONICpoints indicate two successive conic (quadratic) Bézier arcs with a virtualCONTOUR_CURVE_TAG_ONpoint at their middle.
- Each contour is closed. The last point of a contour uses the first point of a contour as its next point, and vice versa. The first point can beCONTOUR_CURVE_TAG_OFF_CONICpoint.
Each contour is closed. The last point of a contour uses the first point of a contour as its next point, and vice versa. The first point can beCONTOUR_CURVE_TAG_OFF_CONICpoint.
intfont_get_glyph_index(font_rid:RID, size:int, char:int, variation_selector:int)const🔗
Returns the glyph index of achar, optionally modified by thevariation_selector. Seefont_get_char_from_glyph_index().
PackedInt32Arrayfont_get_glyph_list(font_rid:RID, size:Vector2i)const🔗
Returns list of rendered glyphs in the cache entry.
Vector2font_get_glyph_offset(font_rid:RID, size:Vector2i, glyph:int)const🔗
Returns glyph offset from the baseline.
Vector2font_get_glyph_size(font_rid:RID, size:Vector2i, glyph:int)const🔗
Returns size of the glyph.
intfont_get_glyph_texture_idx(font_rid:RID, size:Vector2i, glyph:int)const🔗
Returns index of the cache texture containing the glyph.
RIDfont_get_glyph_texture_rid(font_rid:RID, size:Vector2i, glyph:int)const🔗
Returns resource ID of the cache texture containing the glyph.
Note:If there are pending glyphs to render, calling this function might trigger the texture cache update.
Vector2font_get_glyph_texture_size(font_rid:RID, size:Vector2i, glyph:int)const🔗
Returns size of the cache texture containing the glyph.
Note:If there are pending glyphs to render, calling this function might trigger the texture cache update.
Rect2font_get_glyph_uv_rect(font_rid:RID, size:Vector2i, glyph:int)const🔗
Returns rectangle in the cache texture containing the glyph.
Hintingfont_get_hinting(font_rid:RID)const🔗
Returns the font hinting mode. Used by dynamic fonts only.
boolfont_get_keep_rounding_remainders(font_rid:RID)const🔗
Returns glyph position rounding behavior. If set totrue, when aligning glyphs to the pixel boundaries rounding remainders are accumulated to ensure more uniform glyph distribution. This setting has no effect if subpixel positioning is enabled.
Vector2font_get_kerning(font_rid:RID, size:int, glyph_pair:Vector2i)const🔗
Returns kerning for the pair of glyphs.
Array[Vector2i]font_get_kerning_list(font_rid:RID, size:int)const🔗
Returns list of the kerning overrides.
boolfont_get_language_support_override(font_rid:RID, language:String)🔗
Returnstrueif support override is enabled for thelanguage.
PackedStringArrayfont_get_language_support_overrides(font_rid:RID)🔗
Returns list of language support overrides.
intfont_get_msdf_pixel_range(font_rid:RID)const🔗
Returns the width of the range around the shape between the minimum and maximum representable signed distance.
intfont_get_msdf_size(font_rid:RID)const🔗
Returns source font size used to generate MSDF textures.
Stringfont_get_name(font_rid:RID)const🔗
Returns font family name.
Dictionaryfont_get_opentype_feature_overrides(font_rid:RID)const🔗
Returns font OpenType feature set override.
Dictionaryfont_get_ot_name_strings(font_rid:RID)const🔗
ReturnsDictionarywith OpenType font name strings (localized font names, version, description, license information, sample text, etc.).
floatfont_get_oversampling(font_rid:RID)const🔗
Returns oversampling factor override. If set to a positive value, overrides the oversampling factor of the viewport this font is used in. SeeViewport.oversampling. This value doesn't override theoversamplingparameter ofdraw_*methods. Used by dynamic fonts only.
floatfont_get_scale(font_rid:RID, size:int)const🔗
Returns scaling factor of the color bitmap font.
boolfont_get_script_support_override(font_rid:RID, script:String)🔗
Returnstrueif support override is enabled for thescript.
PackedStringArrayfont_get_script_support_overrides(font_rid:RID)🔗
Returns list of script support overrides.
Array[Dictionary]font_get_size_cache_info(font_rid:RID)const🔗
Returns font cache information, each entry contains the following fields:Vector2isize_px- font size in pixels,floatviewport_oversampling- viewport oversampling factor,intglyphs- number of rendered glyphs,inttextures- number of used textures,inttextures_size- size of texture data in bytes.
Array[Vector2i]font_get_size_cache_list(font_rid:RID)const🔗
Returns list of the font sizes in the cache. Each size isVector2iwith font size and outline size.
intfont_get_spacing(font_rid:RID, spacing:SpacingType)const🔗
Returns the spacing forspacingin pixels (not relative to the font size).
intfont_get_stretch(font_rid:RID)const🔗
Returns font stretch amount, compared to a normal width. A percentage value between50%and200%.
BitField[FontStyle]font_get_style(font_rid:RID)const🔗
Returns font style flags.
Stringfont_get_style_name(font_rid:RID)const🔗
Returns font style name.
SubpixelPositioningfont_get_subpixel_positioning(font_rid:RID)const🔗
Returns font subpixel glyph positioning mode.
Stringfont_get_supported_chars(font_rid:RID)const🔗
Returns a string containing all the characters available in the font.
PackedInt32Arrayfont_get_supported_glyphs(font_rid:RID)const🔗
Returns an array containing all glyph indices in the font.
intfont_get_texture_count(font_rid:RID, size:Vector2i)const🔗
Returns number of textures used by font cache entry.
Imagefont_get_texture_image(font_rid:RID, size:Vector2i, texture_index:int)const🔗
Returns font cache texture image data.
PackedInt32Arrayfont_get_texture_offsets(font_rid:RID, size:Vector2i, texture_index:int)const🔗
Returns array containing glyph packing data.
Transform2Dfont_get_transform(font_rid:RID)const🔗
Returns 2D transform applied to the font outlines.
floatfont_get_underline_position(font_rid:RID, size:int)const🔗
Returns pixel offset of the underline below the baseline.
floatfont_get_underline_thickness(font_rid:RID, size:int)const🔗
Returns thickness of the underline in pixels.
Dictionaryfont_get_variation_coordinates(font_rid:RID)const🔗
Returns variation coordinates for the specified font cache entry. Seefont_supported_variation_list()for more info.
intfont_get_weight(font_rid:RID)const🔗
Returns weight (boldness) of the font. A value in the100...999range, normal font weight is400, bold font weight is700.
boolfont_has_char(font_rid:RID, char:int)const🔗
Returnstrueif a Unicodecharis available in the font.
boolfont_is_allow_system_fallback(font_rid:RID)const🔗
Returnstrueif system fonts can be automatically used as fallbacks.
boolfont_is_force_autohinter(font_rid:RID)const🔗
Returnstrueif auto-hinting is supported and preferred over font built-in hinting. Used by dynamic fonts only.
boolfont_is_language_supported(font_rid:RID, language:String)const🔗
Returnstrueif the font supports the given language (as aISO 639code).
boolfont_is_modulate_color_glyphs(font_rid:RID)const🔗
Returnstrueif color modulation is applied when drawing the font's colored glyphs.
boolfont_is_multichannel_signed_distance_field(font_rid:RID)const🔗
Returnstrueif glyphs of all sizes are rendered using single multichannel signed distance field generated from the dynamic font vector data.
boolfont_is_script_supported(font_rid:RID, script:String)const🔗
Returnstrueif the font supports the given script (as aISO 15924code).
voidfont_remove_glyph(font_rid:RID, size:Vector2i, glyph:int)🔗
Removes specified rendered glyph information from the cache entry.
Note:This function will not remove textures associated with the glyphs, usefont_remove_texture()to remove them manually.
voidfont_remove_kerning(font_rid:RID, size:int, glyph_pair:Vector2i)🔗
Removes kerning override for the pair of glyphs.
voidfont_remove_language_support_override(font_rid:RID, language:String)🔗
Remove language support override.
voidfont_remove_script_support_override(font_rid:RID, script:String)🔗
Removes script support override.
voidfont_remove_size_cache(font_rid:RID, size:Vector2i)🔗
Removes specified font size from the cache entry.
voidfont_remove_texture(font_rid:RID, size:Vector2i, texture_index:int)🔗
Removes specified texture from the cache entry.
Note:This function will not remove glyphs associated with the texture, remove them manually, usingfont_remove_glyph().
voidfont_render_glyph(font_rid:RID, size:Vector2i, index:int)🔗
Renders specified glyph to the font cache texture.
voidfont_render_range(font_rid:RID, size:Vector2i, start:int, end:int)🔗
Renders the range of characters to the font cache texture.
voidfont_set_allow_system_fallback(font_rid:RID, allow_system_fallback:bool)🔗
If set totrue, system fonts can be automatically used as fallbacks.
voidfont_set_antialiasing(font_rid:RID, antialiasing:FontAntialiasing)🔗
Sets font anti-aliasing mode.
voidfont_set_ascent(font_rid:RID, size:int, ascent:float)🔗
Sets the font ascent (number of pixels above the baseline).
voidfont_set_baseline_offset(font_rid:RID, baseline_offset:float)🔗
Sets extra baseline offset (as a fraction of font height).
voidfont_set_data(font_rid:RID, data:PackedByteArray)🔗
Sets font source data, e.g contents of the dynamic font source file.
voidfont_set_descent(font_rid:RID, size:int, descent:float)🔗
Sets the font descent (number of pixels below the baseline).
voidfont_set_disable_embedded_bitmaps(font_rid:RID, disable_embedded_bitmaps:bool)🔗
If set totrue, embedded font bitmap loading is disabled (bitmap-only and color fonts ignore this property).
voidfont_set_embolden(font_rid:RID, strength:float)🔗
Sets font embolden strength. Ifstrengthis not equal to zero, emboldens the font outlines. Negative values reduce the outline thickness.
voidfont_set_face_index(font_rid:RID, face_index:int)🔗
Sets an active face index in the TrueType / OpenType collection.
voidfont_set_fixed_size(font_rid:RID, fixed_size:int)🔗
Sets bitmap font fixed size. If set to value greater than zero, same cache entry will be used for all font sizes.
voidfont_set_fixed_size_scale_mode(font_rid:RID, fixed_size_scale_mode:FixedSizeScaleMode)🔗
Sets bitmap font scaling mode. This property is used only iffixed_sizeis greater than zero.
voidfont_set_force_autohinter(font_rid:RID, force_autohinter:bool)🔗
If set totrueauto-hinting is preferred over font built-in hinting.
voidfont_set_generate_mipmaps(font_rid:RID, generate_mipmaps:bool)🔗
If set totruefont texture mipmap generation is enabled.
voidfont_set_global_oversampling(oversampling:float)🔗
Deprecated:UseViewportoversampling, or theoversamplingargument of thedraw_*methods instead.
This method does nothing.
voidfont_set_glyph_advance(font_rid:RID, size:int, glyph:int, advance:Vector2)🔗
Sets glyph advance (offset of the next glyph).
Note:Advance for glyphs outlines is the same as the base glyph advance and is not saved.
voidfont_set_glyph_offset(font_rid:RID, size:Vector2i, glyph:int, offset:Vector2)🔗
Sets glyph offset from the baseline.
voidfont_set_glyph_size(font_rid:RID, size:Vector2i, glyph:int, gl_size:Vector2)🔗
Sets size of the glyph.
voidfont_set_glyph_texture_idx(font_rid:RID, size:Vector2i, glyph:int, texture_idx:int)🔗
Sets index of the cache texture containing the glyph.
voidfont_set_glyph_uv_rect(font_rid:RID, size:Vector2i, glyph:int, uv_rect:Rect2)🔗
Sets rectangle in the cache texture containing the glyph.
voidfont_set_hinting(font_rid:RID, hinting:Hinting)🔗
Sets font hinting mode. Used by dynamic fonts only.
voidfont_set_keep_rounding_remainders(font_rid:RID, keep_rounding_remainders:bool)🔗
Sets glyph position rounding behavior. If set totrue, when aligning glyphs to the pixel boundaries rounding remainders are accumulated to ensure more uniform glyph distribution. This setting has no effect if subpixel positioning is enabled.
voidfont_set_kerning(font_rid:RID, size:int, glyph_pair:Vector2i, kerning:Vector2)🔗
Sets kerning for the pair of glyphs.
voidfont_set_language_support_override(font_rid:RID, language:String, supported:bool)🔗
Adds override forfont_is_language_supported().
voidfont_set_modulate_color_glyphs(font_rid:RID, force_autohinter:bool)🔗
If set totrue, color modulation is applied when drawing colored glyphs, otherwise it's applied to the monochrome glyphs only.
voidfont_set_msdf_pixel_range(font_rid:RID, msdf_pixel_range:int)🔗
Sets the width of the range around the shape between the minimum and maximum representable signed distance.
voidfont_set_msdf_size(font_rid:RID, msdf_size:int)🔗
Sets source font size used to generate MSDF textures.
voidfont_set_multichannel_signed_distance_field(font_rid:RID, msdf:bool)🔗
If set totrue, glyphs of all sizes are rendered using single multichannel signed distance field generated from the dynamic font vector data. MSDF rendering allows displaying the font at any scaling factor without blurriness, and without incurring a CPU cost when the font size changes (since the font no longer needs to be rasterized on the CPU). As a downside, font hinting is not available with MSDF. The lack of font hinting may result in less crisp and less readable fonts at small sizes.
Note:MSDF font rendering does not render glyphs with overlapping shapes correctly. Overlapping shapes are not valid per the OpenType standard, but are still commonly found in many font files, especially those converted by Google Fonts. To avoid issues with overlapping glyphs, consider downloading the font file directly from the type foundry instead of relying on Google Fonts.
voidfont_set_name(font_rid:RID, name:String)🔗
Sets the font family name.
voidfont_set_opentype_feature_overrides(font_rid:RID, overrides:Dictionary)🔗
Sets font OpenType feature set override.
voidfont_set_oversampling(font_rid:RID, oversampling:float)🔗
If set to a positive value, overrides the oversampling factor of the viewport this font is used in. SeeViewport.oversampling. This value doesn't override theoversamplingparameter ofdraw_*methods. Used by dynamic fonts only.
voidfont_set_scale(font_rid:RID, size:int, scale:float)🔗
Sets scaling factor of the color bitmap font.
voidfont_set_script_support_override(font_rid:RID, script:String, supported:bool)🔗
Adds override forfont_is_script_supported().
voidfont_set_spacing(font_rid:RID, spacing:SpacingType, value:int)🔗
Sets the spacing forspacingtovaluein pixels (not relative to the font size).
voidfont_set_stretch(font_rid:RID, weight:int)🔗
Sets font stretch amount, compared to a normal width. A percentage value between50%and200%.
Note:This value is used for font matching only and will not affect font rendering. Usefont_set_face_index(),font_set_variation_coordinates(), orfont_set_transform()instead.
voidfont_set_style(font_rid:RID, style:BitField[FontStyle])🔗
Sets the font style flags.
Note:This value is used for font matching only and will not affect font rendering. Usefont_set_face_index(),font_set_variation_coordinates(),font_set_embolden(), orfont_set_transform()instead.
voidfont_set_style_name(font_rid:RID, name:String)🔗
Sets the font style name.
voidfont_set_subpixel_positioning(font_rid:RID, subpixel_positioning:SubpixelPositioning)🔗
Sets font subpixel glyph positioning mode.
voidfont_set_texture_image(font_rid:RID, size:Vector2i, texture_index:int, image:Image)🔗
Sets font cache texture image data.
voidfont_set_texture_offsets(font_rid:RID, size:Vector2i, texture_index:int, offset:PackedInt32Array)🔗
Sets array containing glyph packing data.
voidfont_set_transform(font_rid:RID, transform:Transform2D)🔗
Sets 2D transform, applied to the font outlines, can be used for slanting, flipping, and rotating glyphs.
For example, to simulate italic typeface by slanting, apply the following transformTransform2D(1.0,slant,0.0,1.0,0.0,0.0).
voidfont_set_underline_position(font_rid:RID, size:int, underline_position:float)🔗
Sets pixel offset of the underline below the baseline.
voidfont_set_underline_thickness(font_rid:RID, size:int, underline_thickness:float)🔗
Sets thickness of the underline in pixels.
voidfont_set_variation_coordinates(font_rid:RID, variation_coordinates:Dictionary)🔗
Sets variation coordinates for the specified font cache entry. Seefont_supported_variation_list()for more info.
voidfont_set_weight(font_rid:RID, weight:int)🔗
Sets weight (boldness) of the font. A value in the100...999range, normal font weight is400, bold font weight is700.
Note:This value is used for font matching only and will not affect font rendering. Usefont_set_face_index(),font_set_variation_coordinates(), orfont_set_embolden()instead.
Dictionaryfont_supported_feature_list(font_rid:RID)const🔗
Returns the dictionary of the supported OpenType features.
Dictionaryfont_supported_variation_list(font_rid:RID)const🔗
Returns the dictionary of the supported OpenType variation coordinates.
Stringformat_number(number:String, language:String= "")const🔗
Deprecated:UseTranslationServer.format_number()instead.
Converts a number from Western Arabic (0..9) to the numeral system used in the givenlanguage.
Iflanguageis an empty string, the active locale will be used.
voidfree_rid(rid:RID)🔗
Frees an object created by thisTextServer.
intget_features()const🔗
Returns text server features, seeFeature.
Vector2get_hex_code_box_size(size:int, index:int)const🔗
Returns size of the replacement character (box with character hexadecimal code that is drawn in place of invalid characters).
Stringget_name()const🔗
Returns the name of the server interface.
PackedByteArrayget_support_data()const🔗
Returns default TextServer database (e.g. ICU break iterators and dictionaries).
Stringget_support_data_filename()const🔗
Returns default TextServer database (e.g. ICU break iterators and dictionaries) filename.
Stringget_support_data_info()const🔗
Returns TextServer database (e.g. ICU break iterators and dictionaries) description.
boolhas(rid:RID)🔗
Returnstrueifridis valid resource owned by this text server.
boolhas_feature(feature:Feature)const🔗
Returnstrueif the server supports a feature.
intis_confusable(string:String, dict:PackedStringArray)const🔗
Returns index of the first string indictwhich is visually confusable with thestring, or-1if none is found.
Note:This method doesn't detect invisible characters, for spoof detection use it in combination withspoof_check().
Note:Always returns-1if the server does not support theFEATURE_UNICODE_SECURITYfeature.
boolis_locale_right_to_left(locale:String)const🔗
Returnstrueif locale is right-to-left.
boolis_locale_using_support_data(locale:String)const🔗
Returnstrueif the locale requires text server support data for line/word breaking.
boolis_valid_identifier(string:String)const🔗
Returnstrueifstringis a valid identifier.
If the text server supports theFEATURE_UNICODE_IDENTIFIERSfeature, a valid identifier must:
- Conform to normalization form C.
Conform to normalization form C.
- Begin with a Unicode character of class XID_Start or"*".
Begin with a Unicode character of class XID_Start or"*".
- May contain Unicode characters of class XID_Continue in the other positions.
May contain Unicode characters of class XID_Continue in the other positions.
- Use UAX #31 recommended scripts only (mixed scripts are allowed).
Use UAX #31 recommended scripts only (mixed scripts are allowed).
If theFEATURE_UNICODE_IDENTIFIERSfeature is not supported, a valid identifier must:
- Begin with a Unicode character of class XID_Start or"*".
Begin with a Unicode character of class XID_Start or"*".
- May contain Unicode characters of class XID_Continue in the other positions.
May contain Unicode characters of class XID_Continue in the other positions.
boolis_valid_letter(unicode:int)const🔗
Returnstrueif the given code point is a valid letter, i.e. it belongs to the Unicode category "L".
boolload_support_data(filename:String)🔗
Loads optional TextServer database (e.g. ICU break iterators and dictionaries).
Note:This function should be called before any other TextServer functions used, otherwise it won't have any effect.
intname_to_tag(name:String)const🔗
Converts the given readable name of a feature, variation, script, or language to an OpenType tag.
Stringparse_number(number:String, language:String= "")const🔗
Deprecated:UseTranslationServer.parse_number()instead.
Convertsnumberfrom the numeral system used in the givenlanguageto Western Arabic (0..9).
Iflanguageis an empty string, the active locale will be used.
Array[Vector3i]parse_structured_text(parser_type:StructuredTextParser, args:Array, text:String)const🔗
Default implementation of the BiDi algorithm override function.
Stringpercent_sign(language:String= "")const🔗
Deprecated:UseTranslationServer.get_percent_sign()instead.
Returns the percent sign used in the givenlanguage.
Iflanguageis an empty string, the active locale will be used.
boolsave_support_data(filename:String)const🔗
Saves optional TextServer database (e.g. ICU break iterators and dictionaries) to the file.
Note:This function is used by during project export, to include TextServer database.
intshaped_get_run_count(shaped:RID)const🔗
Returns the number of uniform text runs in the buffer.
Directionshaped_get_run_direction(shaped:RID, index:int)const🔗
Returns the direction of theindextext run (in visual order).
RIDshaped_get_run_font_rid(shaped:RID, index:int)const🔗
Returns the font RID of theindextext run (in visual order).
intshaped_get_run_font_size(shaped:RID, index:int)const🔗
Returns the font size of theindextext run (in visual order).
Stringshaped_get_run_language(shaped:RID, index:int)const🔗
Returns the language of theindextext run (in visual order).
Variantshaped_get_run_object(shaped:RID, index:int)const🔗
Returns the embedded object of theindextext run (in visual order).
Vector2ishaped_get_run_range(shaped:RID, index:int)const🔗
Returns the source text range of theindextext run (in visual order).
Stringshaped_get_run_text(shaped:RID, index:int)const🔗
Returns the source text of theindextext run (in visual order).
intshaped_get_span_count(shaped:RID)const🔗
Returns number of text spans added usingshaped_text_add_string()orshaped_text_add_object().
Variantshaped_get_span_embedded_object(shaped:RID, index:int)const🔗
Returns text embedded object key.
Variantshaped_get_span_meta(shaped:RID, index:int)const🔗
Returns text span metadata.
Variantshaped_get_span_object(shaped:RID, index:int)const🔗
Returns the text span embedded object key.
Stringshaped_get_span_text(shaped:RID, index:int)const🔗
Returns the text span source text.
Stringshaped_get_text(shaped:RID)const🔗
Returns the text buffer source text, including object replacement characters.
voidshaped_set_span_update_font(shaped:RID, index:int, fonts:Array[RID], size:int, opentype_features:Dictionary= {})🔗
Changes text span font, font size, and OpenType features, without changing the text.
boolshaped_text_add_object(shaped:RID, key:Variant, size:Vector2, inline_align:InlineAlignment= 5, length:int= 1, baseline:float= 0.0)🔗
Adds inline object to the text buffer,keymust be unique. In the text, object is represented aslengthobject replacement characters.
boolshaped_text_add_string(shaped:RID, text:String, fonts:Array[RID], size:int, opentype_features:Dictionary= {}, language:String= "", meta:Variant= null)🔗
Adds text span and font to draw it to the text buffer.
voidshaped_text_clear(rid:RID)🔗
Clears text buffer (removes text and inline objects).
intshaped_text_closest_character_pos(shaped:RID, pos:int)const🔗
Returns composite character position closest to thepos.
voidshaped_text_draw(shaped:RID, canvas:RID, pos:Vector2, clip_l:float= -1, clip_r:float= -1, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const🔗
Draw shaped text into a canvas item at a given position, withcolor.posspecifies the leftmost point of the baseline (for horizontal layout) or topmost point of the baseline (for vertical layout). Ifoversamplingis greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.
clip_landclip_rare offsets relative topos, going to the right in horizontal layout and downward in vertical layout. Ifclip_lis not negative, glyphs starting before the offset are clipped. Ifclip_ris not negative, glyphs ending after the offset are clipped.
voidshaped_text_draw_outline(shaped:RID, canvas:RID, pos:Vector2, clip_l:float= -1, clip_r:float= -1, outline_size:int= 1, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const🔗
Draw the outline of the shaped text into a canvas item at a given position, withcolor.posspecifies the leftmost point of the baseline (for horizontal layout) or topmost point of the baseline (for vertical layout). Ifoversamplingis greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.
clip_landclip_rare offsets relative topos, going to the right in horizontal layout and downward in vertical layout. Ifclip_lis not negative, glyphs starting before the offset are clipped. Ifclip_ris not negative, glyphs ending after the offset are clipped.
RIDshaped_text_duplicate(rid:RID)🔗
Duplicates shaped text buffer.
floatshaped_text_fit_to_width(shaped:RID, width:float, justification_flags:BitField[JustificationFlag] = 3)🔗
Adjusts text width to fit to specified width, returns new text width.
floatshaped_text_get_ascent(shaped:RID)const🔗
Returns the text ascent (number of pixels above the baseline for horizontal layout or to the left of baseline for vertical).
Note:Overall ascent can be higher than font ascent, if some glyphs are displaced from the baseline.
Dictionaryshaped_text_get_carets(shaped:RID, position:int)const🔗
Returns shapes of the carets corresponding to the character offsetpositionin the text. Returned caret shape is 1 pixel wide rectangle.
PackedInt32Arrayshaped_text_get_character_breaks(shaped:RID)const🔗
Returns array of the composite character boundaries.
intshaped_text_get_custom_ellipsis(shaped:RID)const🔗
Returns ellipsis character used for text clipping.
Stringshaped_text_get_custom_punctuation(shaped:RID)const🔗
Returns custom punctuation character list, used for word breaking. If set to empty string, server defaults are used.
floatshaped_text_get_descent(shaped:RID)const🔗
Returns the text descent (number of pixels below the baseline for horizontal layout or to the right of baseline for vertical).
Note:Overall descent can be higher than font descent, if some glyphs are displaced from the baseline.
Directionshaped_text_get_direction(shaped:RID)const🔗
Returns direction of the text.
Directionshaped_text_get_dominant_direction_in_range(shaped:RID, start:int, end:int)const🔗
Returns dominant direction of in the range of text.
intshaped_text_get_ellipsis_glyph_count(shaped:RID)const🔗
Returns number of glyphs in the ellipsis.
Array[Dictionary]shaped_text_get_ellipsis_glyphs(shaped:RID)const🔗
Returns array of the glyphs in the ellipsis.
intshaped_text_get_ellipsis_pos(shaped:RID)const🔗
Returns position of the ellipsis.
intshaped_text_get_glyph_count(shaped:RID)const🔗
Returns number of glyphs in the buffer.
Array[Dictionary]shaped_text_get_glyphs(shaped:RID)const🔗
Returns an array of glyphs in the visual order.
Vector2shaped_text_get_grapheme_bounds(shaped:RID, pos:int)const🔗
Returns composite character's bounds as offsets from the start of the line.
Directionshaped_text_get_inferred_direction(shaped:RID)const🔗
Returns direction of the text, inferred by the BiDi algorithm.
PackedInt32Arrayshaped_text_get_line_breaks(shaped:RID, width:float, start:int= 0, break_flags:BitField[LineBreakFlag] = 3)const🔗
Breaks text to the lines and returns character ranges for each line.
PackedInt32Arrayshaped_text_get_line_breaks_adv(shaped:RID, width:PackedFloat32Array, start:int= 0, once:bool= true, break_flags:BitField[LineBreakFlag] = 3)const🔗
Breaks text to the lines and columns. Returns character ranges for each segment.
intshaped_text_get_object_glyph(shaped:RID, key:Variant)const🔗
Returns the glyph index of the inline object.
Vector2ishaped_text_get_object_range(shaped:RID, key:Variant)const🔗
Returns the character range of the inline object.
Rect2shaped_text_get_object_rect(shaped:RID, key:Variant)const🔗
Returns bounding rectangle of the inline object.
Arrayshaped_text_get_objects(shaped:RID)const🔗
Returns array of inline objects.
Orientationshaped_text_get_orientation(shaped:RID)const🔗
Returns text orientation.
RIDshaped_text_get_parent(shaped:RID)const🔗
Returns the parent buffer from which the substring originates.
boolshaped_text_get_preserve_control(shaped:RID)const🔗
Returnstrueif text buffer is configured to display control characters.
boolshaped_text_get_preserve_invalid(shaped:RID)const🔗
Returnstrueif text buffer is configured to display hexadecimal codes in place of invalid characters.
Note:If set tofalse, nothing is displayed in place of invalid characters.
Vector2ishaped_text_get_range(shaped:RID)const🔗
Returns substring buffer character range in the parent buffer.
PackedVector2Arrayshaped_text_get_selection(shaped:RID, start:int, end:int)const🔗
Returns selection rectangles for the specified character range.
Vector2shaped_text_get_size(shaped:RID)const🔗
Returns size of the text.
intshaped_text_get_spacing(shaped:RID, spacing:SpacingType)const🔗
Returns extra spacing added between glyphs or lines in pixels.
intshaped_text_get_trim_pos(shaped:RID)const🔗
Returns the position of the overrun trim.
floatshaped_text_get_underline_position(shaped:RID)const🔗
Returns pixel offset of the underline below the baseline.
floatshaped_text_get_underline_thickness(shaped:RID)const🔗
Returns thickness of the underline.
floatshaped_text_get_width(shaped:RID)const🔗
Returns width (for horizontal layout) or height (for vertical) of the text.
PackedInt32Arrayshaped_text_get_word_breaks(shaped:RID, grapheme_flags:BitField[GraphemeFlag] = 264, skip_grapheme_flags:BitField[GraphemeFlag] = 4)const🔗
Breaks text into words and returns array of character ranges. Usegrapheme_flagsto set what characters are used for breaking.
boolshaped_text_has_object(shaped:RID, key:Variant)const🔗
Returnstrueif an object withkeyis embedded in this shaped text buffer.
boolshaped_text_has_visible_chars(shaped:RID)const🔗
Returnstrueif text buffer contains any visible characters.
intshaped_text_hit_test_grapheme(shaped:RID, coords:float)const🔗
Returns grapheme index at the specified pixel offset at the baseline, or-1if none is found.
intshaped_text_hit_test_position(shaped:RID, coords:float)const🔗
Returns caret character offset at the specified pixel offset at the baseline. This function always returns a valid position.
boolshaped_text_is_ready(shaped:RID)const🔗
Returnstrueif buffer is successfully shaped.
intshaped_text_next_character_pos(shaped:RID, pos:int)const🔗
Returns composite character end position closest to thepos.
intshaped_text_next_grapheme_pos(shaped:RID, pos:int)const🔗
Returns grapheme end position closest to thepos.
voidshaped_text_overrun_trim_to_width(shaped:RID, width:float= 0, overrun_trim_flags:BitField[TextOverrunFlag] = 0)🔗
Trims text if it exceeds the given width.
intshaped_text_prev_character_pos(shaped:RID, pos:int)const🔗
Returns composite character start position closest to thepos.
intshaped_text_prev_grapheme_pos(shaped:RID, pos:int)const🔗
Returns grapheme start position closest to thepos.
boolshaped_text_resize_object(shaped:RID, key:Variant, size:Vector2, inline_align:InlineAlignment= 5, baseline:float= 0.0)🔗
Sets new size and alignment of embedded object.
voidshaped_text_set_bidi_override(shaped:RID, override:Array)🔗
Overrides BiDi for the structured text.
Override ranges should cover full source text without overlaps. BiDi algorithm will be used on each range separately.
voidshaped_text_set_custom_ellipsis(shaped:RID, char:int)🔗
Sets ellipsis character used for text clipping.
voidshaped_text_set_custom_punctuation(shaped:RID, punct:String)🔗
Sets custom punctuation character list, used for word breaking. If set to empty string, server defaults are used.
voidshaped_text_set_direction(shaped:RID, direction:Direction= 0)🔗
Sets desired text direction. If set toDIRECTION_AUTO, direction will be detected based on the buffer contents and current locale.
Note:Direction is ignored if server does not supportFEATURE_BIDI_LAYOUTfeature (supported byTextServerAdvanced).
voidshaped_text_set_orientation(shaped:RID, orientation:Orientation= 0)🔗
Sets desired text orientation.
Note:Orientation is ignored if server does not supportFEATURE_VERTICAL_LAYOUTfeature (supported byTextServerAdvanced).
voidshaped_text_set_preserve_control(shaped:RID, enabled:bool)🔗
If set totruetext buffer will display control characters.
voidshaped_text_set_preserve_invalid(shaped:RID, enabled:bool)🔗
If set totruetext buffer will display invalid characters as hexadecimal codes, otherwise nothing is displayed.
voidshaped_text_set_spacing(shaped:RID, spacing:SpacingType, value:int)🔗
Sets extra spacing added between glyphs or lines in pixels.
boolshaped_text_shape(shaped:RID)🔗
Shapes buffer if it's not shaped. Returnstrueif the string is shaped successfully.
Note:It is not necessary to call this function manually, buffer will be shaped automatically as soon as any of its output data is requested.
Array[Dictionary]shaped_text_sort_logical(shaped:RID)🔗
Returns text glyphs in the logical order.
RIDshaped_text_substr(shaped:RID, start:int, length:int)const🔗
Returns text buffer for the substring of the text in theshapedtext buffer (including inline objects).
floatshaped_text_tab_align(shaped:RID, tab_stops:PackedFloat32Array)🔗
Aligns shaped text to the given tab-stops.
boolspoof_check(string:String)const🔗
Returnstrueifstringis likely to be an attempt at confusing the reader.
Note:Always returnsfalseif the server does not support theFEATURE_UNICODE_SECURITYfeature.
PackedInt32Arraystring_get_character_breaks(string:String, language:String= "")const🔗
Returns array of the composite character boundaries.

```
var ts = TextServerManager.get_primary_interface()
print(ts.string_get_character_breaks("Test ❤️‍🔥 Test")) # Prints [1, 2, 3, 4, 5, 9, 10, 11, 12, 13, 14]
```

PackedInt32Arraystring_get_word_breaks(string:String, language:String= "", chars_per_line:int= 0)const🔗
Returns an array of the word break boundaries. Elements in the returned array are the offsets of the start and end of words. Therefore the length of the array is always even.
Whenchars_per_lineis greater than zero, line break boundaries are returned instead.

```
var ts = TextServerManager.get_primary_interface()
# Corresponds to the substrings "The", "Godot", "Engine", and "4".
print(ts.string_get_word_breaks("The Godot Engine, 4")) # Prints [0, 3, 4, 9, 10, 16, 18, 19]
# Corresponds to the substrings "The", "Godot", "Engin", and "e, 4".
print(ts.string_get_word_breaks("The Godot Engine, 4", "en", 5)) # Prints [0, 3, 4, 9, 10, 15, 15, 19]
# Corresponds to the substrings "The Godot" and "Engine, 4".
print(ts.string_get_word_breaks("The Godot Engine, 4", "en", 10)) # Prints [0, 9, 10, 19]
```

Stringstring_to_lower(string:String, language:String= "")const🔗
Returns the string converted tolowercase.
Note:Casing is locale dependent and context sensitive if server supportFEATURE_CONTEXT_SENSITIVE_CASE_CONVERSIONfeature (supported byTextServerAdvanced).
Note:The result may be longer or shorter than the original.
Stringstring_to_title(string:String, language:String= "")const🔗
Returns the string converted toTitleCase.
Note:Casing is locale dependent and context sensitive if server supportFEATURE_CONTEXT_SENSITIVE_CASE_CONVERSIONfeature (supported byTextServerAdvanced).
Note:The result may be longer or shorter than the original.
Stringstring_to_upper(string:String, language:String= "")const🔗
Returns the string converted toUPPERCASE.
Note:Casing is locale dependent and context sensitive if server supportFEATURE_CONTEXT_SENSITIVE_CASE_CONVERSIONfeature (supported byTextServerAdvanced).
Note:The result may be longer or shorter than the original.
Stringstrip_diacritics(string:String)const🔗
Strips diacritics from the string.
Note:The result may be longer or shorter than the original.
Stringtag_to_name(tag:int)const🔗
Converts the given OpenType tag to the readable name of a feature, variation, script, or language.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
