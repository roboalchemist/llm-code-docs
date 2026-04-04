# TextLine in English

# TextLine

Inherits:RefCounted<Object
Holds a line of text.

## Description

Abstraction overTextServerfor handling a single line of text.

## Properties

| HorizontalAlignment | alignment | 0 |
|---|---|---|
| Direction | direction | 0 |
| String | ellipsis_char | "…" |
| BitField[JustificationFlag] | flags | 3 |
| Orientation | orientation | 0 |
| bool | preserve_control | false |
| bool | preserve_invalid | true |
| OverrunBehavior | text_overrun_behavior | 3 |
| float | width | -1.0 |

HorizontalAlignment
alignment
Direction
direction
String
ellipsis_char
BitField[JustificationFlag]
flags
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
| void | draw(canvas:RID, pos:Vector2, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const |
| void | draw_outline(canvas:RID, pos:Vector2, outline_size:int= 1, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const |
| TextLine | duplicate()const |
| Direction | get_inferred_direction()const |
| float | get_line_ascent()const |
| float | get_line_descent()const |
| float | get_line_underline_position()const |
| float | get_line_underline_thickness()const |
| float | get_line_width()const |
| Rect2 | get_object_rect(key:Variant)const |
| Array | get_objects()const |
| RID | get_rid()const |
| Vector2 | get_size()const |
| bool | has_object(key:Variant)const |
| int | hit_test(coords:float)const |
| bool | resize_object(key:Variant, size:Vector2, inline_align:InlineAlignment= 5, baseline:float= 0.0) |
| void | set_bidi_override(override:Array) |
| void | tab_align(tab_stops:PackedFloat32Array) |

bool
add_object(key:Variant, size:Vector2, inline_align:InlineAlignment= 5, length:int= 1, baseline:float= 0.0)
bool
add_string(text:String, font:Font, font_size:int, language:String= "", meta:Variant= null)
void
clear()
void
draw(canvas:RID, pos:Vector2, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const
void
draw_outline(canvas:RID, pos:Vector2, outline_size:int= 1, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const
TextLine
duplicate()const
Direction
get_inferred_direction()const
float
get_line_ascent()const
float
get_line_descent()const
float
get_line_underline_position()const
float
get_line_underline_thickness()const
float
get_line_width()const
Rect2
get_object_rect(key:Variant)const
Array
get_objects()const
get_rid()const
Vector2
get_size()const
bool
has_object(key:Variant)const
hit_test(coords:float)const
bool
resize_object(key:Variant, size:Vector2, inline_align:InlineAlignment= 5, baseline:float= 0.0)
void
set_bidi_override(override:Array)
void
tab_align(tab_stops:PackedFloat32Array)

## Property Descriptions

HorizontalAlignmentalignment=0🔗

- voidset_horizontal_alignment(value:HorizontalAlignment)
voidset_horizontal_alignment(value:HorizontalAlignment)
- HorizontalAlignmentget_horizontal_alignment()
HorizontalAlignmentget_horizontal_alignment()
Sets text alignment within the line as if the line was horizontal.
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
BitField[JustificationFlag]flags=3🔗
- voidset_flags(value:BitField[JustificationFlag])
voidset_flags(value:BitField[JustificationFlag])
- BitField[JustificationFlag]get_flags()
BitField[JustificationFlag]get_flags()
Line alignment rules. For more info seeTextServer.
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
OverrunBehaviortext_overrun_behavior=3🔗
- voidset_text_overrun_behavior(value:OverrunBehavior)
voidset_text_overrun_behavior(value:OverrunBehavior)
- OverrunBehaviorget_text_overrun_behavior()
OverrunBehaviorget_text_overrun_behavior()
The clipping behavior when the text exceeds the text line's set width.
floatwidth=-1.0🔗
- voidset_width(value:float)
voidset_width(value:float)
- floatget_width()
floatget_width()
Text line width.

## Method Descriptions

booladd_object(key:Variant, size:Vector2, inline_align:InlineAlignment= 5, length:int= 1, baseline:float= 0.0)🔗
Adds inline object to the text buffer,keymust be unique. In the text, object is represented aslengthobject replacement characters.
booladd_string(text:String, font:Font, font_size:int, language:String= "", meta:Variant= null)🔗
Adds text span and font to draw it.
voidclear()🔗
Clears text line (removes text and inline objects).
voiddraw(canvas:RID, pos:Vector2, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const🔗
Draw text into a canvas item at a given position, withcolor.posspecifies the top left corner of the bounding box. Ifoversamplingis greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.
voiddraw_outline(canvas:RID, pos:Vector2, outline_size:int= 1, color:Color= Color(1, 1, 1, 1), oversampling:float= 0.0)const🔗
Draw text into a canvas item at a given position, withcolor.posspecifies the top left corner of the bounding box. Ifoversamplingis greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.
TextLineduplicate()const🔗
Duplicates thisTextLine.
Directionget_inferred_direction()const🔗
Returns the text writing direction inferred by the BiDi algorithm.
floatget_line_ascent()const🔗
Returns the text ascent (number of pixels above the baseline for horizontal layout or to the left of baseline for vertical).
floatget_line_descent()const🔗
Returns the text descent (number of pixels below the baseline for horizontal layout or to the right of baseline for vertical).
floatget_line_underline_position()const🔗
Returns pixel offset of the underline below the baseline.
floatget_line_underline_thickness()const🔗
Returns thickness of the underline.
floatget_line_width()const🔗
Returns width (for horizontal layout) or height (for vertical) of the text.
Rect2get_object_rect(key:Variant)const🔗
Returns bounding rectangle of the inline object.
Arrayget_objects()const🔗
Returns array of inline objects.
RIDget_rid()const🔗
Returns TextServer buffer RID.
Vector2get_size()const🔗
Returns size of the bounding box of the text.
boolhas_object(key:Variant)const🔗
Returnstrueif an object withkeyis embedded in this line.
inthit_test(coords:float)const🔗
Returns caret character offset at the specified pixel offset at the baseline. This function always returns a valid position.
boolresize_object(key:Variant, size:Vector2, inline_align:InlineAlignment= 5, baseline:float= 0.0)🔗
Sets new size and alignment of embedded object.
voidset_bidi_override(override:Array)🔗
Overrides BiDi for the structured text.
Override ranges should cover full source text without overlaps. BiDi algorithm will be used on each range separately.
voidtab_align(tab_stops:PackedFloat32Array)🔗
Aligns text to the given tab-stops.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
