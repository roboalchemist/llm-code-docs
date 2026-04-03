# Label3D in English

# Label3D

Inherits:GeometryInstance3D<VisualInstance3D<Node3D<Node<Object
A node for displaying plain text in 3D space.

## Description

A node for displaying plain text in 3D space. By adjusting various properties of this node, you can configure things such as the text's appearance and whether it always faces the camera.

## Tutorials

- 3D text
3D text

## Properties

| float | alpha_antialiasing_edge | 0.0 |
|---|---|---|
| AlphaAntiAliasing | alpha_antialiasing_mode | 0 |
| AlphaCutMode | alpha_cut | 0 |
| float | alpha_hash_scale | 1.0 |
| float | alpha_scissor_threshold | 0.5 |
| AutowrapMode | autowrap_mode | 0 |
| BitField[LineBreakFlag] | autowrap_trim_flags | 192 |
| BillboardMode | billboard | 0 |
| ShadowCastingSetting | cast_shadow | 0(overridesGeometryInstance3D) |
| bool | double_sided | true |
| bool | fixed_size | false |
| Font | font |  |
| int | font_size | 32 |
| GIMode | gi_mode | 0(overridesGeometryInstance3D) |
| HorizontalAlignment | horizontal_alignment | 1 |
| BitField[JustificationFlag] | justification_flags | 163 |
| String | language | "" |
| float | line_spacing | 0.0 |
| Color | modulate | Color(1,1,1,1) |
| bool | no_depth_test | false |
| Vector2 | offset | Vector2(0,0) |
| Color | outline_modulate | Color(0,0,0,1) |
| int | outline_render_priority | -1 |
| int | outline_size | 12 |
| float | pixel_size | 0.005 |
| int | render_priority | 0 |
| bool | shaded | false |
| StructuredTextParser | structured_text_bidi_override | 0 |
| Array | structured_text_bidi_override_options | [] |
| String | text | "" |
| Direction | text_direction | 0 |
| TextureFilter | texture_filter | 3 |
| bool | uppercase | false |
| VerticalAlignment | vertical_alignment | 1 |
| float | width | 500.0 |

float
alpha_antialiasing_edge
AlphaAntiAliasing
alpha_antialiasing_mode
AlphaCutMode
alpha_cut
float
alpha_hash_scale
float
alpha_scissor_threshold
AutowrapMode
autowrap_mode
BitField[LineBreakFlag]
autowrap_trim_flags
BillboardMode
billboard
ShadowCastingSetting
cast_shadow
0(overridesGeometryInstance3D)
bool
double_sided
true
bool
fixed_size
false
Font
font
font_size
GIMode
gi_mode
0(overridesGeometryInstance3D)
HorizontalAlignment
horizontal_alignment
BitField[JustificationFlag]
justification_flags
String
language
float
line_spacing
Color
modulate
Color(1,1,1,1)
bool
no_depth_test
false
Vector2
offset
Vector2(0,0)
Color
outline_modulate
Color(0,0,0,1)
outline_render_priority
outline_size
float
pixel_size
0.005
render_priority
bool
shaded
false
StructuredTextParser
structured_text_bidi_override
Array
structured_text_bidi_override_options
String
text
Direction
text_direction
TextureFilter
texture_filter
bool
uppercase
false
VerticalAlignment
vertical_alignment
float
width
500.0

## Methods

| TriangleMesh | generate_triangle_mesh()const |
|---|---|
| bool | get_draw_flag(flag:DrawFlags)const |
| void | set_draw_flag(flag:DrawFlags, enabled:bool) |

TriangleMesh
generate_triangle_mesh()const
bool
get_draw_flag(flag:DrawFlags)const
void
set_draw_flag(flag:DrawFlags, enabled:bool)

## Enumerations

enumDrawFlags:🔗
DrawFlagsFLAG_SHADED=0
If set, lights in the environment affect the label.
DrawFlagsFLAG_DOUBLE_SIDED=1
If set, text can be seen from the back as well. If not, the text is invisible when looking at it from behind.
DrawFlagsFLAG_DISABLE_DEPTH_TEST=2
Disables the depth test, so this object is drawn on top of all others. However, objects drawn after it in the draw order may cover it.
DrawFlagsFLAG_FIXED_SIZE=3
Label is scaled by depth so that it always appears the same size on screen.
DrawFlagsFLAG_MAX=4
Represents the size of theDrawFlagsenum.
enumAlphaCutMode:🔗
AlphaCutModeALPHA_CUT_DISABLED=0
This mode performs standard alpha blending. It can display translucent areas, but transparency sorting issues may be visible when multiple transparent materials are overlapping.GeometryInstance3D.cast_shadowhas no effect when this transparency mode is used; theLabel3Dwill never cast shadows.
AlphaCutModeALPHA_CUT_DISCARD=1
This mode only allows fully transparent or fully opaque pixels. Harsh edges will be visible unless some form of screen-space antialiasing is enabled (seeProjectSettings.rendering/anti_aliasing/quality/screen_space_aa). This mode is also known asalpha testingor1-bit transparency.
Note:This mode might have issues with anti-aliased fonts and outlines, try adjustingalpha_scissor_thresholdor using MSDF font.
Note:When using text with overlapping glyphs (e.g., cursive scripts), this mode might have transparency sorting issues between the main text and the outline.
AlphaCutModeALPHA_CUT_OPAQUE_PREPASS=2
This mode draws fully opaque pixels in the depth prepass. This is slower thanALPHA_CUT_DISABLEDorALPHA_CUT_DISCARD, but it allows displaying translucent areas and smooth edges while using proper sorting.
Note:When using text with overlapping glyphs (e.g., cursive scripts), this mode might have transparency sorting issues between the main text and the outline.
AlphaCutModeALPHA_CUT_HASH=3
This mode draws cuts off all values below a spatially-deterministic threshold, the rest will remain opaque.

## Property Descriptions

floatalpha_antialiasing_edge=0.0🔗

- voidset_alpha_antialiasing_edge(value:float)
voidset_alpha_antialiasing_edge(value:float)
- floatget_alpha_antialiasing_edge()
floatget_alpha_antialiasing_edge()
Threshold at which antialiasing will be applied on the alpha channel.
AlphaAntiAliasingalpha_antialiasing_mode=0🔗
- voidset_alpha_antialiasing(value:AlphaAntiAliasing)
voidset_alpha_antialiasing(value:AlphaAntiAliasing)
- AlphaAntiAliasingget_alpha_antialiasing()
AlphaAntiAliasingget_alpha_antialiasing()
The type of alpha antialiasing to apply.
AlphaCutModealpha_cut=0🔗
- voidset_alpha_cut_mode(value:AlphaCutMode)
voidset_alpha_cut_mode(value:AlphaCutMode)
- AlphaCutModeget_alpha_cut_mode()
AlphaCutModeget_alpha_cut_mode()
The alpha cutting mode to use for the sprite.
floatalpha_hash_scale=1.0🔗
- voidset_alpha_hash_scale(value:float)
voidset_alpha_hash_scale(value:float)
- floatget_alpha_hash_scale()
floatget_alpha_hash_scale()
The hashing scale for Alpha Hash. Recommended values between0and2.
floatalpha_scissor_threshold=0.5🔗
- voidset_alpha_scissor_threshold(value:float)
voidset_alpha_scissor_threshold(value:float)
- floatget_alpha_scissor_threshold()
floatget_alpha_scissor_threshold()
Threshold at which the alpha scissor will discard values.
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
BillboardModebillboard=0🔗
- voidset_billboard_mode(value:BillboardMode)
voidset_billboard_mode(value:BillboardMode)
- BillboardModeget_billboard_mode()
BillboardModeget_billboard_mode()
The billboard mode to use for the label.
booldouble_sided=true🔗
- voidset_draw_flag(flag:DrawFlags, enabled:bool)
voidset_draw_flag(flag:DrawFlags, enabled:bool)
- boolget_draw_flag(flag:DrawFlags)const
boolget_draw_flag(flag:DrawFlags)const
Iftrue, text can be seen from the back as well, iffalse, it is invisible when looking at it from behind.
boolfixed_size=false🔗
- voidset_draw_flag(flag:DrawFlags, enabled:bool)
voidset_draw_flag(flag:DrawFlags, enabled:bool)
- boolget_draw_flag(flag:DrawFlags)const
boolget_draw_flag(flag:DrawFlags)const
Iftrue, the label is rendered at the same size regardless of distance. The label's size on screen is the same as if the camera was1.0units away from the label's origin, regardless of the actual distance from the camera. TheCamera3D's field of view (orCamera3D.sizewhen in orthogonal/frustum mode) still affects the size the label is drawn at.
Fontfont🔗
- voidset_font(value:Font)
voidset_font(value:Font)
- Fontget_font()
Fontget_font()
Font configuration used to display text.
intfont_size=32🔗
- voidset_font_size(value:int)
voidset_font_size(value:int)
- intget_font_size()
intget_font_size()
Font size of theLabel3D's text. To make the font look more detailed when up close, increasefont_sizewhile decreasingpixel_sizeat the same time.
Higher font sizes require more time to render new characters, which can cause stuttering during gameplay.
HorizontalAlignmenthorizontal_alignment=1🔗
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
Stringlanguage=""🔗
- voidset_language(value:String)
voidset_language(value:String)
- Stringget_language()
Stringget_language()
Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.
floatline_spacing=0.0🔗
- voidset_line_spacing(value:float)
voidset_line_spacing(value:float)
- floatget_line_spacing()
floatget_line_spacing()
Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.
Colormodulate=Color(1,1,1,1)🔗
- voidset_modulate(value:Color)
voidset_modulate(value:Color)
- Colorget_modulate()
Colorget_modulate()
TextColorof theLabel3D.
boolno_depth_test=false🔗
- voidset_draw_flag(flag:DrawFlags, enabled:bool)
voidset_draw_flag(flag:DrawFlags, enabled:bool)
- boolget_draw_flag(flag:DrawFlags)const
boolget_draw_flag(flag:DrawFlags)const
Iftrue, depth testing is disabled and the object will be drawn in render order.
Vector2offset=Vector2(0,0)🔗
- voidset_offset(value:Vector2)
voidset_offset(value:Vector2)
- Vector2get_offset()
Vector2get_offset()
The text drawing offset (in pixels).
Coloroutline_modulate=Color(0,0,0,1)🔗
- voidset_outline_modulate(value:Color)
voidset_outline_modulate(value:Color)
- Colorget_outline_modulate()
Colorget_outline_modulate()
The tint of text outline.
intoutline_render_priority=-1🔗
- voidset_outline_render_priority(value:int)
voidset_outline_render_priority(value:int)
- intget_outline_render_priority()
intget_outline_render_priority()
Sets the render priority for the text outline. Higher priority objects will be sorted in front of lower priority objects.
Note:This only applies ifalpha_cutis set toALPHA_CUT_DISABLED(default value).
Note:This only applies to sorting of transparent objects. This will not impact how transparent objects are sorted relative to opaque objects. This is because opaque objects are not sorted, while transparent objects are sorted from back to front (subject to priority).
intoutline_size=12🔗
- voidset_outline_size(value:int)
voidset_outline_size(value:int)
- intget_outline_size()
intget_outline_size()
Text outline size.
floatpixel_size=0.005🔗
- voidset_pixel_size(value:float)
voidset_pixel_size(value:float)
- floatget_pixel_size()
floatget_pixel_size()
The size of one pixel's width on the label to scale it in 3D. To make the font look more detailed when up close, increasefont_sizewhile decreasingpixel_sizeat the same time.
intrender_priority=0🔗
- voidset_render_priority(value:int)
voidset_render_priority(value:int)
- intget_render_priority()
intget_render_priority()
Sets the render priority for the text. Higher priority objects will be sorted in front of lower priority objects.
Note:This only applies ifalpha_cutis set toALPHA_CUT_DISABLED(default value).
Note:This only applies to sorting of transparent objects. This will not impact how transparent objects are sorted relative to opaque objects. This is because opaque objects are not sorted, while transparent objects are sorted from back to front (subject to priority).
boolshaded=false🔗
- voidset_draw_flag(flag:DrawFlags, enabled:bool)
voidset_draw_flag(flag:DrawFlags, enabled:bool)
- boolget_draw_flag(flag:DrawFlags)const
boolget_draw_flag(flag:DrawFlags)const
Iftrue, theLight3Din theEnvironmenthas effects on the label.
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
Stringtext=""🔗
- voidset_text(value:String)
voidset_text(value:String)
- Stringget_text()
Stringget_text()
The text to display on screen.
Directiontext_direction=0🔗
- voidset_text_direction(value:Direction)
voidset_text_direction(value:Direction)
- Directionget_text_direction()
Directionget_text_direction()
Base text writing direction.
TextureFiltertexture_filter=3🔗
- voidset_texture_filter(value:TextureFilter)
voidset_texture_filter(value:TextureFilter)
- TextureFilterget_texture_filter()
TextureFilterget_texture_filter()
Filter flags for the texture.
booluppercase=false🔗
- voidset_uppercase(value:bool)
voidset_uppercase(value:bool)
- boolis_uppercase()
boolis_uppercase()
Iftrue, all the text displays as UPPERCASE.
VerticalAlignmentvertical_alignment=1🔗
- voidset_vertical_alignment(value:VerticalAlignment)
voidset_vertical_alignment(value:VerticalAlignment)
- VerticalAlignmentget_vertical_alignment()
VerticalAlignmentget_vertical_alignment()
Controls the text's vertical alignment. Supports top, center, and bottom.
floatwidth=500.0🔗
- voidset_width(value:float)
voidset_width(value:float)
- floatget_width()
floatget_width()
Text width (in pixels), used for autowrap and fill alignment.

## Method Descriptions

TriangleMeshgenerate_triangle_mesh()const🔗
Returns aTriangleMeshwith the label's vertices following its current configuration (such as itspixel_size).
boolget_draw_flag(flag:DrawFlags)const🔗
Returns the value of the specified flag.
voidset_draw_flag(flag:DrawFlags, enabled:bool)🔗
Iftrue, the specifiedflagwill be enabled.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
