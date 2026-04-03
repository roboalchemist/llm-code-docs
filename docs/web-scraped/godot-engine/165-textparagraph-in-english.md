# TextParagraph in English

# TextParagraph
Inherits:RefCounted<Object
Holds a paragraph of text.

## Description
Abstraction overTextServerfor handling a single paragraph of text.

## Properties

| HorizontalAlignment | alignment | 0 |
|---|---|---|
| BitField[LineBreakFlag] | break_flags | 3 |
| String | custom_punctuation | "" |
| Direction | direction | 0 |
| String | ellipsis_char | "…" |
| BitField[JustificationFlag] | justification_flags | 163 |
| float | line_spacing | 0.0 |
| int | max_lines_visible | -1 |
| Orientation | orientation | 0 |
| bool | preserve_control | false |
| bool | preserve_invalid | true |
| OverrunBehavior | text_overrun_behavior | 0 |
| float | width | -1.0 |

HorizontalAlignment
alignment
BitField[LineBreakFlag]
break_flags
String
custom_punctuation
Direction
direction
String
ellipsis_char
BitField[JustificationFlag]
justification_flags
float
line_spacing
max_lines_visible
Orientation
orientation
bool
preserve_control
false
bool
preserve_invalid
true
OverrunBehavior
text_overrun_behavior
float
width
-1.0

## Methods

| bool | add_object(key:Variant, size:Vector2, inline_align:InlineAlignment= 5, length:int= 1, baseline:float= 0.0) |
|---|---|
| bool | add_string(text:String, font:Font, font_size:int, language:String= "", meta:Variant= null) |
| void | clear() |
| void | clear_dropcap() |
| void | draw(canvas:RID, pos:Vector2, color:Color= Color(1, 1, 1, 1), dc_color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const |
| void | draw_dropcap(canvas:RID, pos:Vector2, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const |
| void | draw_dropcap_outline(canvas:RID, pos:Vector2, outline_size:int= 1, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const |
| void | draw_line(canvas:RID, pos:Vector2, line:int, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const |
| void | draw_line_outline(canvas:RID, pos:Vector2, line:int, outline_size:int= 1, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const |
| void | draw_outline(canvas:RID, pos:Vector2, outline_size:int= 1, color:Color= Color(1, 1, 1, 1), dc_color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const |
| TextParagraph | duplicate()const |
| int | get_dropcap_lines()const |
| RID | get_dropcap_rid()const |
| Vector2 | get_dropcap_size()const |
| Direction | get_inferred_direction()const |
| float | get_line_ascent(line:int)const |
| int | get_line_count()const |
| float | get_line_descent(line:int)const |
| Rect2 | get_line_object_rect(line:int, key:Variant)const |
| Array | get_line_objects(line:int)const |
| Vector2i | get_line_range(line:int)const |
| RID | get_line_rid(line:int)const |
| Vector2 | get_line_size(line:int)const |
| float | get_line_underline_position(line:int)const |
| float | get_line_underline_thickness(line:int)const |
| float | get_line_width(line:int)const |
| Vector2 | get_non_wrapped_size()const |
| Vector2i | get_range()const |
| RID | get_rid()const |
| Vector2 | get_size()const |
| bool | has_object(key:Variant)const |
| int | hit_test(coords:Vector2)const |
| bool | resize_object(key:Variant, size:Vector2, inline_align:InlineAlignment= 5, baseline:float= 0.0) |
| void | set_bidi_override(override:Array) |
| bool | set_dropcap(text:String, font:Font, font_size:int, dropcap_margins:Rect2= Rect2(0, 0, 0, 0), language:String= "") |
| void | tab_align(tab_stops:PackedFloat32Array) |

bool
add_object(key:Variant, size:Vector2, inline_align:InlineAlignment= 5, length:int= 1, baseline:float= 0.0)
bool
add_string(text:String, font:Font, font_size:int, language:String= "", meta:Variant= null)
void
clear()
void
clear_dropcap()
void
draw(canvas:RID, pos:Vector2, color:Color= Color(1, 1, 1, 1), dc_color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const
void
draw_dropcap(canvas:RID, pos:Vector2, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const
void
draw_dropcap_outline(canvas:RID, pos:Vector2, outline_size:int= 1, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const
void
draw_line(canvas:RID, pos:Vector2, line:int, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const
void
draw_line_outline(canvas:RID, pos:Vector2, line:int, outline_size:int= 1, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const
void
draw_outline(canvas:RID, pos:Vector2, outline_size:int= 1, color:Color= Color(1, 1, 1, 1), dc_color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const
TextParagraph
duplicate()const
get_dropcap_lines()const
get_dropcap_rid()const
Vector2
get_dropcap_size()const
Direction
get_inferred_direction()const
float
get_line_ascent(line:int)const
get_line_count()const
float
get_line_descent(line:int)const
Rect2
get_line_object_rect(line:int, key:Variant)const
Array
get_line_objects(line:int)const
Vector2i
get_line_range(line:int)const
get_line_rid(line:int)const
Vector2
get_line_size(line:int)const
float
get_line_underline_position(line:int)const
float
get_line_underline_thickness(line:int)const
float
get_line_width(line:int)const
Vector2
get_non_wrapped_size()const
Vector2i
get_range()const
get_rid()const
Vector2
get_size()const
bool
has_object(key:Variant)const
hit_test(coords:Vector2)const
bool
resize_object(key:Variant, size:Vector2, inline_align:InlineAlignment= 5, baseline:float= 0.0)
void
set_bidi_override(override:Array)
bool
set_dropcap(text:String, font:Font, font_size:int, dropcap_margins:Rect2= Rect2(0, 0, 0, 0), language:String= "")
void
tab_align(tab_stops:PackedFloat32Array)

## Property Descriptions
HorizontalAlignmentalignment=0🔗
- voidset_alignment(value:HorizontalAlignment)
voidset_alignment(value:HorizontalAlignment)
- HorizontalAlignmentget_alignment()
HorizontalAlignmentget_alignment()
Paragraph horizontal alignment.
BitField[LineBreakFlag]break_flags=3🔗
- voidset_break_flags(value:BitField[LineBreakFlag])
voidset_break_flags(value:BitField[LineBreakFlag])
- BitField[LineBreakFlag]get_break_flags()
BitField[LineBreakFlag]get_break_flags()
Line breaking rules. For more info seeTextServer.
Stringcustom_punctuation=""🔗
- voidset_custom_punctuation(value:String)
voidset_custom_punctuation(value:String)
- Stringget_custom_punctuation()
Stringget_custom_punctuation()
Custom punctuation character list, used for word breaking. If set to empty string, server defaults are used.
Directiondirection=0🔗
- voidset_direction(value:Direction)
voidset_direction(value:Direction)
- Directionget_direction()
Directionget_direction()
Text writing direction.
Stringellipsis_char="…"🔗
- voidset_ellipsis_char(value:String)
voidset_ellipsis_char(value:String)
- Stringget_ellipsis_char()
Stringget_ellipsis_char()
Ellipsis character used for text clipping.
BitField[JustificationFlag]justification_flags=163🔗
- voidset_justification_flags(value:BitField[JustificationFlag])
voidset_justification_flags(value:BitField[JustificationFlag])
- BitField[JustificationFlag]get_justification_flags()
BitField[JustificationFlag]get_justification_flags()
Line fill alignment rules.
floatline_spacing=0.0🔗
- voidset_line_spacing(value:float)
voidset_line_spacing(value:float)
- floatget_line_spacing()
floatget_line_spacing()
Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.
intmax_lines_visible=-1🔗
- voidset_max_lines_visible(value:int)
voidset_max_lines_visible(value:int)
- intget_max_lines_visible()
intget_max_lines_visible()
Limits the lines of text shown.
Orientationorientation=0🔗
- voidset_orientation(value:Orientation)
voidset_orientation(value:Orientation)
- Orientationget_orientation()
Orientationget_orientation()
Text orientation.
boolpreserve_control=false🔗
- voidset_preserve_control(value:bool)
voidset_preserve_control(value:bool)
- boolget_preserve_control()
boolget_preserve_control()
If set totruetext will display control characters.
boolpreserve_invalid=true🔗
- voidset_preserve_invalid(value:bool)
voidset_preserve_invalid(value:bool)
- boolget_preserve_invalid()
boolget_preserve_invalid()
If set totruetext will display invalid characters.
OverrunBehaviortext_overrun_behavior=0🔗
- voidset_text_overrun_behavior(value:OverrunBehavior)
voidset_text_overrun_behavior(value:OverrunBehavior)
- OverrunBehaviorget_text_overrun_behavior()
OverrunBehaviorget_text_overrun_behavior()
The clipping behavior when the text exceeds the paragraph's set width.
floatwidth=-1.0🔗
- voidset_width(value:float)
voidset_width(value:float)
- floatget_width()
floatget_width()
Paragraph width.

## Method Descriptions
booladd_object(key:Variant, size:Vector2, inline_align:InlineAlignment= 5, length:int= 1, baseline:float= 0.0)🔗
Adds inline object to the text buffer,keymust be unique. In the text, object is represented aslengthobject replacement characters.
booladd_string(text:String, font:Font, font_size:int, language:String= "", meta:Variant= null)🔗
Adds text span and font to draw it.
voidclear()🔗
Clears text paragraph (removes text and inline objects).
voidclear_dropcap()🔗
Removes dropcap.
voiddraw(canvas:RID, pos:Vector2, color:Color= Color(1, 1, 1, 1), dc_color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const🔗
Draw all lines of the text and drop cap into a canvas item at a given position, withcolor.posspecifies the top left corner of the bounding box. Ifoversamplingis greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.
voiddraw_dropcap(canvas:RID, pos:Vector2, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const🔗
Draw drop cap into a canvas item at a given position, withcolor.posspecifies the top left corner of the bounding box. Ifoversamplingis greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.
voiddraw_dropcap_outline(canvas:RID, pos:Vector2, outline_size:int= 1, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const🔗
Draw drop cap outline into a canvas item at a given position, withcolor.posspecifies the top left corner of the bounding box. Ifoversamplingis greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.
voiddraw_line(canvas:RID, pos:Vector2, line:int, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const🔗
Draw single line of text into a canvas item at a given position, withcolor.posspecifies the top left corner of the bounding box. Ifoversamplingis greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.
voiddraw_line_outline(canvas:RID, pos:Vector2, line:int, outline_size:int= 1, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const🔗
Draw outline of the single line of text into a canvas item at a given position, withcolor.posspecifies the top left corner of the bounding box. Ifoversamplingis greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.
voiddraw_outline(canvas:RID, pos:Vector2, outline_size:int= 1, color:Color= Color(1, 1, 1, 1), dc_color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const🔗
Draw outlines of all lines of the text and drop cap into a canvas item at a given position, withcolor.posspecifies the top left corner of the bounding box. Ifoversamplingis greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.
TextParagraphduplicate()const🔗
Duplicates thisTextParagraph.
intget_dropcap_lines()const🔗
Returns number of lines used by dropcap.
RIDget_dropcap_rid()const🔗
Returns drop cap text buffer RID.
Vector2get_dropcap_size()const🔗
Returns drop cap bounding box size.
Directionget_inferred_direction()const🔗
Returns the text writing direction inferred by the BiDi algorithm.
floatget_line_ascent(line:int)const🔗
Returns the text line ascent (number of pixels above the baseline for horizontal layout or to the left of baseline for vertical).
intget_line_count()const🔗
Returns number of lines in the paragraph.
floatget_line_descent(line:int)const🔗
Returns the text line descent (number of pixels below the baseline for horizontal layout or to the right of baseline for vertical).
Rect2get_line_object_rect(line:int, key:Variant)const🔗
Returns bounding rectangle of the inline object.
Arrayget_line_objects(line:int)const🔗
Returns array of inline objects in the line.
Vector2iget_line_range(line:int)const🔗
Returns character range of the line.
RIDget_line_rid(line:int)const🔗
Returns TextServer line buffer RID.
Vector2get_line_size(line:int)const🔗
Returns size of the bounding box of the line of text. Returned size is rounded up.
floatget_line_underline_position(line:int)const🔗
Returns pixel offset of the underline below the baseline.
floatget_line_underline_thickness(line:int)const🔗
Returns thickness of the underline.
floatget_line_width(line:int)const🔗
Returns width (for horizontal layout) or height (for vertical) of the line of text.
Vector2get_non_wrapped_size()const🔗
Returns the size of the bounding box of the paragraph, without line breaks.
Vector2iget_range()const🔗
Returns the character range of the paragraph.
RIDget_rid()const🔗
Returns TextServer full string buffer RID.
Vector2get_size()const🔗
Returns the size of the bounding box of the paragraph.
boolhas_object(key:Variant)const🔗
Returnstrueif an object withkeyis embedded in this shaped text buffer.
inthit_test(coords:Vector2)const🔗
Returns caret character offset at the specified coordinates. This function always returns a valid position.
boolresize_object(key:Variant, size:Vector2, inline_align:InlineAlignment= 5, baseline:float= 0.0)🔗
Sets new size and alignment of embedded object.
voidset_bidi_override(override:Array)🔗
Overrides BiDi for the structured text.
Override ranges should cover full source text without overlaps. BiDi algorithm will be used on each range separately.
boolset_dropcap(text:String, font:Font, font_size:int, dropcap_margins:Rect2= Rect2(0, 0, 0, 0), language:String= "")🔗
Sets drop cap, overrides previously set drop cap. Drop cap (dropped capital) is a decorative element at the beginning of a paragraph that is larger than the rest of the text.
voidtab_align(tab_stops:PackedFloat32Array)🔗
Aligns paragraph to the given tab-stops.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.