# TextServerExtension in English

# TextServerExtension

Inherits:TextServer<RefCounted<Object
Inherited By:TextServerAdvanced,TextServerDummy,TextServerFallback
Base class for customTextServerimplementations (plugins).

## Description

ExternalTextServerimplementations should inherit from this class.

## Methods

| void | _cleanup()virtual |
|---|---|
| RID | _create_font()virtualrequired |
| RID | _create_font_linked_variation(font_rid:RID)virtual |
| RID | _create_shaped_text(direction:Direction, orientation:Orientation)virtualrequired |
| void | _draw_hex_code_box(canvas:RID, size:int, pos:Vector2, index:int, color:Color)virtualconst |
| void | _font_clear_glyphs(font_rid:RID, size:Vector2i)virtualrequired |
| void | _font_clear_kerning_map(font_rid:RID, size:int)virtual |
| void | _font_clear_size_cache(font_rid:RID)virtualrequired |
| void | _font_clear_system_fallback_cache()virtual |
| void | _font_clear_textures(font_rid:RID, size:Vector2i)virtualrequired |
| void | _font_draw_glyph(font_rid:RID, canvas:RID, size:int, pos:Vector2, index:int, color:Color, oversampling:float)virtualrequiredconst |
| void | _font_draw_glyph_outline(font_rid:RID, canvas:RID, size:int, outline_size:int, pos:Vector2, index:int, color:Color, oversampling:float)virtualrequiredconst |
| FontAntialiasing | _font_get_antialiasing(font_rid:RID)virtualconst |
| float | _font_get_ascent(font_rid:RID, size:int)virtualrequiredconst |
| float | _font_get_baseline_offset(font_rid:RID)virtualconst |
| int | _font_get_char_from_glyph_index(font_rid:RID, size:int, glyph_index:int)virtualrequiredconst |
| float | _font_get_descent(font_rid:RID, size:int)virtualrequiredconst |
| bool | _font_get_disable_embedded_bitmaps(font_rid:RID)virtualconst |
| float | _font_get_embolden(font_rid:RID)virtualconst |
| int | _font_get_face_count(font_rid:RID)virtualconst |
| int | _font_get_face_index(font_rid:RID)virtualconst |
| int | _font_get_fixed_size(font_rid:RID)virtualrequiredconst |
| FixedSizeScaleMode | _font_get_fixed_size_scale_mode(font_rid:RID)virtualrequiredconst |
| bool | _font_get_generate_mipmaps(font_rid:RID)virtualconst |
| float | _font_get_global_oversampling()virtualconst |
| Vector2 | _font_get_glyph_advance(font_rid:RID, size:int, glyph:int)virtualrequiredconst |
| Dictionary | _font_get_glyph_contours(font_rid:RID, size:int, index:int)virtualconst |
| int | _font_get_glyph_index(font_rid:RID, size:int, char:int, variation_selector:int)virtualrequiredconst |
| PackedInt32Array | _font_get_glyph_list(font_rid:RID, size:Vector2i)virtualrequiredconst |
| Vector2 | _font_get_glyph_offset(font_rid:RID, size:Vector2i, glyph:int)virtualrequiredconst |
| Vector2 | _font_get_glyph_size(font_rid:RID, size:Vector2i, glyph:int)virtualrequiredconst |
| int | _font_get_glyph_texture_idx(font_rid:RID, size:Vector2i, glyph:int)virtualrequiredconst |
| RID | _font_get_glyph_texture_rid(font_rid:RID, size:Vector2i, glyph:int)virtualrequiredconst |
| Vector2 | _font_get_glyph_texture_size(font_rid:RID, size:Vector2i, glyph:int)virtualrequiredconst |
| Rect2 | _font_get_glyph_uv_rect(font_rid:RID, size:Vector2i, glyph:int)virtualrequiredconst |
| Hinting | _font_get_hinting(font_rid:RID)virtualconst |
| bool | _font_get_keep_rounding_remainders(font_rid:RID)virtualconst |
| Vector2 | _font_get_kerning(font_rid:RID, size:int, glyph_pair:Vector2i)virtualconst |
| Array[Vector2i] | _font_get_kerning_list(font_rid:RID, size:int)virtualconst |
| bool | _font_get_language_support_override(font_rid:RID, language:String)virtual |
| PackedStringArray | _font_get_language_support_overrides(font_rid:RID)virtual |
| int | _font_get_msdf_pixel_range(font_rid:RID)virtualconst |
| int | _font_get_msdf_size(font_rid:RID)virtualconst |
| String | _font_get_name(font_rid:RID)virtualconst |
| Dictionary | _font_get_opentype_feature_overrides(font_rid:RID)virtualconst |
| Dictionary | _font_get_ot_name_strings(font_rid:RID)virtualconst |
| float | _font_get_oversampling(font_rid:RID)virtualconst |
| float | _font_get_scale(font_rid:RID, size:int)virtualrequiredconst |
| bool | _font_get_script_support_override(font_rid:RID, script:String)virtual |
| PackedStringArray | _font_get_script_support_overrides(font_rid:RID)virtual |
| Array[Dictionary] | _font_get_size_cache_info(font_rid:RID)virtualconst |
| Array[Vector2i] | _font_get_size_cache_list(font_rid:RID)virtualrequiredconst |
| int | _font_get_spacing(font_rid:RID, spacing:SpacingType)virtualconst |
| int | _font_get_stretch(font_rid:RID)virtualconst |
| BitField[FontStyle] | _font_get_style(font_rid:RID)virtualconst |
| String | _font_get_style_name(font_rid:RID)virtualconst |
| SubpixelPositioning | _font_get_subpixel_positioning(font_rid:RID)virtualconst |
| String | _font_get_supported_chars(font_rid:RID)virtualrequiredconst |
| PackedInt32Array | _font_get_supported_glyphs(font_rid:RID)virtualrequiredconst |
| int | _font_get_texture_count(font_rid:RID, size:Vector2i)virtualrequiredconst |
| Image | _font_get_texture_image(font_rid:RID, size:Vector2i, texture_index:int)virtualrequiredconst |
| PackedInt32Array | _font_get_texture_offsets(font_rid:RID, size:Vector2i, texture_index:int)virtualconst |
| Transform2D | _font_get_transform(font_rid:RID)virtualconst |
| float | _font_get_underline_position(font_rid:RID, size:int)virtualrequiredconst |
| float | _font_get_underline_thickness(font_rid:RID, size:int)virtualrequiredconst |
| Dictionary | _font_get_variation_coordinates(font_rid:RID)virtualconst |
| int | _font_get_weight(font_rid:RID)virtualconst |
| bool | _font_has_char(font_rid:RID, char:int)virtualrequiredconst |
| bool | _font_is_allow_system_fallback(font_rid:RID)virtualconst |
| bool | _font_is_force_autohinter(font_rid:RID)virtualconst |
| bool | _font_is_language_supported(font_rid:RID, language:String)virtualconst |
| bool | _font_is_modulate_color_glyphs(font_rid:RID)virtualconst |
| bool | _font_is_multichannel_signed_distance_field(font_rid:RID)virtualconst |
| bool | _font_is_script_supported(font_rid:RID, script:String)virtualconst |
| void | _font_remove_glyph(font_rid:RID, size:Vector2i, glyph:int)virtualrequired |
| void | _font_remove_kerning(font_rid:RID, size:int, glyph_pair:Vector2i)virtual |
| void | _font_remove_language_support_override(font_rid:RID, language:String)virtual |
| void | _font_remove_script_support_override(font_rid:RID, script:String)virtual |
| void | _font_remove_size_cache(font_rid:RID, size:Vector2i)virtualrequired |
| void | _font_remove_texture(font_rid:RID, size:Vector2i, texture_index:int)virtualrequired |
| void | _font_render_glyph(font_rid:RID, size:Vector2i, index:int)virtual |
| void | _font_render_range(font_rid:RID, size:Vector2i, start:int, end:int)virtual |
| void | _font_set_allow_system_fallback(font_rid:RID, allow_system_fallback:bool)virtual |
| void | _font_set_antialiasing(font_rid:RID, antialiasing:FontAntialiasing)virtual |
| void | _font_set_ascent(font_rid:RID, size:int, ascent:float)virtualrequired |
| void | _font_set_baseline_offset(font_rid:RID, baseline_offset:float)virtual |
| void | _font_set_data(font_rid:RID, data:PackedByteArray)virtual |
| void | _font_set_data_ptr(font_rid:RID, data_ptr:constuint8_t*, data_size:int)virtual |
| void | _font_set_descent(font_rid:RID, size:int, descent:float)virtualrequired |
| void | _font_set_disable_embedded_bitmaps(font_rid:RID, disable_embedded_bitmaps:bool)virtual |
| void | _font_set_embolden(font_rid:RID, strength:float)virtual |
| void | _font_set_face_index(font_rid:RID, face_index:int)virtual |
| void | _font_set_fixed_size(font_rid:RID, fixed_size:int)virtualrequired |
| void | _font_set_fixed_size_scale_mode(font_rid:RID, fixed_size_scale_mode:FixedSizeScaleMode)virtualrequired |
| void | _font_set_force_autohinter(font_rid:RID, force_autohinter:bool)virtual |
| void | _font_set_generate_mipmaps(font_rid:RID, generate_mipmaps:bool)virtual |
| void | _font_set_global_oversampling(oversampling:float)virtual |
| void | _font_set_glyph_advance(font_rid:RID, size:int, glyph:int, advance:Vector2)virtualrequired |
| void | _font_set_glyph_offset(font_rid:RID, size:Vector2i, glyph:int, offset:Vector2)virtualrequired |
| void | _font_set_glyph_size(font_rid:RID, size:Vector2i, glyph:int, gl_size:Vector2)virtualrequired |
| void | _font_set_glyph_texture_idx(font_rid:RID, size:Vector2i, glyph:int, texture_idx:int)virtualrequired |
| void | _font_set_glyph_uv_rect(font_rid:RID, size:Vector2i, glyph:int, uv_rect:Rect2)virtualrequired |
| void | _font_set_hinting(font_rid:RID, hinting:Hinting)virtual |
| void | _font_set_keep_rounding_remainders(font_rid:RID, keep_rounding_remainders:bool)virtual |
| void | _font_set_kerning(font_rid:RID, size:int, glyph_pair:Vector2i, kerning:Vector2)virtual |
| void | _font_set_language_support_override(font_rid:RID, language:String, supported:bool)virtual |
| void | _font_set_modulate_color_glyphs(font_rid:RID, modulate:bool)virtual |
| void | _font_set_msdf_pixel_range(font_rid:RID, msdf_pixel_range:int)virtual |
| void | _font_set_msdf_size(font_rid:RID, msdf_size:int)virtual |
| void | _font_set_multichannel_signed_distance_field(font_rid:RID, msdf:bool)virtual |
| void | _font_set_name(font_rid:RID, name:String)virtual |
| void | _font_set_opentype_feature_overrides(font_rid:RID, overrides:Dictionary)virtual |
| void | _font_set_oversampling(font_rid:RID, oversampling:float)virtual |
| void | _font_set_scale(font_rid:RID, size:int, scale:float)virtualrequired |
| void | _font_set_script_support_override(font_rid:RID, script:String, supported:bool)virtual |
| void | _font_set_spacing(font_rid:RID, spacing:SpacingType, value:int)virtual |
| void | _font_set_stretch(font_rid:RID, stretch:int)virtual |
| void | _font_set_style(font_rid:RID, style:BitField[FontStyle])virtual |
| void | _font_set_style_name(font_rid:RID, name_style:String)virtual |
| void | _font_set_subpixel_positioning(font_rid:RID, subpixel_positioning:SubpixelPositioning)virtual |
| void | _font_set_texture_image(font_rid:RID, size:Vector2i, texture_index:int, image:Image)virtualrequired |
| void | _font_set_texture_offsets(font_rid:RID, size:Vector2i, texture_index:int, offset:PackedInt32Array)virtual |
| void | _font_set_transform(font_rid:RID, transform:Transform2D)virtual |
| void | _font_set_underline_position(font_rid:RID, size:int, underline_position:float)virtualrequired |
| void | _font_set_underline_thickness(font_rid:RID, size:int, underline_thickness:float)virtualrequired |
| void | _font_set_variation_coordinates(font_rid:RID, variation_coordinates:Dictionary)virtual |
| void | _font_set_weight(font_rid:RID, weight:int)virtual |
| Dictionary | _font_supported_feature_list(font_rid:RID)virtualconst |
| Dictionary | _font_supported_variation_list(font_rid:RID)virtualconst |
| String | _format_number(number:String, language:String)virtualconst |
| void | _free_rid(rid:RID)virtualrequired |
| int | _get_features()virtualrequiredconst |
| Vector2 | _get_hex_code_box_size(size:int, index:int)virtualconst |
| String | _get_name()virtualrequiredconst |
| PackedByteArray | _get_support_data()virtualconst |
| String | _get_support_data_filename()virtualconst |
| String | _get_support_data_info()virtualconst |
| bool | _has(rid:RID)virtualrequired |
| bool | _has_feature(feature:Feature)virtualrequiredconst |
| int | _is_confusable(string:String, dict:PackedStringArray)virtualconst |
| bool | _is_locale_right_to_left(locale:String)virtualconst |
| bool | _is_locale_using_support_data(locale:String)virtualconst |
| bool | _is_valid_identifier(string:String)virtualconst |
| bool | _is_valid_letter(unicode:int)virtualconst |
| bool | _load_support_data(filename:String)virtual |
| int | _name_to_tag(name:String)virtualconst |
| String | _parse_number(number:String, language:String)virtualconst |
| Array[Vector3i] | _parse_structured_text(parser_type:StructuredTextParser, args:Array, text:String)virtualconst |
| String | _percent_sign(language:String)virtualconst |
| void | _reference_oversampling_level(oversampling:float)virtual |
| bool | _save_support_data(filename:String)virtualconst |
| int | _shaped_get_run_count(shaped:RID)virtualconst |
| Direction | _shaped_get_run_direction(shaped:RID, index:int)virtualconst |
| RID | _shaped_get_run_font_rid(shaped:RID, index:int)virtualconst |
| int | _shaped_get_run_font_size(shaped:RID, index:int)virtualconst |
| String | _shaped_get_run_language(shaped:RID, index:int)virtualconst |
| Variant | _shaped_get_run_object(shaped:RID, index:int)virtualconst |
| Vector2i | _shaped_get_run_range(shaped:RID, index:int)virtualconst |
| String | _shaped_get_run_text(shaped:RID, index:int)virtualconst |
| int | _shaped_get_span_count(shaped:RID)virtualrequiredconst |
| Variant | _shaped_get_span_embedded_object(shaped:RID, index:int)virtualrequiredconst |
| Variant | _shaped_get_span_meta(shaped:RID, index:int)virtualrequiredconst |
| Variant | _shaped_get_span_object(shaped:RID, index:int)virtualrequiredconst |
| String | _shaped_get_span_text(shaped:RID, index:int)virtualrequiredconst |
| String | _shaped_get_text(shaped:RID)virtualrequiredconst |
| void | _shaped_set_span_update_font(shaped:RID, index:int, fonts:Array[RID], size:int, opentype_features:Dictionary)virtualrequired |
| bool | _shaped_text_add_object(shaped:RID, key:Variant, size:Vector2, inline_align:InlineAlignment, length:int, baseline:float)virtualrequired |
| bool | _shaped_text_add_string(shaped:RID, text:String, fonts:Array[RID], size:int, opentype_features:Dictionary, language:String, meta:Variant)virtualrequired |
| void | _shaped_text_clear(shaped:RID)virtualrequired |
| int | _shaped_text_closest_character_pos(shaped:RID, pos:int)virtualconst |
| void | _shaped_text_draw(shaped:RID, canvas:RID, pos:Vector2, clip_l:float, clip_r:float, color:Color, oversampling:float)virtualconst |
| void | _shaped_text_draw_outline(shaped:RID, canvas:RID, pos:Vector2, clip_l:float, clip_r:float, outline_size:int, color:Color, oversampling:float)virtualconst |
| RID | _shaped_text_duplicate(shaped:RID)virtualrequired |
| float | _shaped_text_fit_to_width(shaped:RID, width:float, justification_flags:BitField[JustificationFlag])virtual |
| float | _shaped_text_get_ascent(shaped:RID)virtualrequiredconst |
| void | _shaped_text_get_carets(shaped:RID, position:int, caret:CaretInfo*)virtualconst |
| PackedInt32Array | _shaped_text_get_character_breaks(shaped:RID)virtualconst |
| int | _shaped_text_get_custom_ellipsis(shaped:RID)virtualconst |
| String | _shaped_text_get_custom_punctuation(shaped:RID)virtualconst |
| float | _shaped_text_get_descent(shaped:RID)virtualrequiredconst |
| Direction | _shaped_text_get_direction(shaped:RID)virtualconst |
| int | _shaped_text_get_dominant_direction_in_range(shaped:RID, start:int, end:int)virtualconst |
| int | _shaped_text_get_ellipsis_glyph_count(shaped:RID)virtualrequiredconst |
| constGlyph* | _shaped_text_get_ellipsis_glyphs(shaped:RID)virtualrequiredconst |
| int | _shaped_text_get_ellipsis_pos(shaped:RID)virtualrequiredconst |
| int | _shaped_text_get_glyph_count(shaped:RID)virtualrequiredconst |
| constGlyph* | _shaped_text_get_glyphs(shaped:RID)virtualrequiredconst |
| Vector2 | _shaped_text_get_grapheme_bounds(shaped:RID, pos:int)virtualconst |
| Direction | _shaped_text_get_inferred_direction(shaped:RID)virtualconst |
| PackedInt32Array | _shaped_text_get_line_breaks(shaped:RID, width:float, start:int, break_flags:BitField[LineBreakFlag])virtualconst |
| PackedInt32Array | _shaped_text_get_line_breaks_adv(shaped:RID, width:PackedFloat32Array, start:int, once:bool, break_flags:BitField[LineBreakFlag])virtualconst |
| int | _shaped_text_get_object_glyph(shaped:RID, key:Variant)virtualrequiredconst |
| Vector2i | _shaped_text_get_object_range(shaped:RID, key:Variant)virtualrequiredconst |
| Rect2 | _shaped_text_get_object_rect(shaped:RID, key:Variant)virtualrequiredconst |
| Array | _shaped_text_get_objects(shaped:RID)virtualrequiredconst |
| Orientation | _shaped_text_get_orientation(shaped:RID)virtualconst |
| RID | _shaped_text_get_parent(shaped:RID)virtualrequiredconst |
| bool | _shaped_text_get_preserve_control(shaped:RID)virtualconst |
| bool | _shaped_text_get_preserve_invalid(shaped:RID)virtualconst |
| Vector2i | _shaped_text_get_range(shaped:RID)virtualrequiredconst |
| PackedVector2Array | _shaped_text_get_selection(shaped:RID, start:int, end:int)virtualconst |
| Vector2 | _shaped_text_get_size(shaped:RID)virtualrequiredconst |
| int | _shaped_text_get_spacing(shaped:RID, spacing:SpacingType)virtualconst |
| int | _shaped_text_get_trim_pos(shaped:RID)virtualrequiredconst |
| float | _shaped_text_get_underline_position(shaped:RID)virtualrequiredconst |
| float | _shaped_text_get_underline_thickness(shaped:RID)virtualrequiredconst |
| float | _shaped_text_get_width(shaped:RID)virtualrequiredconst |
| PackedInt32Array | _shaped_text_get_word_breaks(shaped:RID, grapheme_flags:BitField[GraphemeFlag], skip_grapheme_flags:BitField[GraphemeFlag])virtualconst |
| bool | _shaped_text_has_object(shaped:RID, key:Variant)virtualrequiredconst |
| int | _shaped_text_hit_test_grapheme(shaped:RID, coord:float)virtualconst |
| int | _shaped_text_hit_test_position(shaped:RID, coord:float)virtualconst |
| bool | _shaped_text_is_ready(shaped:RID)virtualrequiredconst |
| int | _shaped_text_next_character_pos(shaped:RID, pos:int)virtualconst |
| int | _shaped_text_next_grapheme_pos(shaped:RID, pos:int)virtualconst |
| void | _shaped_text_overrun_trim_to_width(shaped:RID, width:float, trim_flags:BitField[TextOverrunFlag])virtual |
| int | _shaped_text_prev_character_pos(shaped:RID, pos:int)virtualconst |
| int | _shaped_text_prev_grapheme_pos(shaped:RID, pos:int)virtualconst |
| bool | _shaped_text_resize_object(shaped:RID, key:Variant, size:Vector2, inline_align:InlineAlignment, baseline:float)virtualrequired |
| void | _shaped_text_set_bidi_override(shaped:RID, override:Array)virtual |
| void | _shaped_text_set_custom_ellipsis(shaped:RID, char:int)virtual |
| void | _shaped_text_set_custom_punctuation(shaped:RID, punct:String)virtual |
| void | _shaped_text_set_direction(shaped:RID, direction:Direction)virtual |
| void | _shaped_text_set_orientation(shaped:RID, orientation:Orientation)virtual |
| void | _shaped_text_set_preserve_control(shaped:RID, enabled:bool)virtual |
| void | _shaped_text_set_preserve_invalid(shaped:RID, enabled:bool)virtual |
| void | _shaped_text_set_spacing(shaped:RID, spacing:SpacingType, value:int)virtual |
| bool | _shaped_text_shape(shaped:RID)virtualrequired |
| constGlyph* | _shaped_text_sort_logical(shaped:RID)virtualrequired |
| RID | _shaped_text_substr(shaped:RID, start:int, length:int)virtualrequiredconst |
| float | _shaped_text_tab_align(shaped:RID, tab_stops:PackedFloat32Array)virtual |
| bool | _shaped_text_update_breaks(shaped:RID)virtual |
| bool | _shaped_text_update_justification_ops(shaped:RID)virtual |
| bool | _spoof_check(string:String)virtualconst |
| PackedInt32Array | _string_get_character_breaks(string:String, language:String)virtualconst |
| PackedInt32Array | _string_get_word_breaks(string:String, language:String, chars_per_line:int)virtualconst |
| String | _string_to_lower(string:String, language:String)virtualconst |
| String | _string_to_title(string:String, language:String)virtualconst |
| String | _string_to_upper(string:String, language:String)virtualconst |
| String | _strip_diacritics(string:String)virtualconst |
| String | _tag_to_name(tag:int)virtualconst |
| void | _unreference_oversampling_level(oversampling:float)virtual |

void
_cleanup()virtual
_create_font()virtualrequired
_create_font_linked_variation(font_rid:RID)virtual
_create_shaped_text(direction:Direction, orientation:Orientation)virtualrequired
void
_draw_hex_code_box(canvas:RID, size:int, pos:Vector2, index:int, color:Color)virtualconst
void
_font_clear_glyphs(font_rid:RID, size:Vector2i)virtualrequired
void
_font_clear_kerning_map(font_rid:RID, size:int)virtual
void
_font_clear_size_cache(font_rid:RID)virtualrequired
void
_font_clear_system_fallback_cache()virtual
void
_font_clear_textures(font_rid:RID, size:Vector2i)virtualrequired
void
_font_draw_glyph(font_rid:RID, canvas:RID, size:int, pos:Vector2, index:int, color:Color, oversampling:float)virtualrequiredconst
void
_font_draw_glyph_outline(font_rid:RID, canvas:RID, size:int, outline_size:int, pos:Vector2, index:int, color:Color, oversampling:float)virtualrequiredconst
FontAntialiasing
_font_get_antialiasing(font_rid:RID)virtualconst
float
_font_get_ascent(font_rid:RID, size:int)virtualrequiredconst
float
_font_get_baseline_offset(font_rid:RID)virtualconst
_font_get_char_from_glyph_index(font_rid:RID, size:int, glyph_index:int)virtualrequiredconst
float
_font_get_descent(font_rid:RID, size:int)virtualrequiredconst
bool
_font_get_disable_embedded_bitmaps(font_rid:RID)virtualconst
float
_font_get_embolden(font_rid:RID)virtualconst
_font_get_face_count(font_rid:RID)virtualconst
_font_get_face_index(font_rid:RID)virtualconst
_font_get_fixed_size(font_rid:RID)virtualrequiredconst
FixedSizeScaleMode
_font_get_fixed_size_scale_mode(font_rid:RID)virtualrequiredconst
bool
_font_get_generate_mipmaps(font_rid:RID)virtualconst
float
_font_get_global_oversampling()virtualconst
Vector2
_font_get_glyph_advance(font_rid:RID, size:int, glyph:int)virtualrequiredconst
Dictionary
_font_get_glyph_contours(font_rid:RID, size:int, index:int)virtualconst
_font_get_glyph_index(font_rid:RID, size:int, char:int, variation_selector:int)virtualrequiredconst
PackedInt32Array
_font_get_glyph_list(font_rid:RID, size:Vector2i)virtualrequiredconst
Vector2
_font_get_glyph_offset(font_rid:RID, size:Vector2i, glyph:int)virtualrequiredconst
Vector2
_font_get_glyph_size(font_rid:RID, size:Vector2i, glyph:int)virtualrequiredconst
_font_get_glyph_texture_idx(font_rid:RID, size:Vector2i, glyph:int)virtualrequiredconst
_font_get_glyph_texture_rid(font_rid:RID, size:Vector2i, glyph:int)virtualrequiredconst
Vector2
_font_get_glyph_texture_size(font_rid:RID, size:Vector2i, glyph:int)virtualrequiredconst
Rect2
_font_get_glyph_uv_rect(font_rid:RID, size:Vector2i, glyph:int)virtualrequiredconst
Hinting
_font_get_hinting(font_rid:RID)virtualconst
bool
_font_get_keep_rounding_remainders(font_rid:RID)virtualconst
Vector2
_font_get_kerning(font_rid:RID, size:int, glyph_pair:Vector2i)virtualconst
Array[Vector2i]
_font_get_kerning_list(font_rid:RID, size:int)virtualconst
bool
_font_get_language_support_override(font_rid:RID, language:String)virtual
PackedStringArray
_font_get_language_support_overrides(font_rid:RID)virtual
_font_get_msdf_pixel_range(font_rid:RID)virtualconst
_font_get_msdf_size(font_rid:RID)virtualconst
String
_font_get_name(font_rid:RID)virtualconst
Dictionary
_font_get_opentype_feature_overrides(font_rid:RID)virtualconst
Dictionary
_font_get_ot_name_strings(font_rid:RID)virtualconst
float
_font_get_oversampling(font_rid:RID)virtualconst
float
_font_get_scale(font_rid:RID, size:int)virtualrequiredconst
bool
_font_get_script_support_override(font_rid:RID, script:String)virtual
PackedStringArray
_font_get_script_support_overrides(font_rid:RID)virtual
Array[Dictionary]
_font_get_size_cache_info(font_rid:RID)virtualconst
Array[Vector2i]
_font_get_size_cache_list(font_rid:RID)virtualrequiredconst
_font_get_spacing(font_rid:RID, spacing:SpacingType)virtualconst
_font_get_stretch(font_rid:RID)virtualconst
BitField[FontStyle]
_font_get_style(font_rid:RID)virtualconst
String
_font_get_style_name(font_rid:RID)virtualconst
SubpixelPositioning
_font_get_subpixel_positioning(font_rid:RID)virtualconst
String
_font_get_supported_chars(font_rid:RID)virtualrequiredconst
PackedInt32Array
_font_get_supported_glyphs(font_rid:RID)virtualrequiredconst
_font_get_texture_count(font_rid:RID, size:Vector2i)virtualrequiredconst
Image
_font_get_texture_image(font_rid:RID, size:Vector2i, texture_index:int)virtualrequiredconst
PackedInt32Array
_font_get_texture_offsets(font_rid:RID, size:Vector2i, texture_index:int)virtualconst
Transform2D
_font_get_transform(font_rid:RID)virtualconst
float
_font_get_underline_position(font_rid:RID, size:int)virtualrequiredconst
float
_font_get_underline_thickness(font_rid:RID, size:int)virtualrequiredconst
Dictionary
_font_get_variation_coordinates(font_rid:RID)virtualconst
_font_get_weight(font_rid:RID)virtualconst
bool
_font_has_char(font_rid:RID, char:int)virtualrequiredconst
bool
_font_is_allow_system_fallback(font_rid:RID)virtualconst
bool
_font_is_force_autohinter(font_rid:RID)virtualconst
bool
_font_is_language_supported(font_rid:RID, language:String)virtualconst
bool
_font_is_modulate_color_glyphs(font_rid:RID)virtualconst
bool
_font_is_multichannel_signed_distance_field(font_rid:RID)virtualconst
bool
_font_is_script_supported(font_rid:RID, script:String)virtualconst
void
_font_remove_glyph(font_rid:RID, size:Vector2i, glyph:int)virtualrequired
void
_font_remove_kerning(font_rid:RID, size:int, glyph_pair:Vector2i)virtual
void
_font_remove_language_support_override(font_rid:RID, language:String)virtual
void
_font_remove_script_support_override(font_rid:RID, script:String)virtual
void
_font_remove_size_cache(font_rid:RID, size:Vector2i)virtualrequired
void
_font_remove_texture(font_rid:RID, size:Vector2i, texture_index:int)virtualrequired
void
_font_render_glyph(font_rid:RID, size:Vector2i, index:int)virtual
void
_font_render_range(font_rid:RID, size:Vector2i, start:int, end:int)virtual
void
_font_set_allow_system_fallback(font_rid:RID, allow_system_fallback:bool)virtual
void
_font_set_antialiasing(font_rid:RID, antialiasing:FontAntialiasing)virtual
void
_font_set_ascent(font_rid:RID, size:int, ascent:float)virtualrequired
void
_font_set_baseline_offset(font_rid:RID, baseline_offset:float)virtual
void
_font_set_data(font_rid:RID, data:PackedByteArray)virtual
void
_font_set_data_ptr(font_rid:RID, data_ptr:constuint8_t*, data_size:int)virtual
void
_font_set_descent(font_rid:RID, size:int, descent:float)virtualrequired
void
_font_set_disable_embedded_bitmaps(font_rid:RID, disable_embedded_bitmaps:bool)virtual
void
_font_set_embolden(font_rid:RID, strength:float)virtual
void
_font_set_face_index(font_rid:RID, face_index:int)virtual
void
_font_set_fixed_size(font_rid:RID, fixed_size:int)virtualrequired
void
_font_set_fixed_size_scale_mode(font_rid:RID, fixed_size_scale_mode:FixedSizeScaleMode)virtualrequired
void
_font_set_force_autohinter(font_rid:RID, force_autohinter:bool)virtual
void
_font_set_generate_mipmaps(font_rid:RID, generate_mipmaps:bool)virtual
void
_font_set_global_oversampling(oversampling:float)virtual
void
_font_set_glyph_advance(font_rid:RID, size:int, glyph:int, advance:Vector2)virtualrequired
void
_font_set_glyph_offset(font_rid:RID, size:Vector2i, glyph:int, offset:Vector2)virtualrequired
void
_font_set_glyph_size(font_rid:RID, size:Vector2i, glyph:int, gl_size:Vector2)virtualrequired
void
_font_set_glyph_texture_idx(font_rid:RID, size:Vector2i, glyph:int, texture_idx:int)virtualrequired
void
_font_set_glyph_uv_rect(font_rid:RID, size:Vector2i, glyph:int, uv_rect:Rect2)virtualrequired
void
_font_set_hinting(font_rid:RID, hinting:Hinting)virtual
void
_font_set_keep_rounding_remainders(font_rid:RID, keep_rounding_remainders:bool)virtual
void
_font_set_kerning(font_rid:RID, size:int, glyph_pair:Vector2i, kerning:Vector2)virtual
void
_font_set_language_support_override(font_rid:RID, language:String, supported:bool)virtual
void
_font_set_modulate_color_glyphs(font_rid:RID, modulate:bool)virtual
void
_font_set_msdf_pixel_range(font_rid:RID, msdf_pixel_range:int)virtual
void
_font_set_msdf_size(font_rid:RID, msdf_size:int)virtual
void
_font_set_multichannel_signed_distance_field(font_rid:RID, msdf:bool)virtual
void
_font_set_name(font_rid:RID, name:String)virtual
void
_font_set_opentype_feature_overrides(font_rid:RID, overrides:Dictionary)virtual
void
_font_set_oversampling(font_rid:RID, oversampling:float)virtual
void
_font_set_scale(font_rid:RID, size:int, scale:float)virtualrequired
void
_font_set_script_support_override(font_rid:RID, script:String, supported:bool)virtual
void
_font_set_spacing(font_rid:RID, spacing:SpacingType, value:int)virtual
void
_font_set_stretch(font_rid:RID, stretch:int)virtual
void
_font_set_style(font_rid:RID, style:BitField[FontStyle])virtual
void
_font_set_style_name(font_rid:RID, name_style:String)virtual
void
_font_set_subpixel_positioning(font_rid:RID, subpixel_positioning:SubpixelPositioning)virtual
void
_font_set_texture_image(font_rid:RID, size:Vector2i, texture_index:int, image:Image)virtualrequired
void
_font_set_texture_offsets(font_rid:RID, size:Vector2i, texture_index:int, offset:PackedInt32Array)virtual
void
_font_set_transform(font_rid:RID, transform:Transform2D)virtual
void
_font_set_underline_position(font_rid:RID, size:int, underline_position:float)virtualrequired
void
_font_set_underline_thickness(font_rid:RID, size:int, underline_thickness:float)virtualrequired
void
_font_set_variation_coordinates(font_rid:RID, variation_coordinates:Dictionary)virtual
void
_font_set_weight(font_rid:RID, weight:int)virtual
Dictionary
_font_supported_feature_list(font_rid:RID)virtualconst
Dictionary
_font_supported_variation_list(font_rid:RID)virtualconst
String
_format_number(number:String, language:String)virtualconst
void
_free_rid(rid:RID)virtualrequired
_get_features()virtualrequiredconst
Vector2
_get_hex_code_box_size(size:int, index:int)virtualconst
String
_get_name()virtualrequiredconst
PackedByteArray
_get_support_data()virtualconst
String
_get_support_data_filename()virtualconst
String
_get_support_data_info()virtualconst
bool
_has(rid:RID)virtualrequired
bool
_has_feature(feature:Feature)virtualrequiredconst
_is_confusable(string:String, dict:PackedStringArray)virtualconst
bool
_is_locale_right_to_left(locale:String)virtualconst
bool
_is_locale_using_support_data(locale:String)virtualconst
bool
_is_valid_identifier(string:String)virtualconst
bool
_is_valid_letter(unicode:int)virtualconst
bool
_load_support_data(filename:String)virtual
_name_to_tag(name:String)virtualconst
String
_parse_number(number:String, language:String)virtualconst
Array[Vector3i]
_parse_structured_text(parser_type:StructuredTextParser, args:Array, text:String)virtualconst
String
_percent_sign(language:String)virtualconst
void
_reference_oversampling_level(oversampling:float)virtual
bool
_save_support_data(filename:String)virtualconst
_shaped_get_run_count(shaped:RID)virtualconst
Direction
_shaped_get_run_direction(shaped:RID, index:int)virtualconst
_shaped_get_run_font_rid(shaped:RID, index:int)virtualconst
_shaped_get_run_font_size(shaped:RID, index:int)virtualconst
String
_shaped_get_run_language(shaped:RID, index:int)virtualconst
Variant
_shaped_get_run_object(shaped:RID, index:int)virtualconst
Vector2i
_shaped_get_run_range(shaped:RID, index:int)virtualconst
String
_shaped_get_run_text(shaped:RID, index:int)virtualconst
_shaped_get_span_count(shaped:RID)virtualrequiredconst
Variant
_shaped_get_span_embedded_object(shaped:RID, index:int)virtualrequiredconst
Variant
_shaped_get_span_meta(shaped:RID, index:int)virtualrequiredconst
Variant
_shaped_get_span_object(shaped:RID, index:int)virtualrequiredconst
String
_shaped_get_span_text(shaped:RID, index:int)virtualrequiredconst
String
_shaped_get_text(shaped:RID)virtualrequiredconst
void
_shaped_set_span_update_font(shaped:RID, index:int, fonts:Array[RID], size:int, opentype_features:Dictionary)virtualrequired
bool
_shaped_text_add_object(shaped:RID, key:Variant, size:Vector2, inline_align:InlineAlignment, length:int, baseline:float)virtualrequired
bool
_shaped_text_add_string(shaped:RID, text:String, fonts:Array[RID], size:int, opentype_features:Dictionary, language:String, meta:Variant)virtualrequired
void
_shaped_text_clear(shaped:RID)virtualrequired
_shaped_text_closest_character_pos(shaped:RID, pos:int)virtualconst
void
_shaped_text_draw(shaped:RID, canvas:RID, pos:Vector2, clip_l:float, clip_r:float, color:Color, oversampling:float)virtualconst
void
_shaped_text_draw_outline(shaped:RID, canvas:RID, pos:Vector2, clip_l:float, clip_r:float, outline_size:int, color:Color, oversampling:float)virtualconst
_shaped_text_duplicate(shaped:RID)virtualrequired
float
_shaped_text_fit_to_width(shaped:RID, width:float, justification_flags:BitField[JustificationFlag])virtual
float
_shaped_text_get_ascent(shaped:RID)virtualrequiredconst
void
_shaped_text_get_carets(shaped:RID, position:int, caret:CaretInfo*)virtualconst
PackedInt32Array
_shaped_text_get_character_breaks(shaped:RID)virtualconst
_shaped_text_get_custom_ellipsis(shaped:RID)virtualconst
String
_shaped_text_get_custom_punctuation(shaped:RID)virtualconst
float
_shaped_text_get_descent(shaped:RID)virtualrequiredconst
Direction
_shaped_text_get_direction(shaped:RID)virtualconst
_shaped_text_get_dominant_direction_in_range(shaped:RID, start:int, end:int)virtualconst
_shaped_text_get_ellipsis_glyph_count(shaped:RID)virtualrequiredconst
constGlyph*
_shaped_text_get_ellipsis_glyphs(shaped:RID)virtualrequiredconst
_shaped_text_get_ellipsis_pos(shaped:RID)virtualrequiredconst
_shaped_text_get_glyph_count(shaped:RID)virtualrequiredconst
constGlyph*
_shaped_text_get_glyphs(shaped:RID)virtualrequiredconst
Vector2
_shaped_text_get_grapheme_bounds(shaped:RID, pos:int)virtualconst
Direction
_shaped_text_get_inferred_direction(shaped:RID)virtualconst
PackedInt32Array
_shaped_text_get_line_breaks(shaped:RID, width:float, start:int, break_flags:BitField[LineBreakFlag])virtualconst
PackedInt32Array
_shaped_text_get_line_breaks_adv(shaped:RID, width:PackedFloat32Array, start:int, once:bool, break_flags:BitField[LineBreakFlag])virtualconst
_shaped_text_get_object_glyph(shaped:RID, key:Variant)virtualrequiredconst
Vector2i
_shaped_text_get_object_range(shaped:RID, key:Variant)virtualrequiredconst
Rect2
_shaped_text_get_object_rect(shaped:RID, key:Variant)virtualrequiredconst
Array
_shaped_text_get_objects(shaped:RID)virtualrequiredconst
Orientation
_shaped_text_get_orientation(shaped:RID)virtualconst
_shaped_text_get_parent(shaped:RID)virtualrequiredconst
bool
_shaped_text_get_preserve_control(shaped:RID)virtualconst
bool
_shaped_text_get_preserve_invalid(shaped:RID)virtualconst
Vector2i
_shaped_text_get_range(shaped:RID)virtualrequiredconst
PackedVector2Array
_shaped_text_get_selection(shaped:RID, start:int, end:int)virtualconst
Vector2
_shaped_text_get_size(shaped:RID)virtualrequiredconst
_shaped_text_get_spacing(shaped:RID, spacing:SpacingType)virtualconst
_shaped_text_get_trim_pos(shaped:RID)virtualrequiredconst
float
_shaped_text_get_underline_position(shaped:RID)virtualrequiredconst
float
_shaped_text_get_underline_thickness(shaped:RID)virtualrequiredconst
float
_shaped_text_get_width(shaped:RID)virtualrequiredconst
PackedInt32Array
_shaped_text_get_word_breaks(shaped:RID, grapheme_flags:BitField[GraphemeFlag], skip_grapheme_flags:BitField[GraphemeFlag])virtualconst
bool
_shaped_text_has_object(shaped:RID, key:Variant)virtualrequiredconst
_shaped_text_hit_test_grapheme(shaped:RID, coord:float)virtualconst
_shaped_text_hit_test_position(shaped:RID, coord:float)virtualconst
bool
_shaped_text_is_ready(shaped:RID)virtualrequiredconst
_shaped_text_next_character_pos(shaped:RID, pos:int)virtualconst
_shaped_text_next_grapheme_pos(shaped:RID, pos:int)virtualconst
void
_shaped_text_overrun_trim_to_width(shaped:RID, width:float, trim_flags:BitField[TextOverrunFlag])virtual
_shaped_text_prev_character_pos(shaped:RID, pos:int)virtualconst
_shaped_text_prev_grapheme_pos(shaped:RID, pos:int)virtualconst
bool
_shaped_text_resize_object(shaped:RID, key:Variant, size:Vector2, inline_align:InlineAlignment, baseline:float)virtualrequired
void
_shaped_text_set_bidi_override(shaped:RID, override:Array)virtual
void
_shaped_text_set_custom_ellipsis(shaped:RID, char:int)virtual
void
_shaped_text_set_custom_punctuation(shaped:RID, punct:String)virtual
void
_shaped_text_set_direction(shaped:RID, direction:Direction)virtual
void
_shaped_text_set_orientation(shaped:RID, orientation:Orientation)virtual
void
_shaped_text_set_preserve_control(shaped:RID, enabled:bool)virtual
void
_shaped_text_set_preserve_invalid(shaped:RID, enabled:bool)virtual
void
_shaped_text_set_spacing(shaped:RID, spacing:SpacingType, value:int)virtual
bool
_shaped_text_shape(shaped:RID)virtualrequired
constGlyph*
_shaped_text_sort_logical(shaped:RID)virtualrequired
_shaped_text_substr(shaped:RID, start:int, length:int)virtualrequiredconst
float
_shaped_text_tab_align(shaped:RID, tab_stops:PackedFloat32Array)virtual
bool
_shaped_text_update_breaks(shaped:RID)virtual
bool
_shaped_text_update_justification_ops(shaped:RID)virtual
bool
_spoof_check(string:String)virtualconst
PackedInt32Array
_string_get_character_breaks(string:String, language:String)virtualconst
PackedInt32Array
_string_get_word_breaks(string:String, language:String, chars_per_line:int)virtualconst
String
_string_to_lower(string:String, language:String)virtualconst
String
_string_to_title(string:String, language:String)virtualconst
String
_string_to_upper(string:String, language:String)virtualconst
String
_strip_diacritics(string:String)virtualconst
String
_tag_to_name(tag:int)virtualconst
void
_unreference_oversampling_level(oversampling:float)virtual

## Method Descriptions

void_cleanup()virtual🔗
This method is called before text server is unregistered.
RID_create_font()virtualrequired🔗
Creates a new, empty font cache entry resource.
RID_create_font_linked_variation(font_rid:RID)virtual🔗
Optional, implement if font supports extra spacing or baseline offset.
Creates a new variation existing font which is reusing the same glyph cache and font data.
RID_create_shaped_text(direction:Direction, orientation:Orientation)virtualrequired🔗
Creates a new buffer for complex text layout, with the givendirectionandorientation.
void_draw_hex_code_box(canvas:RID, size:int, pos:Vector2, index:int, color:Color)virtualconst🔗
Draws box displaying character hexadecimal code.
void_font_clear_glyphs(font_rid:RID, size:Vector2i)virtualrequired🔗
Removes all rendered glyph information from the cache entry.
void_font_clear_kerning_map(font_rid:RID, size:int)virtual🔗
Removes all kerning overrides.
void_font_clear_size_cache(font_rid:RID)virtualrequired🔗
Removes all font sizes from the cache entry.
void_font_clear_system_fallback_cache()virtual🔗
Frees all automatically loaded system fonts.
void_font_clear_textures(font_rid:RID, size:Vector2i)virtualrequired🔗
Removes all textures from font cache entry.
void_font_draw_glyph(font_rid:RID, canvas:RID, size:int, pos:Vector2, index:int, color:Color, oversampling:float)virtualrequiredconst🔗
Draws single glyph into a canvas item at the position, usingfont_ridat the sizesize. Ifoversamplingis greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.
void_font_draw_glyph_outline(font_rid:RID, canvas:RID, size:int, outline_size:int, pos:Vector2, index:int, color:Color, oversampling:float)virtualrequiredconst🔗
Draws single glyph outline of sizeoutline_sizeinto a canvas item at the position, usingfont_ridat the sizesize. Ifoversamplingis greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.
FontAntialiasing_font_get_antialiasing(font_rid:RID)virtualconst🔗
Returns font anti-aliasing mode.
float_font_get_ascent(font_rid:RID, size:int)virtualrequiredconst🔗
Returns the font ascent (number of pixels above the baseline).
float_font_get_baseline_offset(font_rid:RID)virtualconst🔗
Returns extra baseline offset (as a fraction of font height).
int_font_get_char_from_glyph_index(font_rid:RID, size:int, glyph_index:int)virtualrequiredconst🔗
Returns character code associated withglyph_index, or0ifglyph_indexis invalid.
float_font_get_descent(font_rid:RID, size:int)virtualrequiredconst🔗
Returns the font descent (number of pixels below the baseline).
bool_font_get_disable_embedded_bitmaps(font_rid:RID)virtualconst🔗
Returns whether the font's embedded bitmap loading is disabled.
float_font_get_embolden(font_rid:RID)virtualconst🔗
Returns font embolden strength.
int_font_get_face_count(font_rid:RID)virtualconst🔗
Returns number of faces in the TrueType / OpenType collection.
int_font_get_face_index(font_rid:RID)virtualconst🔗
Returns an active face index in the TrueType / OpenType collection.
int_font_get_fixed_size(font_rid:RID)virtualrequiredconst🔗
Returns bitmap font fixed size.
FixedSizeScaleMode_font_get_fixed_size_scale_mode(font_rid:RID)virtualrequiredconst🔗
Returns bitmap font scaling mode.
bool_font_get_generate_mipmaps(font_rid:RID)virtualconst🔗
Returnstrueif font texture mipmap generation is enabled.
float_font_get_global_oversampling()virtualconst🔗
Returns the font oversampling factor, shared by all fonts in the TextServer.
Vector2_font_get_glyph_advance(font_rid:RID, size:int, glyph:int)virtualrequiredconst🔗
Returns glyph advance (offset of the next glyph).
Dictionary_font_get_glyph_contours(font_rid:RID, size:int, index:int)virtualconst🔗
Returns outline contours of the glyph.
int_font_get_glyph_index(font_rid:RID, size:int, char:int, variation_selector:int)virtualrequiredconst🔗
Returns the glyph index of achar, optionally modified by thevariation_selector.
PackedInt32Array_font_get_glyph_list(font_rid:RID, size:Vector2i)virtualrequiredconst🔗
Returns list of rendered glyphs in the cache entry.
Vector2_font_get_glyph_offset(font_rid:RID, size:Vector2i, glyph:int)virtualrequiredconst🔗
Returns glyph offset from the baseline.
Vector2_font_get_glyph_size(font_rid:RID, size:Vector2i, glyph:int)virtualrequiredconst🔗
Returns size of the glyph.
int_font_get_glyph_texture_idx(font_rid:RID, size:Vector2i, glyph:int)virtualrequiredconst🔗
Returns index of the cache texture containing the glyph.
RID_font_get_glyph_texture_rid(font_rid:RID, size:Vector2i, glyph:int)virtualrequiredconst🔗
Returns resource ID of the cache texture containing the glyph.
Vector2_font_get_glyph_texture_size(font_rid:RID, size:Vector2i, glyph:int)virtualrequiredconst🔗
Returns size of the cache texture containing the glyph.
Rect2_font_get_glyph_uv_rect(font_rid:RID, size:Vector2i, glyph:int)virtualrequiredconst🔗
Returns rectangle in the cache texture containing the glyph.
Hinting_font_get_hinting(font_rid:RID)virtualconst🔗
Returns the font hinting mode. Used by dynamic fonts only.
bool_font_get_keep_rounding_remainders(font_rid:RID)virtualconst🔗
Returns glyph position rounding behavior. If set totrue, when aligning glyphs to the pixel boundaries rounding remainders are accumulated to ensure more uniform glyph distribution. This setting has no effect if subpixel positioning is enabled.
Vector2_font_get_kerning(font_rid:RID, size:int, glyph_pair:Vector2i)virtualconst🔗
Returns kerning for the pair of glyphs.
Array[Vector2i]_font_get_kerning_list(font_rid:RID, size:int)virtualconst🔗
Returns list of the kerning overrides.
bool_font_get_language_support_override(font_rid:RID, language:String)virtual🔗
Returnstrueif support override is enabled for thelanguage.
PackedStringArray_font_get_language_support_overrides(font_rid:RID)virtual🔗
Returns list of language support overrides.
int_font_get_msdf_pixel_range(font_rid:RID)virtualconst🔗
Returns the width of the range around the shape between the minimum and maximum representable signed distance.
int_font_get_msdf_size(font_rid:RID)virtualconst🔗
Returns source font size used to generate MSDF textures.
String_font_get_name(font_rid:RID)virtualconst🔗
Returns font family name.
Dictionary_font_get_opentype_feature_overrides(font_rid:RID)virtualconst🔗
Returns font OpenType feature set override.
Dictionary_font_get_ot_name_strings(font_rid:RID)virtualconst🔗
ReturnsDictionarywith OpenType font name strings (localized font names, version, description, license information, sample text, etc.).
float_font_get_oversampling(font_rid:RID)virtualconst🔗
Returns oversampling factor override. If set to a positive value, overrides the oversampling factor of the viewport this font is used in. SeeViewport.oversampling. This value doesn't override theoversamplingparameter ofdraw_*methods. Used by dynamic fonts only.
float_font_get_scale(font_rid:RID, size:int)virtualrequiredconst🔗
Returns scaling factor of the color bitmap font.
bool_font_get_script_support_override(font_rid:RID, script:String)virtual🔗
Returnstrueif support override is enabled for thescript.
PackedStringArray_font_get_script_support_overrides(font_rid:RID)virtual🔗
Returns list of script support overrides.
Array[Dictionary]_font_get_size_cache_info(font_rid:RID)virtualconst🔗
Returns font cache information, each entry contains the following fields:Vector2isize_px- font size in pixels,floatviewport_oversampling- viewport oversampling factor,intglyphs- number of rendered glyphs,inttextures- number of used textures,inttextures_size- size of texture data in bytes.
Array[Vector2i]_font_get_size_cache_list(font_rid:RID)virtualrequiredconst🔗
Returns list of the font sizes in the cache. Each size isVector2iwith font size and outline size.
int_font_get_spacing(font_rid:RID, spacing:SpacingType)virtualconst🔗
Returns the spacing forspacingin pixels (not relative to the font size).
int_font_get_stretch(font_rid:RID)virtualconst🔗
Returns font stretch amount, compared to a normal width. A percentage value between50%and200%.
BitField[FontStyle]_font_get_style(font_rid:RID)virtualconst🔗
Returns font style flags.
String_font_get_style_name(font_rid:RID)virtualconst🔗
Returns font style name.
SubpixelPositioning_font_get_subpixel_positioning(font_rid:RID)virtualconst🔗
Returns font subpixel glyph positioning mode.
String_font_get_supported_chars(font_rid:RID)virtualrequiredconst🔗
Returns a string containing all the characters available in the font.
PackedInt32Array_font_get_supported_glyphs(font_rid:RID)virtualrequiredconst🔗
Returns an array containing all glyph indices in the font.
int_font_get_texture_count(font_rid:RID, size:Vector2i)virtualrequiredconst🔗
Returns number of textures used by font cache entry.
Image_font_get_texture_image(font_rid:RID, size:Vector2i, texture_index:int)virtualrequiredconst🔗
Returns font cache texture image data.
PackedInt32Array_font_get_texture_offsets(font_rid:RID, size:Vector2i, texture_index:int)virtualconst🔗
Returns array containing glyph packing data.
Transform2D_font_get_transform(font_rid:RID)virtualconst🔗
Returns 2D transform applied to the font outlines.
float_font_get_underline_position(font_rid:RID, size:int)virtualrequiredconst🔗
Returns pixel offset of the underline below the baseline.
float_font_get_underline_thickness(font_rid:RID, size:int)virtualrequiredconst🔗
Returns thickness of the underline in pixels.
Dictionary_font_get_variation_coordinates(font_rid:RID)virtualconst🔗
Returns variation coordinates for the specified font cache entry.
int_font_get_weight(font_rid:RID)virtualconst🔗
Returns weight (boldness) of the font. A value in the100...999range, normal font weight is400, bold font weight is700.
bool_font_has_char(font_rid:RID, char:int)virtualrequiredconst🔗
Returnstrueif a Unicodecharis available in the font.
bool_font_is_allow_system_fallback(font_rid:RID)virtualconst🔗
Returnstrueif system fonts can be automatically used as fallbacks.
bool_font_is_force_autohinter(font_rid:RID)virtualconst🔗
Returnstrueif auto-hinting is supported and preferred over font built-in hinting.
bool_font_is_language_supported(font_rid:RID, language:String)virtualconst🔗
Returnstrueif the font supports the given language (as aISO 639code).
bool_font_is_modulate_color_glyphs(font_rid:RID)virtualconst🔗
Returnstrueif color modulation is applied when drawing the font's colored glyphs.
bool_font_is_multichannel_signed_distance_field(font_rid:RID)virtualconst🔗
Returnstrueif glyphs of all sizes are rendered using single multichannel signed distance field generated from the dynamic font vector data.
bool_font_is_script_supported(font_rid:RID, script:String)virtualconst🔗
Returnstrueif the font supports the given script (as aISO 15924code).
void_font_remove_glyph(font_rid:RID, size:Vector2i, glyph:int)virtualrequired🔗
Removes specified rendered glyph information from the cache entry.
void_font_remove_kerning(font_rid:RID, size:int, glyph_pair:Vector2i)virtual🔗
Removes kerning override for the pair of glyphs.
void_font_remove_language_support_override(font_rid:RID, language:String)virtual🔗
Remove language support override.
void_font_remove_script_support_override(font_rid:RID, script:String)virtual🔗
Removes script support override.
void_font_remove_size_cache(font_rid:RID, size:Vector2i)virtualrequired🔗
Removes specified font size from the cache entry.
void_font_remove_texture(font_rid:RID, size:Vector2i, texture_index:int)virtualrequired🔗
Removes specified texture from the cache entry.
void_font_render_glyph(font_rid:RID, size:Vector2i, index:int)virtual🔗
Renders specified glyph to the font cache texture.
void_font_render_range(font_rid:RID, size:Vector2i, start:int, end:int)virtual🔗
Renders the range of characters to the font cache texture.
void_font_set_allow_system_fallback(font_rid:RID, allow_system_fallback:bool)virtual🔗
If set totrue, system fonts can be automatically used as fallbacks.
void_font_set_antialiasing(font_rid:RID, antialiasing:FontAntialiasing)virtual🔗
Sets font anti-aliasing mode.
void_font_set_ascent(font_rid:RID, size:int, ascent:float)virtualrequired🔗
Sets the font ascent (number of pixels above the baseline).
void_font_set_baseline_offset(font_rid:RID, baseline_offset:float)virtual🔗
Sets extra baseline offset (as a fraction of font height).
void_font_set_data(font_rid:RID, data:PackedByteArray)virtual🔗
Sets font source data, e.g contents of the dynamic font source file.
void_font_set_data_ptr(font_rid:RID, data_ptr:constuint8_t*, data_size:int)virtual🔗
Sets pointer to the font source data, e.g contents of the dynamic font source file.
void_font_set_descent(font_rid:RID, size:int, descent:float)virtualrequired🔗
Sets the font descent (number of pixels below the baseline).
void_font_set_disable_embedded_bitmaps(font_rid:RID, disable_embedded_bitmaps:bool)virtual🔗
If set totrue, embedded font bitmap loading is disabled.
void_font_set_embolden(font_rid:RID, strength:float)virtual🔗
Sets font embolden strength. Ifstrengthis not equal to zero, emboldens the font outlines. Negative values reduce the outline thickness.
void_font_set_face_index(font_rid:RID, face_index:int)virtual🔗
Sets an active face index in the TrueType / OpenType collection.
void_font_set_fixed_size(font_rid:RID, fixed_size:int)virtualrequired🔗
Sets bitmap font fixed size. If set to value greater than zero, same cache entry will be used for all font sizes.
void_font_set_fixed_size_scale_mode(font_rid:RID, fixed_size_scale_mode:FixedSizeScaleMode)virtualrequired🔗
Sets bitmap font scaling mode. This property is used only iffixed_sizeis greater than zero.
void_font_set_force_autohinter(font_rid:RID, force_autohinter:bool)virtual🔗
If set totrueauto-hinting is preferred over font built-in hinting.
void_font_set_generate_mipmaps(font_rid:RID, generate_mipmaps:bool)virtual🔗
If set totruefont texture mipmap generation is enabled.
void_font_set_global_oversampling(oversampling:float)virtual🔗
Sets oversampling factor, shared by all font in the TextServer.
void_font_set_glyph_advance(font_rid:RID, size:int, glyph:int, advance:Vector2)virtualrequired🔗
Sets glyph advance (offset of the next glyph).
void_font_set_glyph_offset(font_rid:RID, size:Vector2i, glyph:int, offset:Vector2)virtualrequired🔗
Sets glyph offset from the baseline.
void_font_set_glyph_size(font_rid:RID, size:Vector2i, glyph:int, gl_size:Vector2)virtualrequired🔗
Sets size of the glyph.
void_font_set_glyph_texture_idx(font_rid:RID, size:Vector2i, glyph:int, texture_idx:int)virtualrequired🔗
Sets index of the cache texture containing the glyph.
void_font_set_glyph_uv_rect(font_rid:RID, size:Vector2i, glyph:int, uv_rect:Rect2)virtualrequired🔗
Sets rectangle in the cache texture containing the glyph.
void_font_set_hinting(font_rid:RID, hinting:Hinting)virtual🔗
Sets font hinting mode. Used by dynamic fonts only.
void_font_set_keep_rounding_remainders(font_rid:RID, keep_rounding_remainders:bool)virtual🔗
Sets glyph position rounding behavior. If set totrue, when aligning glyphs to the pixel boundaries rounding remainders are accumulated to ensure more uniform glyph distribution. This setting has no effect if subpixel positioning is enabled.
void_font_set_kerning(font_rid:RID, size:int, glyph_pair:Vector2i, kerning:Vector2)virtual🔗
Sets kerning for the pair of glyphs.
void_font_set_language_support_override(font_rid:RID, language:String, supported:bool)virtual🔗
Adds override for_font_is_language_supported().
void_font_set_modulate_color_glyphs(font_rid:RID, modulate:bool)virtual🔗
If set totrue, color modulation is applied when drawing colored glyphs, otherwise it's applied to the monochrome glyphs only.
void_font_set_msdf_pixel_range(font_rid:RID, msdf_pixel_range:int)virtual🔗
Sets the width of the range around the shape between the minimum and maximum representable signed distance.
void_font_set_msdf_size(font_rid:RID, msdf_size:int)virtual🔗
Sets source font size used to generate MSDF textures.
void_font_set_multichannel_signed_distance_field(font_rid:RID, msdf:bool)virtual🔗
If set totrue, glyphs of all sizes are rendered using single multichannel signed distance field generated from the dynamic font vector data. MSDF rendering allows displaying the font at any scaling factor without blurriness, and without incurring a CPU cost when the font size changes (since the font no longer needs to be rasterized on the CPU). As a downside, font hinting is not available with MSDF. The lack of font hinting may result in less crisp and less readable fonts at small sizes.
void_font_set_name(font_rid:RID, name:String)virtual🔗
Sets the font family name.
void_font_set_opentype_feature_overrides(font_rid:RID, overrides:Dictionary)virtual🔗
Sets font OpenType feature set override.
void_font_set_oversampling(font_rid:RID, oversampling:float)virtual🔗
If set to a positive value, overrides the oversampling factor of the viewport this font is used in. SeeViewport.oversampling. This value doesn't override theoversamplingparameter ofdraw_*methods. Used by dynamic fonts only.
void_font_set_scale(font_rid:RID, size:int, scale:float)virtualrequired🔗
Sets scaling factor of the color bitmap font.
void_font_set_script_support_override(font_rid:RID, script:String, supported:bool)virtual🔗
Adds override for_font_is_script_supported().
void_font_set_spacing(font_rid:RID, spacing:SpacingType, value:int)virtual🔗
Sets the spacing forspacingtovaluein pixels (not relative to the font size).
void_font_set_stretch(font_rid:RID, stretch:int)virtual🔗
Sets font stretch amount, compared to a normal width. A percentage value between50%and200%.
void_font_set_style(font_rid:RID, style:BitField[FontStyle])virtual🔗
Sets the font style flags.
void_font_set_style_name(font_rid:RID, name_style:String)virtual🔗
Sets the font style name.
void_font_set_subpixel_positioning(font_rid:RID, subpixel_positioning:SubpixelPositioning)virtual🔗
Sets font subpixel glyph positioning mode.
void_font_set_texture_image(font_rid:RID, size:Vector2i, texture_index:int, image:Image)virtualrequired🔗
Sets font cache texture image data.
void_font_set_texture_offsets(font_rid:RID, size:Vector2i, texture_index:int, offset:PackedInt32Array)virtual🔗
Sets array containing glyph packing data.
void_font_set_transform(font_rid:RID, transform:Transform2D)virtual🔗
Sets 2D transform, applied to the font outlines, can be used for slanting, flipping, and rotating glyphs.
void_font_set_underline_position(font_rid:RID, size:int, underline_position:float)virtualrequired🔗
Sets pixel offset of the underline below the baseline.
void_font_set_underline_thickness(font_rid:RID, size:int, underline_thickness:float)virtualrequired🔗
Sets thickness of the underline in pixels.
void_font_set_variation_coordinates(font_rid:RID, variation_coordinates:Dictionary)virtual🔗
Sets variation coordinates for the specified font cache entry.
void_font_set_weight(font_rid:RID, weight:int)virtual🔗
Sets weight (boldness) of the font. A value in the100...999range, normal font weight is400, bold font weight is700.
Dictionary_font_supported_feature_list(font_rid:RID)virtualconst🔗
Returns the dictionary of the supported OpenType features.
Dictionary_font_supported_variation_list(font_rid:RID)virtualconst🔗
Returns the dictionary of the supported OpenType variation coordinates.
String_format_number(number:String, language:String)virtualconst🔗
Deprecated:UseTranslationServer.format_number()instead.
Converts a number from Western Arabic (0..9) to the numeral system used in the givenlanguage.
Iflanguageis an empty string, the active locale will be used.
void_free_rid(rid:RID)virtualrequired🔗
Frees an object created by thisTextServer.
int_get_features()virtualrequiredconst🔗
Returns text server features, seeFeature.
Vector2_get_hex_code_box_size(size:int, index:int)virtualconst🔗
Returns size of the replacement character (box with character hexadecimal code that is drawn in place of invalid characters).
String_get_name()virtualrequiredconst🔗
Returns the name of the server interface.
PackedByteArray_get_support_data()virtualconst🔗
Returns default TextServer database (e.g. ICU break iterators and dictionaries).
String_get_support_data_filename()virtualconst🔗
Returns default TextServer database (e.g. ICU break iterators and dictionaries) filename.
String_get_support_data_info()virtualconst🔗
Returns TextServer database (e.g. ICU break iterators and dictionaries) description.
bool_has(rid:RID)virtualrequired🔗
Returnstrueifridis valid resource owned by this text server.
bool_has_feature(feature:Feature)virtualrequiredconst🔗
Returnstrueif the server supports a feature.
int_is_confusable(string:String, dict:PackedStringArray)virtualconst🔗
Returns index of the first string indictwhich is visually confusable with thestring, or-1if none is found.
bool_is_locale_right_to_left(locale:String)virtualconst🔗
Returnstrueif locale is right-to-left.
bool_is_locale_using_support_data(locale:String)virtualconst🔗
Returnstrueif the locale requires text server support data for line/word breaking.
bool_is_valid_identifier(string:String)virtualconst🔗
Returnstrueifstringis a valid identifier.
bool_is_valid_letter(unicode:int)virtualconst🔗
There is currently no description for this method. Please help us bycontributing one!
bool_load_support_data(filename:String)virtual🔗
Loads optional TextServer database (e.g. ICU break iterators and dictionaries).
int_name_to_tag(name:String)virtualconst🔗
Converts the given readable name of a feature, variation, script, or language to an OpenType tag.
String_parse_number(number:String, language:String)virtualconst🔗
Deprecated:UseTranslationServer.parse_number()instead.
Convertsnumberfrom the numeral system used in the givenlanguageto Western Arabic (0..9).
Iflanguageis an empty string, the active locale will be used.
Array[Vector3i]_parse_structured_text(parser_type:StructuredTextParser, args:Array, text:String)virtualconst🔗
Default implementation of the BiDi algorithm override function.
String_percent_sign(language:String)virtualconst🔗
Deprecated:UseTranslationServer.get_percent_sign()instead.
Returns percent sign used in the givenlanguage.
void_reference_oversampling_level(oversampling:float)virtual🔗
Increases the reference count of the specified oversampling level. This method is called byViewport, and should not be used directly.
bool_save_support_data(filename:String)virtualconst🔗
Saves optional TextServer database (e.g. ICU break iterators and dictionaries) to the file.
int_shaped_get_run_count(shaped:RID)virtualconst🔗
Returns the number of uniform text runs in the buffer.
Direction_shaped_get_run_direction(shaped:RID, index:int)virtualconst🔗
Returns the direction of theindextext run (in visual order).
RID_shaped_get_run_font_rid(shaped:RID, index:int)virtualconst🔗
Returns the font RID of theindextext run (in visual order).
int_shaped_get_run_font_size(shaped:RID, index:int)virtualconst🔗
Returns the font size of theindextext run (in visual order).
String_shaped_get_run_language(shaped:RID, index:int)virtualconst🔗
Returns the language of theindextext run (in visual order).
Variant_shaped_get_run_object(shaped:RID, index:int)virtualconst🔗
Returns the embedded object of theindextext run (in visual order).
Vector2i_shaped_get_run_range(shaped:RID, index:int)virtualconst🔗
Returns the source text range of theindextext run (in visual order).
String_shaped_get_run_text(shaped:RID, index:int)virtualconst🔗
Returns the source text of theindextext run (in visual order).
int_shaped_get_span_count(shaped:RID)virtualrequiredconst🔗
Returns number of text spans added using_shaped_text_add_string()or_shaped_text_add_object().
Variant_shaped_get_span_embedded_object(shaped:RID, index:int)virtualrequiredconst🔗
Returns text embedded object key.
Variant_shaped_get_span_meta(shaped:RID, index:int)virtualrequiredconst🔗
Returns text span metadata.
Variant_shaped_get_span_object(shaped:RID, index:int)virtualrequiredconst🔗
Returns the text span embedded object key.
String_shaped_get_span_text(shaped:RID, index:int)virtualrequiredconst🔗
Returns the text span source text.
String_shaped_get_text(shaped:RID)virtualrequiredconst🔗
Returns the text buffer source text, including object replacement characters.
void_shaped_set_span_update_font(shaped:RID, index:int, fonts:Array[RID], size:int, opentype_features:Dictionary)virtualrequired🔗
Changes text span font, font size, and OpenType features, without changing the text.
bool_shaped_text_add_object(shaped:RID, key:Variant, size:Vector2, inline_align:InlineAlignment, length:int, baseline:float)virtualrequired🔗
Adds inline object to the text buffer,keymust be unique. In the text, object is represented aslengthobject replacement characters.
bool_shaped_text_add_string(shaped:RID, text:String, fonts:Array[RID], size:int, opentype_features:Dictionary, language:String, meta:Variant)virtualrequired🔗
Adds text span and font to draw it to the text buffer.
void_shaped_text_clear(shaped:RID)virtualrequired🔗
Clears text buffer (removes text and inline objects).
int_shaped_text_closest_character_pos(shaped:RID, pos:int)virtualconst🔗
Returns composite character position closest to thepos.
void_shaped_text_draw(shaped:RID, canvas:RID, pos:Vector2, clip_l:float, clip_r:float, color:Color, oversampling:float)virtualconst🔗
Draw shaped text into a canvas item at a given position, withcolor.posspecifies the leftmost point of the baseline (for horizontal layout) or topmost point of the baseline (for vertical layout). Ifoversamplingis greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.
void_shaped_text_draw_outline(shaped:RID, canvas:RID, pos:Vector2, clip_l:float, clip_r:float, outline_size:int, color:Color, oversampling:float)virtualconst🔗
Draw the outline of the shaped text into a canvas item at a given position, withcolor.posspecifies the leftmost point of the baseline (for horizontal layout) or topmost point of the baseline (for vertical layout). Ifoversamplingis greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.
RID_shaped_text_duplicate(shaped:RID)virtualrequired🔗
Duplicates shaped text buffer.
float_shaped_text_fit_to_width(shaped:RID, width:float, justification_flags:BitField[JustificationFlag])virtual🔗
Adjusts text width to fit to specified width, returns new text width.
float_shaped_text_get_ascent(shaped:RID)virtualrequiredconst🔗
Returns the text ascent (number of pixels above the baseline for horizontal layout or to the left of baseline for vertical).
void_shaped_text_get_carets(shaped:RID, position:int, caret:CaretInfo*)virtualconst🔗
Returns shapes of the carets corresponding to the character offsetpositionin the text. Returned caret shape is 1 pixel wide rectangle.
PackedInt32Array_shaped_text_get_character_breaks(shaped:RID)virtualconst🔗
Returns array of the composite character boundaries.
int_shaped_text_get_custom_ellipsis(shaped:RID)virtualconst🔗
Returns ellipsis character used for text clipping.
String_shaped_text_get_custom_punctuation(shaped:RID)virtualconst🔗
Returns custom punctuation character list, used for word breaking. If set to empty string, server defaults are used.
float_shaped_text_get_descent(shaped:RID)virtualrequiredconst🔗
Returns the text descent (number of pixels below the baseline for horizontal layout or to the right of baseline for vertical).
Direction_shaped_text_get_direction(shaped:RID)virtualconst🔗
Returns direction of the text.
int_shaped_text_get_dominant_direction_in_range(shaped:RID, start:int, end:int)virtualconst🔗
Returns dominant direction of in the range of text.
int_shaped_text_get_ellipsis_glyph_count(shaped:RID)virtualrequiredconst🔗
Returns number of glyphs in the ellipsis.
constGlyph*_shaped_text_get_ellipsis_glyphs(shaped:RID)virtualrequiredconst🔗
Returns array of the glyphs in the ellipsis.
int_shaped_text_get_ellipsis_pos(shaped:RID)virtualrequiredconst🔗
Returns position of the ellipsis.
int_shaped_text_get_glyph_count(shaped:RID)virtualrequiredconst🔗
Returns number of glyphs in the buffer.
constGlyph*_shaped_text_get_glyphs(shaped:RID)virtualrequiredconst🔗
Returns an array of glyphs in the visual order.
Vector2_shaped_text_get_grapheme_bounds(shaped:RID, pos:int)virtualconst🔗
Returns composite character's bounds as offsets from the start of the line.
Direction_shaped_text_get_inferred_direction(shaped:RID)virtualconst🔗
Returns direction of the text, inferred by the BiDi algorithm.
PackedInt32Array_shaped_text_get_line_breaks(shaped:RID, width:float, start:int, break_flags:BitField[LineBreakFlag])virtualconst🔗
Breaks text to the lines and returns character ranges for each line.
PackedInt32Array_shaped_text_get_line_breaks_adv(shaped:RID, width:PackedFloat32Array, start:int, once:bool, break_flags:BitField[LineBreakFlag])virtualconst🔗
Breaks text to the lines and columns. Returns character ranges for each segment.
int_shaped_text_get_object_glyph(shaped:RID, key:Variant)virtualrequiredconst🔗
Returns the glyph index of the inline object.
Vector2i_shaped_text_get_object_range(shaped:RID, key:Variant)virtualrequiredconst🔗
Returns the character range of the inline object.
Rect2_shaped_text_get_object_rect(shaped:RID, key:Variant)virtualrequiredconst🔗
Returns bounding rectangle of the inline object.
Array_shaped_text_get_objects(shaped:RID)virtualrequiredconst🔗
Returns array of inline objects.
Orientation_shaped_text_get_orientation(shaped:RID)virtualconst🔗
Returns text orientation.
RID_shaped_text_get_parent(shaped:RID)virtualrequiredconst🔗
Returns the parent buffer from which the substring originates.
bool_shaped_text_get_preserve_control(shaped:RID)virtualconst🔗
Returnstrueif text buffer is configured to display control characters.
bool_shaped_text_get_preserve_invalid(shaped:RID)virtualconst🔗
Returnstrueif text buffer is configured to display hexadecimal codes in place of invalid characters.
Vector2i_shaped_text_get_range(shaped:RID)virtualrequiredconst🔗
Returns substring buffer character range in the parent buffer.
PackedVector2Array_shaped_text_get_selection(shaped:RID, start:int, end:int)virtualconst🔗
Returns selection rectangles for the specified character range.
Vector2_shaped_text_get_size(shaped:RID)virtualrequiredconst🔗
Returns size of the text.
int_shaped_text_get_spacing(shaped:RID, spacing:SpacingType)virtualconst🔗
Returns extra spacing added between glyphs or lines in pixels.
int_shaped_text_get_trim_pos(shaped:RID)virtualrequiredconst🔗
Returns the position of the overrun trim.
float_shaped_text_get_underline_position(shaped:RID)virtualrequiredconst🔗
Returns pixel offset of the underline below the baseline.
float_shaped_text_get_underline_thickness(shaped:RID)virtualrequiredconst🔗
Returns thickness of the underline.
float_shaped_text_get_width(shaped:RID)virtualrequiredconst🔗
Returns width (for horizontal layout) or height (for vertical) of the text.
PackedInt32Array_shaped_text_get_word_breaks(shaped:RID, grapheme_flags:BitField[GraphemeFlag], skip_grapheme_flags:BitField[GraphemeFlag])virtualconst🔗
Breaks text into words and returns array of character ranges. Usegrapheme_flagsto set what characters are used for breaking.
bool_shaped_text_has_object(shaped:RID, key:Variant)virtualrequiredconst🔗
Returnstrueif an object withkeyis embedded in this shaped text buffer.
int_shaped_text_hit_test_grapheme(shaped:RID, coord:float)virtualconst🔗
Returns grapheme index at the specified pixel offset at the baseline, or-1if none is found.
int_shaped_text_hit_test_position(shaped:RID, coord:float)virtualconst🔗
Returns caret character offset at the specified pixel offset at the baseline. This function always returns a valid position.
bool_shaped_text_is_ready(shaped:RID)virtualrequiredconst🔗
Returnstrueif buffer is successfully shaped.
int_shaped_text_next_character_pos(shaped:RID, pos:int)virtualconst🔗
Returns composite character end position closest to thepos.
int_shaped_text_next_grapheme_pos(shaped:RID, pos:int)virtualconst🔗
Returns grapheme end position closest to thepos.
void_shaped_text_overrun_trim_to_width(shaped:RID, width:float, trim_flags:BitField[TextOverrunFlag])virtual🔗
Trims text if it exceeds the given width.
int_shaped_text_prev_character_pos(shaped:RID, pos:int)virtualconst🔗
Returns composite character start position closest to thepos.
int_shaped_text_prev_grapheme_pos(shaped:RID, pos:int)virtualconst🔗
Returns grapheme start position closest to thepos.
bool_shaped_text_resize_object(shaped:RID, key:Variant, size:Vector2, inline_align:InlineAlignment, baseline:float)virtualrequired🔗
Sets new size and alignment of embedded object.
void_shaped_text_set_bidi_override(shaped:RID, override:Array)virtual🔗
Overrides BiDi for the structured text.
void_shaped_text_set_custom_ellipsis(shaped:RID, char:int)virtual🔗
Sets ellipsis character used for text clipping.
void_shaped_text_set_custom_punctuation(shaped:RID, punct:String)virtual🔗
Sets custom punctuation character list, used for word breaking. If set to empty string, server defaults are used.
void_shaped_text_set_direction(shaped:RID, direction:Direction)virtual🔗
Sets desired text direction. If set toTextServer.DIRECTION_AUTO, direction will be detected based on the buffer contents and current locale.
void_shaped_text_set_orientation(shaped:RID, orientation:Orientation)virtual🔗
Sets desired text orientation.
void_shaped_text_set_preserve_control(shaped:RID, enabled:bool)virtual🔗
If set totruetext buffer will display control characters.
void_shaped_text_set_preserve_invalid(shaped:RID, enabled:bool)virtual🔗
If set totruetext buffer will display invalid characters as hexadecimal codes, otherwise nothing is displayed.
void_shaped_text_set_spacing(shaped:RID, spacing:SpacingType, value:int)virtual🔗
Sets extra spacing added between glyphs or lines in pixels.
bool_shaped_text_shape(shaped:RID)virtualrequired🔗
Shapes buffer if it's not shaped. Returnstrueif the string is shaped successfully.
constGlyph*_shaped_text_sort_logical(shaped:RID)virtualrequired🔗
Returns text glyphs in the logical order.
RID_shaped_text_substr(shaped:RID, start:int, length:int)virtualrequiredconst🔗
Returns text buffer for the substring of the text in theshapedtext buffer (including inline objects).
float_shaped_text_tab_align(shaped:RID, tab_stops:PackedFloat32Array)virtual🔗
Aligns shaped text to the given tab-stops.
bool_shaped_text_update_breaks(shaped:RID)virtual🔗
Updates break points in the shaped text. This method is called by default implementation of text breaking functions.
bool_shaped_text_update_justification_ops(shaped:RID)virtual🔗
Updates justification points in the shaped text. This method is called by default implementation of text justification functions.
bool_spoof_check(string:String)virtualconst🔗
Returnstrueifstringis likely to be an attempt at confusing the reader.
PackedInt32Array_string_get_character_breaks(string:String, language:String)virtualconst🔗
Returns array of the composite character boundaries.
PackedInt32Array_string_get_word_breaks(string:String, language:String, chars_per_line:int)virtualconst🔗
Returns an array of the word break boundaries. Elements in the returned array are the offsets of the start and end of words. Therefore the length of the array is always even.
String_string_to_lower(string:String, language:String)virtualconst🔗
Returns the string converted tolowercase.
String_string_to_title(string:String, language:String)virtualconst🔗
Returns the string converted toTitleCase.
String_string_to_upper(string:String, language:String)virtualconst🔗
Returns the string converted toUPPERCASE.
String_strip_diacritics(string:String)virtualconst🔗
Strips diacritics from the string.
String_tag_to_name(tag:int)virtualconst🔗
Converts the given OpenType tag to the readable name of a feature, variation, script, or language.
void_unreference_oversampling_level(oversampling:float)virtual🔗
Decreases the reference count of the specified oversampling level, and frees the font cache for oversampling level when the reference count reaches zero. This method is called byViewport, and should not be used directly.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
