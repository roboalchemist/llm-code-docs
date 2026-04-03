# Label in English

# Label

Inherits:Control<CanvasItem<Node<Object
A control for displaying plain text.

## Description

A control for displaying plain text. It gives you control over the horizontal and vertical alignment and can wrap the text inside the node's bounding rectangle. It doesn't support bold, italics, or other rich text formatting. For that, useRichTextLabelinstead.
Note:A single Label node is not designed to display huge amounts of text. To display large amounts of text in a single node, consider usingRichTextLabelinstead as it supports features like an integrated scroll bar and threading.RichTextLabelgenerally performs better when displaying large amounts of text (several pages or more).

## Tutorials

- 2D Dodge The Creeps Demo
2D Dodge The Creeps Demo

## Properties

| AutowrapMode | autowrap_mode | 0 |
|---|---|---|
| BitField[LineBreakFlag] | autowrap_trim_flags | 192 |
| bool | clip_text | false |
| String | ellipsis_char | "…" |
| HorizontalAlignment | horizontal_alignment | 0 |
| BitField[JustificationFlag] | justification_flags | 163 |
| LabelSettings | label_settings |  |
| String | language | "" |
| int | lines_skipped | 0 |
| int | max_lines_visible | -1 |
| MouseFilter | mouse_filter | 2(overridesControl) |
| String | paragraph_separator | "\\n" |
| BitField[SizeFlags] | size_flags_vertical | 4(overridesControl) |
| StructuredTextParser | structured_text_bidi_override | 0 |
| Array | structured_text_bidi_override_options | [] |
| PackedFloat32Array | tab_stops | PackedFloat32Array() |
| String | text | "" |
| TextDirection | text_direction | 0 |
| OverrunBehavior | text_overrun_behavior | 0 |
| bool | uppercase | false |
| VerticalAlignment | vertical_alignment | 0 |
| int | visible_characters | -1 |
| VisibleCharactersBehavior | visible_characters_behavior | 0 |
| float | visible_ratio | 1.0 |

AutowrapMode
autowrap_mode
BitField[LineBreakFlag]
autowrap_trim_flags
bool
clip_text
false
String
ellipsis_char
HorizontalAlignment
horizontal_alignment
BitField[JustificationFlag]
justification_flags
LabelSettings
label_settings
String
language
lines_skipped
max_lines_visible
MouseFilter
mouse_filter
2(overridesControl)
String
paragraph_separator
"\\n"
BitField[SizeFlags]
size_flags_vertical
4(overridesControl)
StructuredTextParser
structured_text_bidi_override
Array
structured_text_bidi_override_options
PackedFloat32Array
tab_stops
PackedFloat32Array()
String
text
TextDirection
text_direction
OverrunBehavior
text_overrun_behavior
bool
uppercase
false
VerticalAlignment
vertical_alignment
visible_characters
VisibleCharactersBehavior
visible_characters_behavior
float
visible_ratio

## Methods

| Rect2 | get_character_bounds(pos:int)const |
|---|---|
| int | get_line_count()const |
| int | get_line_height(line:int= -1)const |
| int | get_total_character_count()const |
| int | get_visible_line_count()const |

Rect2
get_character_bounds(pos:int)const
get_line_count()const
get_line_height(line:int= -1)const
get_total_character_count()const
get_visible_line_count()const

## Theme Properties

| Color | font_color | Color(1,1,1,1) |
|---|---|---|
| Color | font_outline_color | Color(0,0,0,1) |
| Color | font_shadow_color | Color(0,0,0,0) |
| int | line_spacing | 3 |
| int | outline_size | 0 |
| int | paragraph_spacing | 0 |
| int | shadow_offset_x | 1 |
| int | shadow_offset_y | 1 |
| int | shadow_outline_size | 1 |
| Font | font |  |
| int | font_size |  |
| StyleBox | focus |  |
| StyleBox | normal |  |

Color
font_color
Color(1,1,1,1)
Color
font_outline_color
Color(0,0,0,1)
Color
font_shadow_color
Color(0,0,0,0)
line_spacing
outline_size
paragraph_spacing
shadow_offset_x
shadow_offset_y
shadow_outline_size
Font
font
font_size
StyleBox
focus
StyleBox
normal

## Property Descriptions

AutowrapModeautowrap_mode=0🔗

- voidset_autowrap_mode(value:AutowrapMode)
voidset_autowrap_mode(value:AutowrapMode)
- AutowrapModeget_autowrap_mode()
AutowrapModeget_autowrap_mode()
If set to something other thanTextServer.AUTOWRAP_OFF, the text gets wrapped inside the node's bounding rectangle. If you resize the node, it will change its height automatically to show all the text.
BitField[LineBreakFlag]autowrap_trim_flags=192🔗
- voidset_autowrap_trim_flags(value:BitField[LineBreakFlag])
voidset_autowrap_trim_flags(value:BitField[LineBreakFlag])
- BitField[LineBreakFlag]get_autowrap_trim_flags()
BitField[LineBreakFlag]get_autowrap_trim_flags()
Autowrap space trimming flags. SeeTextServer.BREAK_TRIM_START_EDGE_SPACESandTextServer.BREAK_TRIM_END_EDGE_SPACESfor more info.
boolclip_text=false🔗
- voidset_clip_text(value:bool)
voidset_clip_text(value:bool)
- boolis_clipping_text()
boolis_clipping_text()
Iftrue, the Label only shows the text that fits inside its bounding rectangle and will clip text horizontally.
Stringellipsis_char="…"🔗
- voidset_ellipsis_char(value:String)
voidset_ellipsis_char(value:String)
- Stringget_ellipsis_char()
Stringget_ellipsis_char()
Ellipsis character used for text clipping.
HorizontalAlignmenthorizontal_alignment=0🔗
- voidset_horizontal_alignment(value:HorizontalAlignment)
voidset_horizontal_alignment(value:HorizontalAlignment)
- HorizontalAlignmentget_horizontal_alignment()
HorizontalAlignmentget_horizontal_alignment()
Controls the text's horizontal alignment. Supports left, center, right, and fill (also known as justify).
BitField[JustificationFlag]justification_flags=163🔗
- voidset_justification_flags(value:BitField[JustificationFlag])
voidset_justification_flags(value:BitField[JustificationFlag])
- BitField[JustificationFlag]get_justification_flags()
BitField[JustificationFlag]get_justification_flags()
Line fill alignment rules.
LabelSettingslabel_settings🔗
- voidset_label_settings(value:LabelSettings)
voidset_label_settings(value:LabelSettings)
- LabelSettingsget_label_settings()
LabelSettingsget_label_settings()
ALabelSettingsresource that can be shared between multipleLabelnodes. Takes priority over theme properties.
Stringlanguage=""🔗
- voidset_language(value:String)
voidset_language(value:String)
- Stringget_language()
Stringget_language()
Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.
intlines_skipped=0🔗
- voidset_lines_skipped(value:int)
voidset_lines_skipped(value:int)
- intget_lines_skipped()
intget_lines_skipped()
The number of the lines ignored and not displayed from the start of thetextvalue.
intmax_lines_visible=-1🔗
- voidset_max_lines_visible(value:int)
voidset_max_lines_visible(value:int)
- intget_max_lines_visible()
intget_max_lines_visible()
Limits the lines of text the node shows on screen.
Stringparagraph_separator="\\n"🔗
- voidset_paragraph_separator(value:String)
voidset_paragraph_separator(value:String)
- Stringget_paragraph_separator()
Stringget_paragraph_separator()
String used as a paragraph separator. Each paragraph is processed independently, in its own BiDi context.
StructuredTextParserstructured_text_bidi_override=0🔗
- voidset_structured_text_bidi_override(value:StructuredTextParser)
voidset_structured_text_bidi_override(value:StructuredTextParser)
- StructuredTextParserget_structured_text_bidi_override()
StructuredTextParserget_structured_text_bidi_override()
Set BiDi algorithm override for the structured text.
Arraystructured_text_bidi_override_options=[]🔗
- voidset_structured_text_bidi_override_options(value:Array)
voidset_structured_text_bidi_override_options(value:Array)
- Arrayget_structured_text_bidi_override_options()
Arrayget_structured_text_bidi_override_options()
Set additional options for BiDi override.
PackedFloat32Arraytab_stops=PackedFloat32Array()🔗
- voidset_tab_stops(value:PackedFloat32Array)
voidset_tab_stops(value:PackedFloat32Array)
- PackedFloat32Arrayget_tab_stops()
PackedFloat32Arrayget_tab_stops()
Aligns text to the given tab-stops.
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedFloat32Arrayfor more details.
Stringtext=""🔗
- voidset_text(value:String)
voidset_text(value:String)
- Stringget_text()
Stringget_text()
The text to display on screen.
TextDirectiontext_direction=0🔗
- voidset_text_direction(value:TextDirection)
voidset_text_direction(value:TextDirection)
- TextDirectionget_text_direction()
TextDirectionget_text_direction()
Base text writing direction.
OverrunBehaviortext_overrun_behavior=0🔗
- voidset_text_overrun_behavior(value:OverrunBehavior)
voidset_text_overrun_behavior(value:OverrunBehavior)
- OverrunBehaviorget_text_overrun_behavior()
OverrunBehaviorget_text_overrun_behavior()
The clipping behavior when the text exceeds the node's bounding rectangle.
booluppercase=false🔗
- voidset_uppercase(value:bool)
voidset_uppercase(value:bool)
- boolis_uppercase()
boolis_uppercase()
Iftrue, all the text displays as UPPERCASE.
VerticalAlignmentvertical_alignment=0🔗
- voidset_vertical_alignment(value:VerticalAlignment)
voidset_vertical_alignment(value:VerticalAlignment)
- VerticalAlignmentget_vertical_alignment()
VerticalAlignmentget_vertical_alignment()
Controls the text's vertical alignment. Supports top, center, bottom, and fill.
intvisible_characters=-1🔗
- voidset_visible_characters(value:int)
voidset_visible_characters(value:int)
- intget_visible_characters()
intget_visible_characters()
The number of characters to display. If set to-1, all characters are displayed. This can be useful when animating the text appearing in a dialog box.
Note:Setting this property updatesvisible_ratioaccordingly.
Note:Characters are counted as Unicode codepoints. A single visible grapheme may contain multiple codepoints (e.g. certain emoji use three codepoints). A single codepoint may contain two UTF-16 characters, which are used in C# strings.
VisibleCharactersBehaviorvisible_characters_behavior=0🔗
- voidset_visible_characters_behavior(value:VisibleCharactersBehavior)
voidset_visible_characters_behavior(value:VisibleCharactersBehavior)
- VisibleCharactersBehaviorget_visible_characters_behavior()
VisibleCharactersBehaviorget_visible_characters_behavior()
The clipping behavior whenvisible_charactersorvisible_ratiois set.
floatvisible_ratio=1.0🔗
- voidset_visible_ratio(value:float)
voidset_visible_ratio(value:float)
- floatget_visible_ratio()
floatget_visible_ratio()
The fraction of characters to display, relative to the total number of characters (seeget_total_character_count()). If set to1.0, all characters are displayed. If set to0.5, only half of the characters will be displayed. This can be useful when animating the text appearing in a dialog box.
Note:Setting this property updatesvisible_charactersaccordingly.

## Method Descriptions

Rect2get_character_bounds(pos:int)const🔗
Returns the bounding rectangle of the character at positionposin the label's local coordinate system. If the character is a non-visual character orposis outside the valid range, an emptyRect2is returned. If the character is a part of a composite grapheme, the bounding rectangle of the whole grapheme is returned.
intget_line_count()const🔗
Returns the number of lines of text the Label has.
intget_line_height(line:int= -1)const🔗
Returns the height of the lineline.
Iflineis set to-1, returns the biggest line height.
If there are no lines, returns font size in pixels.
intget_total_character_count()const🔗
Returns the total number of printable characters in the text (excluding spaces and newlines).
intget_visible_line_count()const🔗
Returns the number of lines shown. Useful if theLabel's height cannot currently display all lines.

## Theme Property Descriptions

Colorfont_color=Color(1,1,1,1)🔗
Default textColorof theLabel.
Colorfont_outline_color=Color(0,0,0,1)🔗
The color of text outline.
Colorfont_shadow_color=Color(0,0,0,0)🔗
Colorof the text's shadow effect.
intline_spacing=3🔗
Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.
intoutline_size=0🔗
Text outline size.
Note:If using a font withFontFile.multichannel_signed_distance_fieldenabled, itsFontFile.msdf_pixel_rangemust be set to at leasttwicethe value ofoutline_sizefor outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.
Note:Using a value that is larger than half the font size is not recommended, as the font outline may fail to be fully closed in this case.
intparagraph_spacing=0🔗
Vertical space between paragraphs. Added on top ofline_spacing.
intshadow_offset_x=1🔗
The horizontal offset of the text's shadow.
intshadow_offset_y=1🔗
The vertical offset of the text's shadow.
intshadow_outline_size=1🔗
The size of the shadow outline.
Fontfont🔗
Fontused for theLabel's text.
intfont_size🔗
Font size of theLabel's text.
StyleBoxfocus🔗
StyleBoxused when theLabelis focused (when used with assistive apps).
StyleBoxnormal🔗
BackgroundStyleBoxfor theLabel.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
