# Source: https://docs.gtk.org/Pango/

Title: Pango-1.0

URL Source: https://docs.gtk.org/Pango/

Markdown Content:
### Namespace

Internationalized text layout and rendering

**PangoCairo**Cairo support for Pango
[Browse documentation](https://docs.gtk.org/PangoCairo/)
**PangoFc**Fontconfig support for Pango
[Browse documentation](https://docs.gtk.org/PangoFc/)
**PangoFT2**FreeType support for Pango
[Browse documentation](https://docs.gtk.org/PangoFT2/)
**PangoOT**OpenType support for Pango
[Browse documentation](https://docs.gtk.org/PangoOT/)
**PangoXft**Xft support for Pango
[Browse documentation](https://docs.gtk.org/PangoXft/)

*   [The Rendering Pipeline](https://docs.gtk.org/Pango/pango_rendering.html)
*   [Text Attributes and Markup](https://docs.gtk.org/Pango/pango_markup.html)
*   [Fonts and Glyphs](https://docs.gtk.org/Pango/pango_fonts.html)
*   [Bidirectional and Vertical Text](https://docs.gtk.org/Pango/pango_bidi.html)
*   [Tools and Demos](https://docs.gtk.org/Pango/tools.html)
*   [Classes Hierarchy](https://docs.gtk.org/Pango/classes_hierarchy.html)

[Context](https://docs.gtk.org/Pango/class.Context.html "Context")A `PangoContext` stores global information used to control the itemization process.
[Coverage](https://docs.gtk.org/Pango/class.Coverage.html "Coverage")A `PangoCoverage` structure is a map from Unicode characters to `PangoCoverageLevel` values.
[Font](https://docs.gtk.org/Pango/class.Font.html "Font")A `PangoFont` is used to represent a font in a rendering-system-independent manner.
[FontFace](https://docs.gtk.org/Pango/class.FontFace.html "FontFace")A `PangoFontFace` is used to represent a group of fonts with the same family, slant, weight, and width, but varying sizes.
[FontFamily](https://docs.gtk.org/Pango/class.FontFamily.html "FontFamily")A `PangoFontFamily` is used to represent a family of related font faces.
[FontMap](https://docs.gtk.org/Pango/class.FontMap.html "FontMap")A `PangoFontMap` represents the set of fonts available for a particular rendering system.
[Fontset](https://docs.gtk.org/Pango/class.Fontset.html "Fontset")A `PangoFontset` represents a set of `PangoFont` to use when rendering text.
[FontsetSimple](https://docs.gtk.org/Pango/class.FontsetSimple.html "FontsetSimple")`PangoFontsetSimple` is a implementation of the abstract `PangoFontset` base class as an array of fonts.
[Layout](https://docs.gtk.org/Pango/class.Layout.html "Layout")A `PangoLayout` structure represents an entire paragraph of text.
[Renderer](https://docs.gtk.org/Pango/class.Renderer.html "Renderer")`PangoRenderer` is a base class for objects that can render text provided as `PangoGlyphString` or `PangoLayout`.

since: 1.8

[Analysis](https://docs.gtk.org/Pango/struct.Analysis.html "Analysis")The `PangoAnalysis` structure stores information about the properties of a segment of text.
[AttrClass](https://docs.gtk.org/Pango/struct.AttrClass.html "AttrClass")The `PangoAttrClass` structure stores the type and operations for a particular type of attribute.
[AttrColor](https://docs.gtk.org/Pango/struct.AttrColor.html "AttrColor")The `PangoAttrColor` structure is used to represent attributes that are colors.
[AttrFloat](https://docs.gtk.org/Pango/struct.AttrFloat.html "AttrFloat")The `PangoAttrFloat` structure is used to represent attributes with a float or double value.
[AttrFontDesc](https://docs.gtk.org/Pango/struct.AttrFontDesc.html "AttrFontDesc")The `PangoAttrFontDesc` structure is used to store an attribute that sets all aspects of the font description at once.
[AttrFontFeatures](https://docs.gtk.org/Pango/struct.AttrFontFeatures.html "AttrFontFeatures")The `PangoAttrFontFeatures` structure is used to represent OpenType font features as an attribute.

since: 1.38
[Attribute](https://docs.gtk.org/Pango/struct.Attribute.html "Attribute")The `PangoAttribute` structure represents the common portions of all attributes.
[AttrInt](https://docs.gtk.org/Pango/struct.AttrInt.html "AttrInt")The `PangoAttrInt` structure is used to represent attributes with an integer or enumeration value.
[AttrIterator](https://docs.gtk.org/Pango/struct.AttrIterator.html "AttrIterator")A `PangoAttrIterator` is used to iterate through a `PangoAttrList`.
[AttrLanguage](https://docs.gtk.org/Pango/struct.AttrLanguage.html "AttrLanguage")The `PangoAttrLanguage` structure is used to represent attributes that are languages.
[AttrList](https://docs.gtk.org/Pango/struct.AttrList.html "AttrList")A `PangoAttrList` represents a list of attributes that apply to a section of text.
[AttrShape](https://docs.gtk.org/Pango/struct.AttrShape.html "AttrShape")The `PangoAttrShape` structure is used to represent attributes which impose shape restrictions.
[AttrSize](https://docs.gtk.org/Pango/struct.AttrSize.html "AttrSize")The `PangoAttrSize` structure is used to represent attributes which set font size.
[AttrString](https://docs.gtk.org/Pango/struct.AttrString.html "AttrString")The `PangoAttrString` structure is used to represent attributes with a string value.
[Color](https://docs.gtk.org/Pango/struct.Color.html "Color")The `PangoColor` structure is used to represent a color in an uncalibrated RGB color-space.
[FontDescription](https://docs.gtk.org/Pango/struct.FontDescription.html "FontDescription")A `PangoFontDescription` describes a font in an implementation-independent manner.
[FontMetrics](https://docs.gtk.org/Pango/struct.FontMetrics.html "FontMetrics")A `PangoFontMetrics` structure holds the overall metric information for a font.
[GlyphGeometry](https://docs.gtk.org/Pango/struct.GlyphGeometry.html "GlyphGeometry")The `PangoGlyphGeometry` structure contains width and positioning information for a single glyph.
[GlyphInfo](https://docs.gtk.org/Pango/struct.GlyphInfo.html "GlyphInfo")A `PangoGlyphInfo` structure represents a single glyph with positioning information and visual attributes.
[GlyphItem](https://docs.gtk.org/Pango/struct.GlyphItem.html "GlyphItem")A `PangoGlyphItem` is a pair of a `PangoItem` and the glyphs resulting from shaping the items text.
[GlyphItemIter](https://docs.gtk.org/Pango/struct.GlyphItemIter.html "GlyphItemIter")A `PangoGlyphItemIter` is an iterator over the clusters in a `PangoGlyphItem`.

since: 1.22
[GlyphString](https://docs.gtk.org/Pango/struct.GlyphString.html "GlyphString")A `PangoGlyphString` is used to store strings of glyphs with geometry and visual attribute information.
[GlyphVisAttr](https://docs.gtk.org/Pango/struct.GlyphVisAttr.html "GlyphVisAttr")A `PangoGlyphVisAttr` structure communicates information between the shaping and rendering phases.
[Item](https://docs.gtk.org/Pango/struct.Item.html "Item")The `PangoItem` structure stores information about a segment of text.
[Language](https://docs.gtk.org/Pango/struct.Language.html "Language")The `PangoLanguage` structure is used to represent a language.
[LayoutIter](https://docs.gtk.org/Pango/struct.LayoutIter.html "LayoutIter")A `PangoLayoutIter` can be used to iterate over the visual extents of a `PangoLayout`.
[LayoutLine](https://docs.gtk.org/Pango/struct.LayoutLine.html "LayoutLine")A `PangoLayoutLine` represents one of the lines resulting from laying out a paragraph via `PangoLayout`.
[LogAttr](https://docs.gtk.org/Pango/struct.LogAttr.html "LogAttr")The `PangoLogAttr` structure stores information about the attributes of a single character.
[Matrix](https://docs.gtk.org/Pango/struct.Matrix.html "Matrix")A `PangoMatrix` specifies a transformation between user-space and device coordinates.

since: 1.6
[Rectangle](https://docs.gtk.org/Pango/struct.Rectangle.html "Rectangle")The `PangoRectangle` structure represents a rectangle.
[ScriptIter](https://docs.gtk.org/Pango/struct.ScriptIter.html "ScriptIter")A `PangoScriptIter` is used to iterate through a string and identify ranges in different scripts.
[TabArray](https://docs.gtk.org/Pango/struct.TabArray.html "TabArray")A `PangoTabArray` contains an array of tab stops.

[Glyph](https://docs.gtk.org/Pango/alias.Glyph.html "Glyph")A `PangoGlyph` represents a single glyph in the output form of a string.
[GlyphUnit](https://docs.gtk.org/Pango/alias.GlyphUnit.html "GlyphUnit")The `PangoGlyphUnit` type is used to store dimensions within Pango.
[LayoutRun](https://docs.gtk.org/Pango/alias.LayoutRun.html "LayoutRun")A `PangoLayoutRun` represents a single run within a `PangoLayoutLine`.

[Alignment](https://docs.gtk.org/Pango/enum.Alignment.html "Alignment")`PangoAlignment` describes how to align the lines of a `PangoLayout` within the available space.
[AttrType](https://docs.gtk.org/Pango/enum.AttrType.html "AttrType")The `PangoAttrType` distinguishes between different types of attributes.
[BaselineShift](https://docs.gtk.org/Pango/enum.BaselineShift.html "BaselineShift")An enumeration that affects baseline shifts between runs.

since: 1.50
[BidiType](https://docs.gtk.org/Pango/enum.BidiType.html "BidiType")`PangoBidiType` represents the bidirectional character type of a Unicode character.

deprecated: 1.44 since: 1.22
[CoverageLevel](https://docs.gtk.org/Pango/enum.CoverageLevel.html "CoverageLevel")`PangoCoverageLevel` is used to indicate how well a font can represent a particular Unicode character for a particular script.
[Direction](https://docs.gtk.org/Pango/enum.Direction.html "Direction")`PangoDirection` represents a direction in the Unicode bidirectional algorithm.
[EllipsizeMode](https://docs.gtk.org/Pango/enum.EllipsizeMode.html "EllipsizeMode")`PangoEllipsizeMode` describes what sort of ellipsization should be applied to text.
[FontColor](https://docs.gtk.org/Pango/enum.FontColor.html "FontColor")Specifies whether a font should or should not have color glyphs.

since: 1.57
[FontScale](https://docs.gtk.org/Pango/enum.FontScale.html "FontScale")An enumeration that affects font sizes for superscript and subscript positioning and for (emulated) Small Caps.

since: 1.50
[Gravity](https://docs.gtk.org/Pango/enum.Gravity.html "Gravity")`PangoGravity` represents the orientation of glyphs in a segment of text.

since: 1.16
[GravityHint](https://docs.gtk.org/Pango/enum.GravityHint.html "GravityHint")`PangoGravityHint` defines how horizontal scripts should behave in a vertical context.

since: 1.16
[Overline](https://docs.gtk.org/Pango/enum.Overline.html "Overline")The `PangoOverline` enumeration is used to specify whether text should be overlined, and if so, the type of line.

since: 1.46
[RenderPart](https://docs.gtk.org/Pango/enum.RenderPart.html "RenderPart")`PangoRenderPart` defines different items to render for such purposes as setting colors.

since: 1.8
[Script](https://docs.gtk.org/Pango/enum.Script.html "Script")The `PangoScript` enumeration identifies different writing systems.
[Stretch](https://docs.gtk.org/Pango/enum.Stretch.html "Stretch")An enumeration specifying the width of the font relative to other designs within a family.
[Style](https://docs.gtk.org/Pango/enum.Style.html "Style")An enumeration specifying the various slant styles possible for a font.
[TabAlign](https://docs.gtk.org/Pango/enum.TabAlign.html "TabAlign")`PangoTabAlign` specifies where the text appears relative to the tab stop position.
[TextTransform](https://docs.gtk.org/Pango/enum.TextTransform.html "TextTransform")An enumeration that affects how Pango treats characters during shaping.

since: 1.50
[Underline](https://docs.gtk.org/Pango/enum.Underline.html "Underline")The `PangoUnderline` enumeration is used to specify whether text should be underlined, and if so, the type of underlining.
[Variant](https://docs.gtk.org/Pango/enum.Variant.html "Variant")An enumeration specifying capitalization variant of the font.
[Weight](https://docs.gtk.org/Pango/enum.Weight.html "Weight")An enumeration specifying the weight (boldness) of a font.
[WrapMode](https://docs.gtk.org/Pango/enum.WrapMode.html "WrapMode")`PangoWrapMode` describes how to wrap the lines of a `PangoLayout` to the desired width.

[FontMask](https://docs.gtk.org/Pango/flags.FontMask.html "FontMask")The bits in a `PangoFontMask` correspond to the set fields in a `PangoFontDescription`.
[LayoutDeserializeFlags](https://docs.gtk.org/Pango/flags.LayoutDeserializeFlags.html "LayoutDeserializeFlags")Flags that influence the behavior of `pango_layout_deserialize()`.

since: 1.50
[LayoutSerializeFlags](https://docs.gtk.org/Pango/flags.LayoutSerializeFlags.html "LayoutSerializeFlags")Flags that influence the behavior of `pango_layout_serialize()`.

since: 1.50
[ShapeFlags](https://docs.gtk.org/Pango/flags.ShapeFlags.html "ShapeFlags")Flags influencing the shaping process.

since: 1.44
[ShowFlags](https://docs.gtk.org/Pango/flags.ShowFlags.html "ShowFlags")These flags affect how Pango treats characters that are normally not visible in the output.

since: 1.44

[attr_allow_breaks_new](https://docs.gtk.org/Pango/func.attr_allow_breaks_new.html "attr_allow_breaks_new")Create a new allow-breaks attribute.

since: 1.44
[attr_background_alpha_new](https://docs.gtk.org/Pango/func.attr_background_alpha_new.html "attr_background_alpha_new")Create a new background alpha attribute.

since: 1.38
[attr_background_new](https://docs.gtk.org/Pango/func.attr_background_new.html "attr_background_new")Create a new background color attribute.
[attr_baseline_shift_new](https://docs.gtk.org/Pango/func.attr_baseline_shift_new.html "attr_baseline_shift_new")Create a new baseline displacement attribute.

since: 1.50
[attr_break](https://docs.gtk.org/Pango/func.attr_break.html "attr_break")Apply customization from attributes to the breaks in `attrs`.

since: 1.50
[attr_fallback_new](https://docs.gtk.org/Pango/func.attr_fallback_new.html "attr_fallback_new")Create a new font fallback attribute.

since: 1.4
[attr_family_new](https://docs.gtk.org/Pango/func.attr_family_new.html "attr_family_new")Create a new font family attribute.
[attr_font_scale_new](https://docs.gtk.org/Pango/func.attr_font_scale_new.html "attr_font_scale_new")Create a new font scale attribute.

since: 1.50
[attr_foreground_alpha_new](https://docs.gtk.org/Pango/func.attr_foreground_alpha_new.html "attr_foreground_alpha_new")Create a new foreground alpha attribute.

since: 1.38
[attr_foreground_new](https://docs.gtk.org/Pango/func.attr_foreground_new.html "attr_foreground_new")Create a new foreground color attribute.
[attr_gravity_hint_new](https://docs.gtk.org/Pango/func.attr_gravity_hint_new.html "attr_gravity_hint_new")Create a new gravity hint attribute.

since: 1.16
[attr_gravity_new](https://docs.gtk.org/Pango/func.attr_gravity_new.html "attr_gravity_new")Create a new gravity attribute.

since: 1.16
[attr_insert_hyphens_new](https://docs.gtk.org/Pango/func.attr_insert_hyphens_new.html "attr_insert_hyphens_new")Create a new insert-hyphens attribute.

since: 1.44
[attr_letter_spacing_new](https://docs.gtk.org/Pango/func.attr_letter_spacing_new.html "attr_letter_spacing_new")Create a new letter-spacing attribute.

since: 1.6
[attr_line_height_new](https://docs.gtk.org/Pango/func.attr_line_height_new.html "attr_line_height_new")Modify the height of logical line extents by a factor.

since: 1.50
[attr_line_height_new_absolute](https://docs.gtk.org/Pango/func.attr_line_height_new_absolute.html "attr_line_height_new_absolute")Override the height of logical line extents to be `height`.

since: 1.50
[attr_overline_color_new](https://docs.gtk.org/Pango/func.attr_overline_color_new.html "attr_overline_color_new")Create a new overline color attribute.

since: 1.46
[attr_overline_new](https://docs.gtk.org/Pango/func.attr_overline_new.html "attr_overline_new")Create a new overline-style attribute.

since: 1.46
[attr_rise_new](https://docs.gtk.org/Pango/func.attr_rise_new.html "attr_rise_new")Create a new baseline displacement attribute.
[attr_scale_new](https://docs.gtk.org/Pango/func.attr_scale_new.html "attr_scale_new")Create a new font size scale attribute.
[attr_sentence_new](https://docs.gtk.org/Pango/func.attr_sentence_new.html "attr_sentence_new")Marks the range of the attribute as a single sentence.

since: 1.50
[attr_show_new](https://docs.gtk.org/Pango/func.attr_show_new.html "attr_show_new")Create a new attribute that influences how invisible characters are rendered.

since: 1.44
[attr_stretch_new](https://docs.gtk.org/Pango/func.attr_stretch_new.html "attr_stretch_new")Create a new font stretch attribute.
[attr_strikethrough_color_new](https://docs.gtk.org/Pango/func.attr_strikethrough_color_new.html "attr_strikethrough_color_new")Create a new strikethrough color attribute.

since: 1.8
[attr_strikethrough_new](https://docs.gtk.org/Pango/func.attr_strikethrough_new.html "attr_strikethrough_new")Create a new strike-through attribute.
[attr_style_new](https://docs.gtk.org/Pango/func.attr_style_new.html "attr_style_new")Create a new font slant style attribute.
[attr_text_transform_new](https://docs.gtk.org/Pango/func.attr_text_transform_new.html "attr_text_transform_new")Create a new attribute that influences how characters are transformed during shaping.

since: 1.50
[attr_underline_color_new](https://docs.gtk.org/Pango/func.attr_underline_color_new.html "attr_underline_color_new")Create a new underline color attribute.

since: 1.8
[attr_underline_new](https://docs.gtk.org/Pango/func.attr_underline_new.html "attr_underline_new")Create a new underline-style attribute.
[attr_variant_new](https://docs.gtk.org/Pango/func.attr_variant_new.html "attr_variant_new")Create a new font variant attribute (normal or small caps).
[attr_weight_new](https://docs.gtk.org/Pango/func.attr_weight_new.html "attr_weight_new")Create a new font weight attribute.
[attr_word_new](https://docs.gtk.org/Pango/func.attr_word_new.html "attr_word_new")Marks the range of the attribute as a single word.

since: 1.50
[break](https://docs.gtk.org/Pango/func.break.html "break")Determines possible line, word, and character breaks for a string of Unicode text with a single analysis.

deprecated: 1.44
[default_break](https://docs.gtk.org/Pango/func.default_break.html "default_break")This is the default break algorithm.
[extents_to_pixels](https://docs.gtk.org/Pango/func.extents_to_pixels.html "extents_to_pixels")Converts extents from Pango units to device units.

since: 1.16
[find_base_dir](https://docs.gtk.org/Pango/func.find_base_dir.html "find_base_dir")Searches a string the first character that has a strong direction, according to the Unicode bidirectional algorithm.

since: 1.4
[find_paragraph_boundary](https://docs.gtk.org/Pango/func.find_paragraph_boundary.html "find_paragraph_boundary")Locates a paragraph boundary in `text`.
[get_log_attrs](https://docs.gtk.org/Pango/func.get_log_attrs.html "get_log_attrs")Computes a `PangoLogAttr` for each character in `text`.
[get_mirror_char](https://docs.gtk.org/Pango/func.get_mirror_char.html "get_mirror_char")Returns the mirrored character of a Unicode character.

deprecated: 1.30
[is_zero_width](https://docs.gtk.org/Pango/func.is_zero_width.html "is_zero_width")Checks if a character that should not be normally rendered.

since: 1.10
[itemize](https://docs.gtk.org/Pango/func.itemize.html "itemize")Breaks a piece of text into segments with consistent directional level and font.
[itemize_with_base_dir](https://docs.gtk.org/Pango/func.itemize_with_base_dir.html "itemize_with_base_dir")Like `pango_itemize()`, but with an explicitly specified base direction.

since: 1.4
[log2vis_get_embedding_levels](https://docs.gtk.org/Pango/func.log2vis_get_embedding_levels.html "log2vis_get_embedding_levels")Return the bidirectional embedding levels of the input paragraph.

since: 1.4
[markup_parser_finish](https://docs.gtk.org/Pango/func.markup_parser_finish.html "markup_parser_finish")Finishes parsing markup.

since: 1.31.0
[markup_parser_new](https://docs.gtk.org/Pango/func.markup_parser_new.html "markup_parser_new")Incrementally parses marked-up text to create a plain-text string and an attribute list.

since: 1.31.0
[parse_enum](https://docs.gtk.org/Pango/func.parse_enum.html "parse_enum")Parses an enum type and stores the result in `value`.

deprecated: 1.38 since: 1.16
[parse_markup](https://docs.gtk.org/Pango/func.parse_markup.html "parse_markup")Parses marked-up text to create a plain-text string and an attribute list.
[parse_stretch](https://docs.gtk.org/Pango/func.parse_stretch.html "parse_stretch")Parses a font stretch.
[parse_style](https://docs.gtk.org/Pango/func.parse_style.html "parse_style")Parses a font style.
[parse_variant](https://docs.gtk.org/Pango/func.parse_variant.html "parse_variant")Parses a font variant.
[parse_weight](https://docs.gtk.org/Pango/func.parse_weight.html "parse_weight")Parses a font weight.
[quantize_line_geometry](https://docs.gtk.org/Pango/func.quantize_line_geometry.html "quantize_line_geometry")Quantizes the thickness and position of a line to whole device pixels.

since: 1.12
[read_line](https://docs.gtk.org/Pango/func.read_line.html "read_line")Reads an entire line from a file into a buffer.

deprecated: 1.38
[reorder_items](https://docs.gtk.org/Pango/func.reorder_items.html "reorder_items")Reorder items from logical order to visual order.
[scan_int](https://docs.gtk.org/Pango/func.scan_int.html "scan_int")Scans an integer.

deprecated: 1.38
[scan_string](https://docs.gtk.org/Pango/func.scan_string.html "scan_string")Scans a string into a `GString` buffer.

deprecated: 1.38
[scan_word](https://docs.gtk.org/Pango/func.scan_word.html "scan_word")Scans a word into a `GString` buffer.

deprecated: 1.38
[shape](https://docs.gtk.org/Pango/func.shape.html "shape")Convert the characters in `text` into glyphs.
[shape_full](https://docs.gtk.org/Pango/func.shape_full.html "shape_full")Convert the characters in `text` into glyphs.

since: 1.32
[shape_item](https://docs.gtk.org/Pango/func.shape_item.html "shape_item")Convert the characters in `item` into glyphs.

since: 1.50
[shape_with_flags](https://docs.gtk.org/Pango/func.shape_with_flags.html "shape_with_flags")Convert the characters in `text` into glyphs.

since: 1.44
[skip_space](https://docs.gtk.org/Pango/func.skip_space.html "skip_space")Skips 0 or more characters of white space.

deprecated: 1.38
[split_file_list](https://docs.gtk.org/Pango/func.split_file_list.html "split_file_list")Splits a `G_SEARCHPATH_SEPARATOR`-separated list of files, stripping white space and substituting ~/ with $HOME/.

deprecated: 1.38
[tailor_break](https://docs.gtk.org/Pango/func.tailor_break.html "tailor_break")Apply language-specific tailoring to the breaks in `attrs`.

since: 1.44
[trim_string](https://docs.gtk.org/Pango/func.trim_string.html "trim_string")Trims leading and trailing whitespace from a string.

deprecated: 1.38
[unichar_direction](https://docs.gtk.org/Pango/func.unichar_direction.html "unichar_direction")Determines the inherent direction of a character.
[units_from_double](https://docs.gtk.org/Pango/func.units_from_double.html "units_from_double")Converts a floating-point number to Pango units.

since: 1.16
[units_to_double](https://docs.gtk.org/Pango/func.units_to_double.html "units_to_double")Converts a number in Pango units to floating-point.

since: 1.16
[version](https://docs.gtk.org/Pango/func.version.html "version")Returns the encoded version of Pango available at run-time.

since: 1.16
[version_check](https://docs.gtk.org/Pango/func.version_check.html "version_check")Checks that the Pango library in use is compatible with the given version.

since: 1.16
[version_string](https://docs.gtk.org/Pango/func.version_string.html "version_string")Returns the version of Pango available at run-time.

since: 1.16

[ASCENT](https://docs.gtk.org/Pango/func.ASCENT.html "ASCENT")Extracts the _ascent_ from a `PangoRectangle` representing glyph extents.
[DESCENT](https://docs.gtk.org/Pango/func.DESCENT.html "DESCENT")Extracts the _descent_ from a `PangoRectangle` representing glyph extents.
[LBEARING](https://docs.gtk.org/Pango/func.LBEARING.html "LBEARING")Extracts the _left bearing_ from a `PangoRectangle` representing glyph extents.
[PIXELS](https://docs.gtk.org/Pango/func.PIXELS.html "PIXELS")Converts a dimension to device units by rounding.
[PIXELS_CEIL](https://docs.gtk.org/Pango/func.PIXELS_CEIL.html "PIXELS_CEIL")Converts a dimension to device units by ceiling.

since: 1.14
[PIXELS_FLOOR](https://docs.gtk.org/Pango/func.PIXELS_FLOOR.html "PIXELS_FLOOR")Converts a dimension to device units by flooring.

since: 1.14
[RBEARING](https://docs.gtk.org/Pango/func.RBEARING.html "RBEARING")Extracts the _right bearing_ from a `PangoRectangle` representing glyph extents.
[UNITS_CEIL](https://docs.gtk.org/Pango/func.UNITS_CEIL.html "UNITS_CEIL")Rounds a dimension up to whole device units, but does not convert it to device units.

since: 1.50
[UNITS_FLOOR](https://docs.gtk.org/Pango/func.UNITS_FLOOR.html "UNITS_FLOOR")Rounds a dimension down to whole device units, but does not convert it to device units.

since: 1.50
[UNITS_ROUND](https://docs.gtk.org/Pango/func.UNITS_ROUND.html "UNITS_ROUND")Rounds a dimension to whole device units, but does not convert it to device units.

since: 1.18
[VERSION_CHECK](https://docs.gtk.org/Pango/func.VERSION_CHECK.html "VERSION_CHECK")Checks that the version of Pango available at compile-time is not older than the provided version number.
[VERSION_ENCODE](https://docs.gtk.org/Pango/func.VERSION_ENCODE.html "VERSION_ENCODE")This macro encodes the given Pango version into an integer. The numbers returned by `PANGO_VERSION` and `pango_version()` are encoded using this macro. Two encoded version numbers can be compared as integers.

[ANALYSIS_FLAG_CENTERED_BASELINE](https://docs.gtk.org/Pango/const.ANALYSIS_FLAG_CENTERED_BASELINE.html "ANALYSIS_FLAG_CENTERED_BASELINE")Whether the segment should be shifted to center around the baseline.
[ANALYSIS_FLAG_IS_ELLIPSIS](https://docs.gtk.org/Pango/const.ANALYSIS_FLAG_IS_ELLIPSIS.html "ANALYSIS_FLAG_IS_ELLIPSIS")Whether this run holds ellipsized text.
[ANALYSIS_FLAG_NEED_HYPHEN](https://docs.gtk.org/Pango/const.ANALYSIS_FLAG_NEED_HYPHEN.html "ANALYSIS_FLAG_NEED_HYPHEN")Whether to add a hyphen at the end of the run during shaping.
[ATTR_INDEX_FROM_TEXT_BEGINNING](https://docs.gtk.org/Pango/const.ATTR_INDEX_FROM_TEXT_BEGINNING.html "ATTR_INDEX_FROM_TEXT_BEGINNING")Value for `start_index` in `PangoAttribute` that indicates the beginning of the text.
[ATTR_INDEX_TO_TEXT_END](https://docs.gtk.org/Pango/const.ATTR_INDEX_TO_TEXT_END.html "ATTR_INDEX_TO_TEXT_END")Value for `end_index` in `PangoAttribute` that indicates the end of the text.
[GLYPH_EMPTY](https://docs.gtk.org/Pango/const.GLYPH_EMPTY.html "GLYPH_EMPTY")A `PangoGlyph` value that indicates a zero-width empty glpyh.
[GLYPH_INVALID_INPUT](https://docs.gtk.org/Pango/const.GLYPH_INVALID_INPUT.html "GLYPH_INVALID_INPUT")A `PangoGlyph` value for invalid input.
[GLYPH_UNKNOWN_FLAG](https://docs.gtk.org/Pango/const.GLYPH_UNKNOWN_FLAG.html "GLYPH_UNKNOWN_FLAG")Flag used in `PangoGlyph` to turn a `gunichar` value of a valid Unicode character into an unknown-character glyph for that `gunichar`.
[SCALE](https://docs.gtk.org/Pango/const.SCALE.html "SCALE")The scale between dimensions used for Pango distances and device units.
[VERSION_MAJOR](https://docs.gtk.org/Pango/const.VERSION_MAJOR.html "VERSION_MAJOR")The major component of the version of Pango available at compile-time.
[VERSION_MICRO](https://docs.gtk.org/Pango/const.VERSION_MICRO.html "VERSION_MICRO")The micro component of the version of Pango available at compile-time.
[VERSION_MINOR](https://docs.gtk.org/Pango/const.VERSION_MINOR.html "VERSION_MINOR")The minor component of the version of Pango available at compile-time.
[VERSION_STRING](https://docs.gtk.org/Pango/const.VERSION_STRING.html "VERSION_STRING")A string literal containing the version of Pango available at compile-time.
